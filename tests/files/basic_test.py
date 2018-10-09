#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: A Sample file to test the QuickUI concept

import argparse
import json

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--check-int', help='integer help', type=int, required=True)
    parser.add_argument('--check-string', help="string help", type=str, required=False)
    parser.add_argument('--check-bool', help="bool help and required is not mentioned", type=bool)
    parser.add_argument('--check-float', help="float help and required is not mentioned", type=float)
    parser.add_argument('--check-json', help="json help", type=json)
    parser.add_argument('--check-dict', help='dict help', type=dict)
    parser.add_argument('--check-tuple', help='tuple help', type=tuple)
    parser.add_argument('--check-list', help='list help', type=list)

    args = parser.parse_args()
    print(args.foo)