#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: Python APIs to build the web page to be rendered

import sys
from quickui.config import Config
from quickui.analyzer import ExtractArgs
from quickui.web_builder import app, socketio

import os

def main():
    if len(sys.argv) < 2:
        print("Please enter your file name separated by space. e.g.")
        print("python -m quickui cool-python-file.py")
        return

    file_path = sys.argv[1]
    print(file_path)
    print(os.getcwd())

    ea = ExtractArgs(file_path)
    config = Config(ea.find_args(), file_path)
    app.config.from_object(config)


    if len(sys.argv) > 2:
        port_number = sys.argv[2]
    else:
        port_number = os.environ.get("PORT", 8756)
    print(port_number)

    socketio.run(app, port=port_number)


if __name__ == '__main__':
    main()
