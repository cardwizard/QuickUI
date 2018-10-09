#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: Config files as required by the web builder

from typing import Dict

class Config:
    """
    Contains the details extracted by the analyzer in form of a dictionary.
    Also maintains the version of the module
    """
    VERSION = "0.0.1"

    def __init__(self, config_details: Dict):
        """
        Helps initialize the form_fields using the config_details variable

        Args:
            config_details: Contains all key/value pairs created by parsing a documents argparse.

        """
        Config.FORM_FIELDS = config_details