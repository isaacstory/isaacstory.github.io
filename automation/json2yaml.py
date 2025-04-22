import os
import yaml
import json

import dotenv

dotenv.load_dotenv()
hash = os.getenv("HASH")
_thisdir = os.path.dirname(os.path.abspath(__file__))
yamldir = f"{_thisdir}/../{hash}/yamlout"
jsondir = f"{_thisdir}/../{hash}/jsonout"


def _load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


def _save_yaml(data, filename):
    with open(filename, "w") as f:
        yaml.dump(data, f)

def main():
    exam_values = _load_json(f"{jsondir}/examvalues.json")
    for e in exam_values:
        if e.get("meta"):
            del e["meta"]
    _save_yaml(exam_values, f"{yamldir}/examvalues-all.yaml")

if __name__ == "__main__":
    main()
