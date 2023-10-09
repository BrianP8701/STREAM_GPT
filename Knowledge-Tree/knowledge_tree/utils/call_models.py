import openai
import os
import warnings
import constants.prompts as prompts

openai.api_key = os.environ.get('OPENAI_API_KEY')

def chat_with_gpt3_turbo(messages, temperature=0.0):
    if type(messages) == str: # In case someone accidentally passes in a string instead of a list of messages
        warnings.warn("chat_with_gpt3_turbo() expects a list of messages, not a string.")
        messages = [{"role": "user", "content": messages}]
    for message in messages:
        message["content"] = message["content"].encode('latin-1', errors='ignore').decode('latin-1')
    completion = openai.ChatCompletion.create(model='gpt-3.5-turbo-16k',messages=messages,temperature=temperature)
    return completion

def chat_with_gpt3_instruct(prompt, temperature=0.0):
    if type(prompt) == list: # In case someone accidentally passes in a list of messages instead of a prompt
        warnings.warn("chat_with_gpt3_instruct() expects a prompt, not a list of messages.")
        prompt = '\n'.join(f'{message["role"]}: {message["content"]}' for message in prompt)
    response = openai.Completion.create(model="gpt-3.5-turbo-instruct",prompt=prompt, temperature=temperature)
    return response

def summarize(user_prompt, text, model="gpt-3.5-turbo-instruct"):
    if model == "gpt-3.5-turbo-instruct":
        prompt = f'{prompts.keyword_summarization_prompt} {user_prompt}\n{text}'
        response = chat_with_gpt3_instruct(prompt).choices[0].text
    if model == "gpt-3.5-turbo-16k":
        messages=[
            {"role": "system", "content": f'{prompts.summarization_system_message} {user_prompt}'},
            {"role": "user", "content": text}
        ]
        response = chat_with_gpt3_turbo(messages).choices[0]['content']
    return response