import stream_gpt.knowledge_tree.tree.tree_class as knowledge_tree
import stream_gpt.utils.inference as call_models
import stream_gpt.constants.prompts as prompts

class Basic_Construct_Tree_From_Chunked_Document:
    '''
        This class creates a hierarchal knowledge tree representing the given text (Already broken into chunks), guided by the given prompt.
        
        1. Add each chunk to the tree as a leaf node
        2. Summarize and label each chunk with keywords. Add these 'compressed chunks' to the tree as parents of the corresponding leaf nodes.
        3. Combine nearby 'compressed chunks' into a single 'compressed chunk', and summarize and label it with keywords. Add this 'compressed chunk' 
           to the tree as a parent of the corresponding 'compressed chunks'.
        4. Repeat step 3 until a singular root summary node is obtained.
    '''
    def __init__(self, chunks, text_id, prompt):
        '''
            Args:
            - chunks    (list): List of text chunks
            - text_id   (string): Unique name of the text you want to be saved in the tree
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
        self.hierarchical_summarization(leaf_layer)
        
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
                self.tree.root = next_layer[0]
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
        index = 0
        for i in range(0, len(layer), granularity):
            nodes_to_process = layer[i:min(i+granularity, len(layer))]
            text = ''
            for node in nodes_to_process:
                text += f"\n{self.tree.nodes[node]['data']}"
            summary = call_models.summarize(self.prompt, text)
            self.tree.add_parent(f'{depth}_{self.text_id}{index}', children_ids=nodes_to_process, data=summary)
            new_layer.append(f'{depth}_{self.text_id}{index}')
        return new_layer