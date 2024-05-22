from openai import OpenAI
client = OpenAI()

def get_or_create(agent, agent_instructions):
    try:
        existing_agent = get_assistant_by_name(agent)
        return existing_agent
    except Exception as e:
        if 'not found' in str(e):
            new_agent = client.beta.assistants.create(
                model="gpt-4",
                name=agent,
                instructions=agent_instructions
            )
            return new_agent
        else:
            raise

def get_assistant_by_name(agent):
    assistants = list(client.beta.assistants.list())
    assistants = [a for a in assistants if a.name == agent]
    if len(assistants) == 0:
        return None
    return assistants[0]

def get_yaml_response(agent_id, prompt, filein):
    pass

def save_yaml_response(filein, dirout, prompt, response):
    pass

