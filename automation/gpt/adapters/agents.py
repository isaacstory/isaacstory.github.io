import os
import requests
from openai import OpenAI
client = OpenAI()

def get_or_create(agent, agent_instructions):
    existing_agent = get_assistant_by_name(agent)
    if existing_agent:
        return existing_agent.id
    else:
        new_agent = client.beta.assistants.create(
            model='gpt-4o',
            name=agent,
            instructions=agent_instructions,
            tools=[{'type':'code_interpreter'}, {'type':'file_search'}]
        )
        return new_agent.id

def get_assistant_by_name(agent):
    assistants = list(client.beta.assistants.list())
    assistants = [a for a in assistants if a.name == agent]
    if len(assistants) == 0:
        return None
    return assistants[0]

def get_yaml_response(agent_id, prompt, filein):
    file_id = upload_file(filein)
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt,
        attachments=[{'file_id': file_id, 'tools': [{'type':'code_interpreter'}, {'type':'file_search'}]}]
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=agent_id,
        # instructions="Please address the user as Jane Doe. The user has a premium account."
    )
    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        response = list(messages)[0].content[0].text.value
    else:
        response = run.status
    delete_file(file_id)
    return response

def upload_file(filepath):
    headers = {
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}',
        # 'Content-Type': 'multipart/form-data'
    }
    with open(filepath, 'rb') as file:
        # read file as bytes
        filebytes = file.read()
        files = {
            'file': ('a.pdf', filebytes),
            'purpose': (None, 'assistants')
        }
        response = requests.post('https://api.openai.com/v1/files', headers=headers, files=files)
        return response.json()['id']

def delete_file(file_id):
    headers = {
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'
    }
    response = requests.delete(f'https://api.openai.com/v1/files/{file_id}', headers=headers)
    return response.status_code


def uploadfiletoopenai(path):
    pass    

