import helpers as h
import os
import openai
import global_vars as gv
import prompts as p
import openai_helpers as oah

openai.api_key = gv.OPENAI_API_KEY

# chunks = h.read_list_from_file('/Users/brianprzezdziecki/Research/Mechatronics/STREAM_GPT/DeepLearningChunks OCR 8.json')

# chunk_index = 0
    
# while chunk_index < len(chunks):
#     print(chunk_index)
#     chunk = chunks[chunk_index]
#     completion = oah.index_chunk(chunk)
#     h.save_key_value_to_json(f'chunk{chunk_index}', completion, '/Users/brianprzezdziecki/Research/Mechatronics/STREAM_GPT/ideas3.json')
#     chunk_index += 1

oah.summarize_layer('/Users/brianprzezdziecki/Research/Mechatronics/STREAM_GPT/ideas.json', '/Users/brianprzezdziecki/Research/Mechatronics/STREAM_GPT/ideas_layer2.json')

# while chunk_index < len(chunks):
#     print(chunk_index)
#     chunk = chunks[chunk_index]
#     messages=[
#         {"role": "system", "content": p.indexing_system_message},
#         {"role": "user", "content": chunk}
#     ]
#     completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo-16k",
#     messages=messages,
#     functions=p.indexing_function,
#     function_call={"name": "construct_list"},
#     temperature=0.0,
#     )
#     print(completion)
#     h.save_ideas_to_json(completion.choices[0].message['function_call']['arguments'], f'chunk{chunk_index}', '/Users/brianprzezdziecki/Research/Mechatronics/STREAM_GPT/ideas.json')
#     chunk_index += 1
