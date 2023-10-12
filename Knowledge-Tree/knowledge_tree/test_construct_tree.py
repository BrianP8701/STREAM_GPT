from main import add_document_to_tree, get_context_from_tree
from tree.tree_class import Global_Knowledge_Tree
import json

with open('/Users/brianprzezdziecki/Research/Mechatronics/STREAM_GPT/DL_IanGoodfellow.json', 'r') as f:
    string_list = json.load(f)
concatenated_string = ''.join(string_list)

text = ''.join(string_list)
tree = Global_Knowledge_Tree()

add_document_to_tree(tree, text, 'DL_IanGoodfellow', 'i am seeking mastery in deep learning')