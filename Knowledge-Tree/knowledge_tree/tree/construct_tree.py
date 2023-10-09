import knowledge_tree.tree.tree_class as knowledge_tree
import utils.call_models as call_models
import constants.prompts as prompts

class Basic_Construct_Tree_From_String:
    '''
        This class creates a hierarchal knowledge tree representing 
        the given text, guided by the given prompt.
    '''
    def __init__(self, chunks, text_id, prompt):
        '''
            Args:
            - chunks    (list): List of text chunks
            - text_name (string): Unique name of the text you want to be saved in the tree
            - prompt    (string): Describe how you want the text to be saved in the tree

            Returns:
            - tree      (Knowledge_Tree): A hierarchal knowledge tree representing the given text
        '''
        self.chunks = chunks
        self.text_id = text_id
        self.prompt = prompt
        self.tree = knowledge_tree.Knowledge_Tree()
        leaf_layer = [f'0_{text_id}{i}' for i in range(len(chunks) + 1)] # Creates a list of keys for the leaf nodes in the tree
        self.tree.add_layer(leaf_layer, chunks) # Adds chunks to the tree as nodes with no connections yet
        self.hierarchical_summarization(chunks, leaf_layer)
        
    def hierarchical_summarization(self, layer):
        '''
        Initiates a hierarchical summarization process from a layer of unconnected leaf nodes.
        Each leaf node contains a text chunk. The function summarizes each chunk, elevating
        these summaries to form a new parent layer. It then combines nearby nodes within this 
        layer, summarizes them, and continues this process iteratively, forming a hierarchy 
        of summarized information, until a singular root summary node is obtained.
        
            Args:
            - layer         (list): Keys of the nodes in the layer
            
            Returns:
            - None
        '''
        root_summary_done = False
        depth = 0
        while(not root_summary_done):
            depth += 1
            next_layer = self.summarize_layer(layer, depth)
            if(len(next_layer) == 1):
                root_summary_done = True
            layer = next_layer

    def summarize_layer(self, layer, depth, granularity=2):
        '''
        Summarizes a layer of the knowledge base.
        
            Args:
            - layer         (list): Keys of the nodes in the layer
            - depth         (int): Depth of the layer being summarized
            - granularity   (int): How many nodes to combine into a single node

            Returns:
            - new_layer    (list): Keys of the nodes in the layer just created
        '''
        # Loop through {granularity} nodes at a time, summarizing them, and adding the summary as a parent of those nodes
        new_layer = []
        for i in range(0, len(layer), granularity):
            nodes_to_process = layer[i:i+granularity]
            text = ''
            for node in nodes_to_process:
                text += self.tree.nodes[node]['data']
            summary = call_models.summarize(self.prompt, text)
            self.tree.add_parent(f'{depth}_{self.text_id}', children_ids=nodes_to_process, data=summary)
            new_layer.append(f'{depth}_{self.text_id}')
        return new_layer