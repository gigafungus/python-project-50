import argparse
import json
from pathlib import Path


def main():
    gendiff_parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
    )
    gendiff_parser.add_argument("first_file")
    gendiff_parser.add_argument("second_file")
    gendiff_parser.add_argument("-f", "--format", help="set format of output")
    args = gendiff_parser.parse_args()
    file_1 = open_file(args.first_file)
    file_2 = open_file(args.second_file)
    print(generate_diff(file_1, file_2))


def open_file(string):
    path = Path(string)
    with path.open() as file:
        data = json.load(file)
    return data


def generate_diff(filepath1, filepath2):
    f1 = open_file(filepath1)
    f2 = open_file(filepath2)
    result = {}
    for k, v in sorted((f1 | f2).items()):
        if k not in f2.keys():
            result[f"  - {k}"] = f1[k]
        elif k not in f1.keys():
            result[f"  + {k}"] = f2[k]
        else:
            if f1[k] == f2[k]:
                result[f"    {k}"] = v
            else:
                result[f"  - {k}"] = f1[k]
                result[f"  + {k}"] = f2[k]
    line = (f'{k}: {json.dumps(v).strip('"')}' for k, v in result.items())
    return "{\n" + "\n".join(line) + "\n}"


if __name__ == "__main__":
    main()
