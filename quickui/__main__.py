#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: Python APIs to build the web page to be rendered

import sys
from quickui.config import Config
from quickui.analyzer import ExtractArgs
from quickui.web_builder import app, socketio

import os

def main():

    port_number = os.environ.get("PORT", 8756)

    if len(sys.argv) < 2:
        print("Please use the following syntax: ")
        print("python -m quickui my-awesome-project.py")
        return

    file_path = sys.argv[1]

    ea = ExtractArgs(file_path)
    config = Config(ea.find_args(), file_path)
    app.config.from_object(config)

    socketio.run(app, port=port_number)

if __name__ == '__main__':
    main()
