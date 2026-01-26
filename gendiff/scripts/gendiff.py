import argparse


def main():
    gendiff_parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    gendiff_parser.add_argument("first_file")
    gendiff_parser.add_argument("second_file")
    args = gendiff_parser.parse_args()
    return args


if __name__ == "__main__":
    main()
