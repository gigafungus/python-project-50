import json


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
