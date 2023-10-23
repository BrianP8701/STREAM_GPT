from stream_gpt.knowledge_tree.main import add_document_to_tree
from stream_gpt.knowledge_tree.tree.tree_class import Global_Knowledge_Tree
import pytest

@pytest.mark.skip(reason="Not ready yet")
def test_add_document_to_tree():
    my_tree = Global_Knowledge_Tree()
    with open('/Users/brianprzezdziecki/Research/Mechatronics/STREAM_GPT/data/library/STREAM_Report.txt', 'r') as file:
        text = file.read()
    add_document_to_tree(my_tree, text, 'STREAM_Report', 'Take note of all ')