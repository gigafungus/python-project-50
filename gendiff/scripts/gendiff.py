import json
from pathlib import Path

import yaml


def generate_diff(f1, f2):
    def open_file(string):
        path = Path(string)
        if path.suffix == ".json":
            with path.open() as file:
                return json.load(file)
        elif path.suffix in {".yaml", ".yml"}:
            with path.open() as file:
                return yaml.load(file, Loader=yaml.Loader)

    f1 = open_file(f1)
    f2 = open_file(f2)
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

