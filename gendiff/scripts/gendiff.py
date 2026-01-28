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
    f1 = json.load(open(args.first_file))
    f2 = json.load(open(args.second_file))
    print(generate_diff(f1, f2))


def generate_diff(f1, f2):
    result = {}
    if isinstance(f1, str):
        f1 = json.load(open(f1))
        f2 = json.load(open(f2))
    for k, v in sorted(f1.items()):
        if k not in f2.keys():
            result[f"- {k}"] = v
        elif f1[k] == f2[k]:
            result[f"  {k}"] = v
        else:
            result[f"- {k}"] = v
            result[f"+ {k}"] = f2[k]

    for key in filter(lambda k: k not in f1.keys(), f2.keys()):
        result[f"+ {key}"] = f2[key]

    return (
        "{\n"
        + "\n".join(f"{k}: {json.dumps(v).strip('\'"')}" for k, v in result.items())
        + "\n}"
    )


if __name__ == "__main__":
    main()
