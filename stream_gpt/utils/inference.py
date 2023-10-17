import openai
import os
import json
import warnings
import constants.prompts as prompts
import constants.function_schemas as function_schemas
import utils.helpers as helpers

openai.api_key = os.environ.get('OPENAI_API_KEY')

def chat_with_gpt3_turbo(messages, temperature=0.0):
    if type(messages) == str: # In case someone accidentally passes in a string instead of a list of messages
        warnings.warn("chat_with_gpt3_turbo() expects a list of messages, not a string.")
        messages = [{"role": "user", "content": messages}]
    for message in messages:
        message["content"] = message["content"].encode('latin-1', errors='ignore').decode('latin-1')
    completion = openai.ChatCompletion.create(model='gpt-3.5-turbo-16k',messages=messages,temperature=temperature)
    return completion

def function_call_with_gpt3_turbo(messages, functions, function_call='auto', temperature=0.0):
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

def rank_categories(user_prompt, categories, model='gpt-3.5-turbo-16k'):
    '''
        Compare and rank a list of categories based on how well they match the user's prompt.
        Must use a model that supports function calling.
        
        Args:
        - user_prompt (string): Prompt from user
        - categories  (list): List of categories to compare and rank
        - model       (string): Model to use for inference
        
        Returns:
        - ranked_categories (list): List of categories ranked by relevance
    '''
    messages = [{"role": "user", "content": user_prompt},
                {"role": "user", "content": helpers.concatenate_with_indices(categories)}]
    response = function_call_with_gpt3_turbo(messages, function_schemas.rank_categories, function_call={'name':'rank_categories'}).choices[0]['message']['function_call']['arguments']
    return(json.loads(response))
    
    