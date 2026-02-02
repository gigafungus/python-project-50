import argparse

from gendiff import generate_diff


def main():
    gendiff_parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
    )
    gendiff_parser.add_argument("first_file")
    gendiff_parser.add_argument("second_file")
    gendiff_parser.add_argument("-f", "--format", help="set format of output")
    args = gendiff_parser.parse_args()
    file_1 = args.first_file
    file_2 = args.second_file
    print(generate_diff(file_1, file_2))


if __name__ == "__main__":
    main()
