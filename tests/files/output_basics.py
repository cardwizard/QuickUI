#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: A Sample file to test the QuickUI concept

import argparse
import time

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--check-int', help='integer help', type=int, required=True, default=2)
    parser.add_argument('--check-string', help="string help", type=str, required=False, default="check")
    parser.add_argument('--check-bool', help="bool help and required is not mentioned", default=False, type=bool)

    args = parser.parse_args()

    for i in range(10):
        print(args.check_int)
        time.sleep(2)
        print(args.check_string)
        time.sleep(1)
        print(args.check_bool)