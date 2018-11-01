#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: Python APIs to build the web page to be rendered

import argparse
import pandas as pd

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # Checking the boolean type
    parser.add_argument('--deal-offered', help="If the deal was offered", type=bool, default=False)

    parser.add_argument('--mark-cuban', help="Mark Cuban was present", type=bool, default=False)
    parser.add_argument('--kevin-leary', help="Kevin Leary was present", type=bool, default=False)
    parser.add_argument('--barabara-corcoran', help="Barabara Corcoran was present", type=bool, default=False)
    parser.add_argument('--lori-greiner', help="Lori Greiner was present", type=bool, default=False)
    parser.add_argument('--robert-herjavec', help="Robert Herjavec was present", type=bool, default=False)
    parser.add_argument('--daymond-johnson', help="Daymond Johnson was present", type=bool, default=False)

    # Checking the string type. No default value or required
    parser.add_argument('--category', help="Enter the category", type=str)

    # Checking the integer type
    parser.add_argument('--season', help="Enter the shark tank season", type=int, default=5, required=True)

    # Checking the float type check with default value
    parser.add_argument('--minimum-valuation', help="Enter the minimum valuation", type=float, default=1000000.00)

    args = parser.parse_args()
    print(args)