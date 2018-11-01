#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: Python APIs to build the web page to be rendered

import argparse
import pandas as pd

from typing import List


def extract_investments(args)->pd.DataFrame:
    df = pd.read_csv("..\\examples\\Shark Tank Companies.csv")

    df["all_sharks"] = df["shark1"] + df["shark2"] + df["shark3"] + df["shark4"] + df["shark5"]

    if args.deal_offered:
        df = df[df["deal"]]

    if args.mark_cuban:
        df = df[df.all_sharks.str.contains("Mark Cuban")]

    if args.kevin_leary:
        df = df[df.all_sharks.str.contains("Kevin Leary")]

    if args.barabara_corcoran:
        df = df[df.all_sharks.str.contains("Mark Cuban")]

    if args.lori_greiner:
        df = df[df.all_sharks.str.contains("Kevin Leary")]

    if args.robert_herjavec:
        df = df[df.all_sharks.str.contains("Mark Cuban")]

    if args.daymond_johnson:
        df = df[df.all_sharks.str.contains("Kevin Leary")]

    if args.category:
        df = df[df.category.str.contains(args.category)]

    if args.company_title:
        df = df[df.title.str.contains(args.company_title)]

    if args.season != 0:
        df = df[df.season == args.season]

    if args.minimum_valuation:
        df = df[df.valuation >= args.minimum_valuation]

    if args.max_results:
        df = df.head(args.max_results)

    return df




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
    parser.add_argument('--category', help="Enter the category (Substring match)", type=str)
    parser.add_argument('--company-title', help="Enter the name of the company (Substring match)", type=str,
                        required=False)

    # Checking the integer type
    parser.add_argument('--season', help="Enter the shark tank season. Enter -1 for all seasons", type=int, default=-1)

    parser.add_argument('--max-results', help="Maximum number of results to be displayed", type=int,
                        required=True)


    # Checking the float type check with default value
    parser.add_argument('--minimum-valuation', help="Enter the minimum valuation", type=float, default=1000000.00)


    args = parser.parse_args()
    print(args)
    print(extract_investments(args))


