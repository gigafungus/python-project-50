import json
from pathlib import Path

import yaml

from .stylish import stylish


def open_file(string):
    path = Path(string).resolve()
    if path.suffix == ".json":
        with path.open() as file:
            return json.load(file)
    elif path.suffix in {".yaml", ".yml"}:
        with path.open() as file:
            return yaml.load(file, Loader=yaml.Loader)


def build_diff(dict1, dict2):
    keys_1, keys_2 = dict1.keys(), dict2.keys()
    all_keys = sorted(list(keys_1 | keys_2))
    diff = []
    for key in all_keys:
        if key in keys_1 and key not in keys_2:
            diff.append({"key": key, "type": "removed", "value": dict1[key]})
        elif key in keys_2 and key not in keys_1:
            diff.append({"key": key, "type": "added", "value": dict2[key]})
        else:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                diff.append(
                    {
                        "key": key,
                        "type": "nested",
                        "children": build_diff(dict1[key], dict2[key]),
                    }
                )
            else:
                if dict1[key] == dict2[key]:
                    diff.append(
                        {"key": key, "type": "unchanged", "value": dict2[key]}
                    )
                else:
                    diff.append(
                        {
                            "key": key,
                            "type": "updated",
                            "old value": dict1[key],
                            "new value": dict2[key],
                        }
                    )
    return diff


def generate_diff(file1, file2, format_name="stylish"):
    f1 = open_file(file1)
    f2 = open_file(file2)

    diff_tree = build_diff(f1, f2)
    if format_name == "stylish":
        stylish_tree = stylish(diff_tree, 1)
        return "{\n" + stylish_tree + "\n}"
