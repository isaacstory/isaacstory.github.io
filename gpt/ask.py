from adapters import agents
import dotenv
import os
import re

dotenv.load_dotenv()
hash = os.getenv("HASH")
_thisdir = os.path.dirname(os.path.abspath(__file__))
dirout = f"{_thisdir}/../{hash}/yamlout"

def main():
    ask_and_save("summarizer", "summarize_exam", f"{_thisdir}/../{hash}/drive/Exams/20231217 - GPL - CSAP.pdf", dirout)

def ask_and_save(agent, prompt, filein, dirout):
    agent_instructions = load_instructions(agent)
    agent_id = agents.get_or_create(agent, agent_instructions)
    response = agents.get_yaml_response(agent_id, load_prompt(prompt), filein)
    save_yaml_response(filein, dirout, prompt, response)
    # pass

def load_instructions(agent):
    with open(f"{_thisdir}/agents/{agent}.txt", "r") as file:
        return file.read()

def load_prompt(prompt):
    with open(f"{_thisdir}/prompts/{prompt}.txt", "r") as file:
        return file.read()

def save_yaml_response(filein, dirout, prompt, response):
    yaml_response = extract_code_blocks(response)[0]
    filename = filein.split('/')[-1]
    with open(f"{dirout}/{prompt}-{filename}.yaml", "w") as file:
        file.write(yaml_response)
    pass

def extract_code_blocks(markdown_text):
    code_block_pattern = re.compile(r'```(?:\w+)?\n(.*?)\n```', re.DOTALL)
    code_blocks = [block.strip() for block in code_block_pattern.findall(markdown_text)]
    return code_blocks

if __name__ == "__main__":
    main()
