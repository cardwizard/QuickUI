#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: Python APIs to build the web page to be rendered

from flask import Flask, request, Response as FlaskResponse, jsonify, render_template, flash, redirect, url_for
from random import randint
from QuickUI.config import Config

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route("/v1/status")
def status()->jsonify:
    """
    A very simple status check
    return: "OK" if status is good

    Returns:
        Jsonified value
    """
    health = {
                "healthy": app.config["FORM_FIELDS"]["test"],
                "version": app.config["VERSION"]
             }
    return jsonify(health=health)


@app.route("/")
def index()->FlaskResponse:
    """
    Rendering the main index file to view the arg parser dashboard
    """
    return render_template("index.html")


if __name__ == '__main__':
    # Pick a random port number to avoid collisions
    config = Config({"test": 1})
    app.config.from_object(config)

    port_number = randint(49152, 65535)
    app.run(debug=False, port=randint(49152, 65535))