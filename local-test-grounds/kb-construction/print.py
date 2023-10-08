import json
from collections.abc import Iterable
import openai_helpers as oah
import helpers as h

with open('/Users/brianprzezdziecki/Research/Mechatronics/STREAM_GPT/local-test-grounds/ideas_layer222.json', 'r') as f:
    json_data = json.load(f)
        
key = 'chunk40'
ideas = json_data[key]
ideas = h.join_strings_with_newline(ideas)
summary = h.extract_ideas(oah.summarize_chunk2(ideas))
h.save_key_value_to_json(key, summary, 'ideas_layer222.json')