import openai
import json
import os
import helpers as h

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


good_data = []
index = 0
for chunk in json_data:
    messages=[
        {"role": "system", "content": 'This text was messed up during collection. Can you rewrite it EXACTLY the same but with spaces and correct format? Say nothing else, just return the text formatted correctly wiht no changes.'},
        {"role": "user", "content": chunk}
    ]
    completion = chat_with_gpt3_5turbo(messages)
    print(completion)
    good_data.append(completion['choices'][0]['message']['content'])
    print(index)
    index+= 1
    
h.save_list_to_file(good_data, '/Users/brianprzezdziecki/Research/Mechatronics/STREAM_GPT/DL_IanGoodfellow.json')
    
