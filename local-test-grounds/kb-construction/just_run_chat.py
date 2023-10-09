import openai
import json
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')

def chat_with_gpt3_5turbo(messages, temperature=0.0):
    for message in messages:
        message["content"] = message["content"].encode('latin-1', errors='ignore').decode('latin-1')
    completion = openai.ChatCompletion.create(model='gpt-3.5-turbo-16k',messages=messages,temperature=temperature)
    return completion

def chat_with_gpt3_5instruct(prompt, temperature=0.0):
    response = openai.Completion.create(model="gpt-3.5-turbo-instruct",prompt=prompt, temperature=temperature)
    return response

with open('/Users/brianprzezdziecki/Research/Mechatronics/STREAM_GPT/DeepLearningChunks OCR.json', 'r') as f:
    json_data = json.load(f)
        
chunk = json_data[2]
messages=[
    {"role": "system", "content": 'Take notes of relevant ideas talked about in depth in this text, summarize. Dont take note of superficial mentions. Make sure anything you take note of is not merely mentioned, but explained, discussed in depth, or otherwise elaborated on.'},
    {"role": "user", "content": chunk}
]
prompt = "Take notes of relevant ideas talked about in depth in this text, summarize. Dont take note of superficial mentions. Make sure anything you take note of is not merely mentioned, but explained, discussed in depth, or otherwise elaborated on. Say nothing if nothing is being taught in this text." + chunk
completion = chat_with_gpt3_5instruct(prompt)
print(messages)
print(completion)
print('\n\n')
completion = chat_with_gpt3_5turbo(messages)
print(messages)
print(completion)