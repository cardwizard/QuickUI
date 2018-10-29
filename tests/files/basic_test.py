#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: A Sample file to test the QuickUI concept

import argparse
import json

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--check-int', help='integer help', type=int, required=True, default=2)
    parser.add_argument('--check-string', help="string help", type=str, required=False, default="check")
    parser.add_argument('--check-bool', help="bool help and required is not mentioned", type=bool, default=False)
    parser.add_argument('--check-float', help="float help and required is not mentioned", type=float, default=1.3)
    parser.add_argument('--check-json', help="json help", type=json, default=[{"check1": 1, "check2": 2},
                                                                              {"check3": 3, "check4": 4}])
    parser.add_argument('--check-dict', help='dict help', type=dict, default={"test1": 1, "test2": 2, "test3": "aadesh"})
    parser.add_argument('--check-tuple', help='tuple help', type=tuple, default=(1, 3, 4))
    parser.add_argument('--check-list', help='list help', type=list, default=["1", 2, 3.4, ["1", 2]])

    args = parser.parse_args()
    print(args.foo)
    