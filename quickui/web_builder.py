#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: Python APIs to build the web page to be rendered

from flask import Flask, Response as FlaskResponse, jsonify, render_template
from flask_socketio import SocketIO, emit
from quickui.config import Config
from quickui.analyzer import ExtractArgs
from typing import Dict
from subprocess import Popen, PIPE, CalledProcessError
from pathlib import Path

import threading
import json


app = Flask(__name__, template_folder="../templates", static_folder="../static")
socketio = SocketIO(app, logger=True, async_mode="threading")

thread = None


@app.route("/v1/status")
def status()->jsonify:
    """
    A very simple status check
    return: "OK" if status is good

    Returns:
        Jsonified value
    """
    health = {
                "healthy": True,
                "version": app.config["VERSION"]
             }
    return jsonify(health=health)


@app.route("/")
def index()->FlaskResponse:
    """
    Rendering the main index file to view the arg parser dashboard
    """
    return render_template("index.html", form_fields=app.config["FORM_FIELDS"], file_path=Path(app.config["FILE_PATH"]).name)


@socketio.on('connect', namespace='/stream')
def on_connect():
    """
    Notifies when a connection is established to the frontend socket
    """
    print("Client Connected")


def background_stuff(args):
    """
    Background thread which actually runs the python process
    """
    print("Background thread")
    socketio.emit("process_output", {"data": "Output ->"}, namespace="/stream")

    with app.test_request_context("/"):
        try:
            p = Popen(args, stdout=PIPE, stderr=PIPE)

            for line in iter(p.stdout.readline, b''):
                socketio.emit("process_output", {'data': json.loads(json.dumps(line.decode().strip()))},
                              namespace="/stream")

            for line in iter(p.stderr.readline, b''):
                socketio.emit("process_output", {'data': {"error": json.loads(json.dumps(line.decode().strip()))}},
                              namespace="/stream")

        except CalledProcessError as e:
            print(e.__str__())

        socketio.emit("process_output", {"data": "Process Run Completed."}, namespace="/stream")


@socketio.on('run_script', namespace='/stream')
def on_message(message: Dict):
    global thread
    args = ["python", app.config["FILE_PATH"]]

    for argument, value in message["data"].items():
        if argument == "term_id" or argument == "action":
            continue
        args.append(str(argument))

        if value:
            args.append(str(value))
        else:
            args.append("")

    emit('process_output', {'data': " ".join([str(x) for x in args])})

    if thread is None or not thread.is_alive():
        thread = threading.Thread(target=background_stuff, args=[args])
        thread.start()


@socketio.on('disconnect', namespace='/stream')
def on_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    # Pick a random port number to avoid collisions
    file_path = "C:\\Users\\AadeshBagmar\\PycharmProjects\\QuickUI\\examples\\investment_portfolio.py"
    ea = ExtractArgs(file_path)
    config = Config(ea.find_args(), file_path)
    app.config.from_object(config)

    port_number = 5000
    socketio.run(app, port=port_number)