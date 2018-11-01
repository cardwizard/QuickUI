#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: Python APIs to build the web page to be rendered

import sys
from quickui.config import Config
from quickui.analyzer import ExtractArgs
from quickui.web_builder import app, socketio


if __name__ == '__main__':

    file_path = sys.argv[1]
    ea = ExtractArgs(file_path)
    config = Config(ea.find_args(), file_path)
    app.config.from_object(config)

    port_number = 81194
    socketio.run(app, port=port_number)