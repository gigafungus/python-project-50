import json


def format_(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool) or value is None:
        return json.dumps(value)
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)


def plain(diff_tree, path=""):
    result = []
    for item in diff_tree:
        if path:
            current_path = f"{path}.{item['key']}"
        else:
            current_path = item["key"]
        if item["type"] == "nested":
            result.append(plain(item["children"], current_path))
        elif item["type"] == "added":
            result.append(
                f"Property '{current_path}' was added with value: "
                f"{format_(item['value'])}"
            )
        elif item["type"] == "removed":
            result.append(f"Property '{current_path}' was removed")
        elif item["type"] == "updated":
            result.append(
                f"Property '{current_path}' was updated. "
                f"From {format_(item['old value'])} "
                f"to {format_(item['new value'])}"
            )
    return "\n".join(result)
