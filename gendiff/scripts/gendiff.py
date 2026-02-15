import json
from pathlib import Path

import yaml


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


def stringify(value, depth):

    def _stringify(val, depth):
        if not isinstance(val, dict):
            return str(val)

        result = []
        result.append("{")

        for key in sorted(val.keys()):
            indent = " " * depth * 4
            if isinstance(val[key], dict):
                result.append(
                    f"{indent}{key}: {_stringify(val[key], depth + 1)}"
                )
            else:
                result.append(f"{indent}{key}: {(val[key])}")

        closing = " " * (depth - 1) * 4
        result.append(f"{closing}}}")
        return "\n".join(result)

    return _stringify(value, depth)


def stylish(diff_tree, depth):
    def jsoning(item):
        return json.dumps(item).strip('"')

    result = []
    for item in diff_tree:
        indent = " " * (depth * 4 - 2)
        if item["type"] == "nested":
            result.append(f"{indent}  {item['key']}: {{")
            result.append(stylish(item["children"], depth + 1))
            result.append(f"{indent}  }}")
        else:
            if item["type"] in ["added", "removed", "unchanged"]:
                if isinstance(item["value"], dict):
                    value = stringify(item["value"], depth + 1)
                else:
                    value = jsoning(item["value"])

                if item["type"] == "added":
                    result.append(f"{indent}+ {item['key']}: {value}")
                elif item["type"] == "removed":
                    result.append(f"{indent}- {item['key']}: {value}")
                else:
                    result.append(f"{indent}  {item['key']}: {value}")
            else:
                if isinstance(item["old value"], dict):
                    old_value = stringify(item["old value"], depth + 1)
                else:
                    old_value = jsoning(item["old value"])
                if isinstance(item["new value"], dict):
                    new_value = stringify(item["new value"], depth + 1)
                else:
                    new_value = jsoning(item["new value"])
                result.append(f"{indent}- {item['key']}: {old_value}")
                result.append(f"{indent}+ {item['key']}: {new_value}")
    return "\n".join(result)


def generate_diff(file1, file2, format_name="stylish"):
    f1 = open_file(file1)
    f2 = open_file(file2)

    diff_tree = build_diff(f1, f2)
    if format_name == "stylish":
        stylish_tree = stylish(diff_tree, 1)
        return "{\n" + stylish_tree + "\n}"
