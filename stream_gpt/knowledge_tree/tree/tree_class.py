import json
from graphviz import Digraph

class Knowledge_Tree:
    '''
        This is a standard tree data structure, with the addition of a data field for each node.
    '''
    def __init__(self):
        self.nodes = {}
        self.root = None

    def add_node(self, node_id, parent_id=None, data=None):
        '''
        Add a node to the tree.
        
        Parameters:
            node_id: Unique identifier for the node.
            parent_id: Identifier of the parent node (None for root).
            data: Data to be stored in the node.
        
        Raises:
            ValueError: If the node_id already exists or the parent_id does not exist.
        '''
        if node_id in self.nodes:
            raise ValueError(f"Node {node_id} already exists.")
        if parent_id and parent_id not in self.nodes:
            raise ValueError(f"Parent node {parent_id} does not exist.")
        
        self.nodes[node_id] = {"data": data, "children": [], "parent": parent_id}
        if parent_id:
            self.nodes[parent_id]["children"].append(node_id)

    def remove_node(self, node_id):
        '''
        Remove a node and all its children from the tree.
        
        Parameters:
            node_id: Identifier of the node to be removed.
        '''
        children = self.nodes[node_id]["children"]
        for child in children:
            self.remove_node(child)
        
        parent_id = self.nodes[node_id]["parent"]
        if parent_id:
            self.nodes[parent_id]["children"].remove(node_id)
        del self.nodes[node_id]
            
    def add_nodes(self, parent_ids, children_ids_list, data_list=None):
        '''
        Adds multiple nodes to the tree.
        
        Parameters:
            parent_ids: List of identifiers for the parent nodes.
            children_ids_list: List of lists, each containing identifiers for children of a parent.
            data_list: List of data to be stored in the nodes. Defaults to None.
        
        Note:
            The lengths of parent_ids, children_ids_list, and data_list must be the same.
        '''
        if data_list is None:
            data_list = [None] * len(parent_ids)
        for parent_id, children_ids, data in zip(parent_ids, children_ids_list, data_list):
            for child_id in children_ids:
                self.add_node(child_id, parent_id, data)

    def add_parent(self, parent_id, children_ids, data=None):
        '''
        Adds a parent node and its children.
        
        Parameters:
            parent_id: Identifier of the parent node.
            children_ids: List of identifiers for the child nodes.
            data: Data to be stored in the parent and child nodes.
        '''
        if parent_id not in self.nodes:
            self.nodes[parent_id] = {"data": data, "children": [], "parent": None}
        for child_id in children_ids:
            if self.nodes[child_id]["parent"]:
                raise ValueError(f"Child node {child_id} already has a parent.")
            else:
                self.nodes[child_id]["parent"] = parent_id
                self.nodes[parent_id]["children"].append(child_id)
            
    def add_layer(self, node_ids, data_list=None):
        '''
        Adds a layer of nodes without connecting them to any parents.
        
        Parameters:
            node_ids: List of identifiers for the nodes.
            data_list: List of data to be stored in the nodes. Defaults to None.
        '''
        if data_list is None:
            data_list = [None] * len(node_ids)
        for node_id, data in zip(node_ids, data_list):
            self.add_node(node_id, data=data)
    
    def save_to_file(self, file_path):
        '''
        Save the tree to a file in JSON format.
        
        Parameters:
            file_path: The path to the file where the tree will be saved.
        '''
        with open(file_path, 'w') as f:
            json.dump(self.nodes, f)

    def load_from_file(self, file_path):
        '''
        Load the tree from a file.
        
        Parameters:
            file_path: The path to the file from which to load the tree.
        
        Note:
            This will overwrite any existing data in the tree.
        '''
        with open(file_path, 'r') as f:
            self.nodes = json.load(f)

    def to_graphviz(self, file_path='knowledge_tree'):
        '''
        Generate a Graphviz representation of the tree and render it.
        
        Parameters:
            file_path: The path where the Graphviz file will be saved. Defaults to 'knowledge_tree'.
        '''
        dot = Digraph()
        for node_id, node_data in self.nodes.items():
            label = f"{node_id}\n{node_data['data']}"
            dot.node(node_id, label=label)
            for child_id in node_data['children']:
                dot.edge(node_id, child_id)
        dot.render(file_path, view=True)

            
class Global_Knowledge_Tree(Knowledge_Tree):
    '''
        This is the same as Knowledge_Tree, but with a list of root nodes of branches within the tree
        that represent individual documents.
    '''
    def __init__(self):
        super().__init__() 
        self.document_roots = []  
        self.add_node('Global Root Node')
        self.root = 'Global Root Node'
        
    def add_knowledge_tree(self, subtree):
        current_node = self.root
        document_root_data = subtree.nodes[subtree.root]['data']
        for node in subtree.nodes:
            self.add_node(node, data=subtree.nodes[node]['data'])
        traversing_tree = True
        while(traversing_tree):
            if self.are_all_children_documents(current_node):
                traversing_tree = False
                self.add_node(subtree.root, current_node)
            else:
                current_node = subtree.nodes[current_node]['children'][0]
                
    def are_all_children_documents(self, node_id):
        return all(child in self.document_roots for child in self.nodes[node_id]['children'])