import argparse
import json


def main():
    gendiff_parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
    )
    gendiff_parser.add_argument("first_file")
    gendiff_parser.add_argument("second_file")
    gendiff_parser.add_argument("-f", "--format", help="set format of output")
    args = gendiff_parser.parse_args()
    print(json.load(open(args.first_file)))
    print(json.load(open(args.second_file)))


if __name__ == "__main__":
    main()
