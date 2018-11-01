#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: Python APIs to build the web page to be rendered

import sys
from quickui.config import Config
from quickui.analyzer import ExtractArgs
from quickui.web_builder import app, socketio


def main():
    if len(sys.argv) < 2:
        print("Please enter your file name separated by space. e.g.")
        print("python -m quickui cool-python-file.py")
        return

    file_path = sys.argv[1]
    ea = ExtractArgs(file_path)
    config = Config(ea.find_args(), file_path)
    app.config.from_object(config)

    port_number = 3000
    socketio.run(app, port=port_number)


if __name__ == '__main__':
    main()
