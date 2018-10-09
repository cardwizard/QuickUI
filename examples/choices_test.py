#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: A short description of the purpose of this source file ...


import argparse

def extract_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check-choices', help='string help', type=str, required=True,
                        choices=['rock', 'paper', 'scissors'])

if __name__ == '__main__':
    extract_args()