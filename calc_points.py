#!/usr/bin/python3

import argparse
import re


def main():
    parser = argparse.ArgumentParser(description="Calculate points for given file")
    parser.add_argument("kljuc_sa_poenima", help="path to file containing points")
    args = parser.parse_args()
    points = 0
    max_points = 0
    with open(args.kljuc_sa_poenima) as file:
        contents = file.read()
        points_lst = re.findall(r"([0-9]+)/([0-9]+)", contents)
        for points_str in points_lst:
            point_str, max_point_str = points_str
            points += int(point_str)
            max_points += int(max_point_str)
    print(points, max_points)


if __name__ == "__main__":
    main()
