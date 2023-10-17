'''
    echo 'export PYTHONPATH="${PYTHONPATH}:/Users/brianprzezdziecki/Research/Mechatronics/STREAM_GPT/Knowledge-Tree/knowledge_tree"' >> ~/.bash_profile
    source ~/.bash_profile
'''
from main import add_document_to_tree, get_context_from_tree
from tree.tree_class import Global_Knowledge_Tree
import json
import time

with open('/Users/brianprzezdziecki/Research/Mechatronics/STREAM_GPT/DL_IanGoodfellow.json', 'r') as f:
    string_list = json.load(f)
concatenated_string = ''.join(string_list)

text = ''.join(string_list)
tree = Global_Knowledge_Tree()

start_time = time.time()
print('Adding document to tree...')
subtree = add_document_to_tree(tree, text, 'DL_IanGoodfellow', 'i am seeking mastery in deep learning')

print(f'Finished adding document to tree in {time.time() - start_time} seconds')

subtree.save_to_file('DL_Tree.json')