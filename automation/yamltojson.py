import dotenv
import os
import yaml
import json
from automation.inventory import examfiles

dotenv.load_dotenv()
hash = os.getenv("HASH")
_thisdir = os.path.dirname(os.path.abspath(__file__))
yamldir = f"{_thisdir}/../{hash}/yamlout"
jsondir = f"{_thisdir}/../{hash}/jsonout"

def exam_summarize():
    exams = [{'file': f} for f in examfiles]
    for e in exams:
        e.update(read_yaml(f'{yamldir}/summarize_exam-{e["file"]}.yaml'))
        e['meta'] = read_yaml(f'{yamldir}/summarize_exam-{e["file"]}.yaml')
    exams.sort(key=lambda e: e['sample_date'])
    with open(f"{jsondir}/exam.json", "w") as file:
        json.dump(exams, file)

def exam_values():
    exams = [{'file': f} for f in examfiles]
    for e in exams:
        e.update(read_yaml(f'{yamldir}/values_exam-{e["file"]}.yaml'))
        e['meta'] = read_yaml(f'{yamldir}/values_exam-{e["file"]}.yaml')
    exams.sort(key=lambda e: e['sample_date'])
    with open(f"{jsondir}/examvalues.json", "w") as file:
        json.dump(exams, file)

def main():
    exam_summarize()
    exam_values()

def read_yaml(filename):
    with open(filename, "r") as f:
        try:
            content = f.read()
            return yaml.safe_load(content)
        except yaml.YAMLError as e:
            print(f'error reading {filename}: {e}')
            raise


if __name__ == "__main__":
    main()

