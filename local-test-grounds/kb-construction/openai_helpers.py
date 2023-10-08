import openai
import global_vars as gv
import requests
import tiktoken
import prompts as p
import helpers as h
import json

openai.api_key = gv.OPENAI_API_KEY

def chat_completion_request(messages, model='gpt-3.5-turbo-16k', functions=None, function_call='auto', temperature=0.5, max_tokens=None, stop=None, top_p=1, frequency_penalty=0, presence_penalty=0, stream=False):
    completion = openai.ChatCompletion.create(model=model,messages=messages,functions=functions,function_call=function_call,temperature=temperature,max_tokens=max_tokens,stop=stop,top_p=top_p,frequency_penalty=frequency_penalty,presence_penalty=presence_penalty,stream=stream)
    return completion
    
def index_chunk(chunk):
    messages=[
        {"role": "system", "content": p.indexing_system_message3},
        {"role": "user", "content": chunk}
    ]
    print(messages)
    completion = chat_completion_request(messages, functions=p.indexing_function, function_call={"name": "construct_list"}, temperature=0.0)
    if completion.choices[0].finish_reason == 'length':
        return split_and_index_chunk(chunk)
    return h.extract_ideas(completion.choices[0].message['function_call']['arguments'])

def split_and_index_chunk(chunk):
    split_chunks = h.split_chunk(chunk)
    entire_completion = []
    for chunk in split_chunks:
        completion = index_chunk(chunk)
        entire_completion.extend(completion)
    return entire_completion

def summarize_chunk(chunk):
    messages=[
        {"role": "system", "content": p.concise_summarization_system_message},
        {"role": "user", "content": chunk}
    ]
    completion = chat_completion_request(messages, functions=p.indexing_function3, function_call={"name": "summarize"}, temperature=0.5)
    print(messages)
    print(completion)
    return completion.choices[0].message['function_call']['arguments']

def summarize_chunk2(chunk):
    messages=[
        {"role": "system", "content": p.summarization_system_message2},
        {"role": "user", "content": chunk}
    ]
    completion = chat_completion_request(messages, functions=p.indexing_function_sentence, function_call={"name": "summarize"}, temperature=0.0)
    print(messages)
    print(completion)
    return completion.choices[0].message['function_call']['arguments']

def concise_summary(chunk):
    messages=[
        {"role": "system", "content": p.summarization_system_message},
        {"role": "user", "content": chunk}
    ]
    completion = chat_completion_request(messages, functions=p.indexing_function, function_call={"name": "construct_list"}, temperature=0.0)
    return completion.choices[0].message['function_call']['arguments']

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = 0
    for message in messages:
        num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":  # if there's a name, the role is omitted
                num_tokens += -1  # role is always required and always 1 token
    num_tokens += 2  # every reply is primed with <im_start>assistant
    return num_tokens

def summarize_layer(json_path, new_json_path):
    """Summarizes a layer of the knowledge base."""
    # Read the JSON file
    with open(json_path, 'r') as f:
        json_data = json.load(f)
        
    for key in json_data:
        print(key)
        ideas = json_data[key]
        ideas = h.join_strings_with_newline(ideas)
        summary = summarize_chunk(ideas)
        h.save_key_value_to_json(key, summary, new_json_path)
    
    # Save the updated JSON data to the file
    with open(json_path, 'w') as f:
        json.dump(json_data, f, indent=4)