from adapters import agents
import dotenv
import os

dotenv.load_dotenv()
hash = os.getenv("HASH")
_thisdir = os.path.dirname(os.path.abspath(__file__))
dirout = f"{_thisdir}/../{hash}/yamlout"

def main():
    ask_and_save("summarizer", "exam", f"{_thisdir}/../{hash}/drive/Exams/20231217 - GPL - CSAP.pdf", dirout)

def ask_and_save(agent, prompt, filein, dirout):
    agent_instructions = load_instructions(agent)
    agent_id = agents.get_or_create(agent, agent_instructions)
    print(agent_id)

    # response = agents.get_yaml_response(agent_id, load_prompt(prompt), filein)
    # save_yaml_response(filein, dirout, prompt, response)
    # pass

def load_instructions(agent):
    with open(f"{_thisdir}/agents/{agent}.txt", "r") as file:
        return file.read()

def load_prompt(prompt):
    pass

def save_yaml_response(filein, dirout, prompt, response):
    pass

if __name__ == "__main__":
    main()

