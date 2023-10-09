import openai
import official_prompts as p
import json
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')

def summarize_chunk(chunk):
    messages=[
        {"role": "system", "content": p.summarization_system_message},
        {"role": "user", "content": chunk}
    ]
    completion = openai.ChatCompletion.create(messages, temperature=0.0)
    print(messages)
    print(completion)
    return undo_json_str(completion.choices[0].message['content'])

def summarize_layer(json_path, new_json_path):
    """Summarizes a layer of the knowledge base."""
    # Read the JSON file
    with open(json_path, 'r') as f:
        json_data = json.load(f)
    
    for key in json_data:
        print(key)
        ideas = json_data[key]
        summary = summarize_chunk(ideas)
        save_key_value_to_json(key, summary, new_json_path)
    
    # Save the updated JSON data to the file
    with open(json_path, 'w') as f:
        json.dump(json_data, f, indent=4)

def undo_json_str(json_str):
    return json.loads(json_str)

def save_key_value_to_json(key, value, json_path):
    """Saves a key-value pair to a JSON file."""
    # Initialize an empty dictionary to hold the JSON data
    json_data = {}
    
    # Check if the file already exists
    try:
        with open(json_path, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        pass  # File doesn't exist, continue with an empty dictionary
    
    # Add the new key-value pair to the JSON data
    json_data[key] = value
    
    # Save the updated JSON data to the file
    with open(json_path, 'w') as f:
        json.dump(json_data, f, indent=4)