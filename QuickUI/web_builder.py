#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: Python APIs to build the web page to be rendered

from flask import Flask, Response as FlaskResponse, jsonify, render_template
from flask_socketio import SocketIO, emit
from QuickUI.config import Config
from QuickUI.analyzer import ExtractArgs
from typing import Dict
from subprocess import Popen, PIPE
from pathlib import Path

import sys
import threading
import json


app = Flask(__name__, template_folder="../templates", static_folder="../static")
socketio = SocketIO(app, logger=True, engineio_logger=True, async_mode="threading")

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
def test_connect():
    print("Client Connected")


def background_stuff(args):
    print("Background thread")
    socketio.emit("process_output", {"data": "Output ->"}, namespace="/stream")

    with app.test_request_context("/"):
        p = Popen(args, stdout=PIPE)
        for line in iter(p.stdout.readline, b''):
            sys.stdout.write(line.decode())
            socketio.emit("process_output", {'data': json.loads(json.dumps(line.decode().strip()))},
                          namespace="/stream")
        print("Thread run completed")
        socketio.emit("process_output", {"data": "Process Run Completed."}, namespace="/stream")


@socketio.on('run_script', namespace='/stream')
def test_message(message: Dict):
    global thread
    args = ["python", app.config["FILE_PATH"]]

    for argument, value in message["data"].items():
        if argument == "term_id" or argument == "action":
            continue
        args.append(str(argument))
        args.append(str(value))

    emit('process_output', {'data': " ".join([str(x) for x in args])})

    if thread is None or not thread.is_alive():
        thread = threading.Thread(target=background_stuff, args=[args])
        thread.start()


@socketio.on('disconnect', namespace='/stream')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    # Pick a random port number to avoid collisions
    file_path = "C:\\Users\\AadeshBagmar\\PycharmProjects\\QuickUI\\tests\\files\\output_basics.py"
    ea = ExtractArgs(file_path)
    config = Config(ea.find_args(), file_path)
    app.config.from_object(config)

    port_number = 5000
    socketio.run(app, port=port_number)