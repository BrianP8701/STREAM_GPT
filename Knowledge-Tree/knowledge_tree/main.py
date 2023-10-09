'''
    This is the primary file that an end user will stay in to interact with the knowledge tree.
'''
import utils.preprocessing as preprocessing
import utils.helpers as helpers
import tree.construct_tree as construct_tree

def add_document_to_tree(tree, text, text_name, prompt):
    '''
        This method breaks your text into chunks, and adds these chunks to 
        a hierarchal knowledge tree.

        Args:
        - tree      (string): Path to the JSON file that contains the tree
        - text      (string): The actual text you want to be saved in the tree
        - text_name (string): Unique name of the text you want to be saved in the tree
        - prompt    (string): Describe how you want the text to be saved in the tree

        Returns:
        - Path in the knowledge tree to the document that was just added
    '''
    
    # First we need to turn the text into its own knowledge tree, and then add it as a branch to the main tree
    chunks = preprocessing.chunk_text(text)
    helpers.upload_chunks(chunks, text_name) # The actual knowledge tree won't contain the text, but rather pointers to chunks
    text_tree = construct_tree.Basic_Construct_Tree_From_String(chunks, text_name, prompt).tree
    
    
    None
    
def cleanup_and_reorganize_tree(tree):
    '''
        This method takes a knowledge tree and reorganizes it so that it is 
        more robust and token efficient. This method should be called periodically.
        
        Args:
        - tree   (string): Path to the JSON file that contains the tree

        Returns:
        - None
    '''
    None

def get_context_from_tree(tree, messages):
    '''
        This method takes a knowledge tree and a list of messages and returns
        relevant context and the original primary source that will best assist
        the user and the AI.
        
        Args:
        - tree      (string): Path to the JSON file that contains the tree
        - messages  (list): List of messages from the user and the AI

        Returns:
        - context   (string): Context from the knowledge tree that best assists the user and the AI
        - source    (string): Path in the knowledge tree to the document used in context
    '''
    None