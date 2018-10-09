#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: A short description of the purpose of this source file ...


import argparse

def extract_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check-choices', help='string help', type=str, required=True,
                        choices=['rock', 'paper', 'scissors'])

    parser.add_argument('--check-range', type=int, choices=range(1, 4))

if __name__ == '__main__':
    extract_args()