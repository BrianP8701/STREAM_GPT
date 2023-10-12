import json

class Knowledge_Tree:
    '''
        This is a standard tree data structure, with the addition of a data field for each node.
    '''
    def __init__(self):
        self.nodes = {}
        self.root = None

    def add_node(self, node_id, parent_id=None, data=None):
        self.nodes[node_id] = {"data": data, "children": [], "parent": parent_id}
        if parent_id:
            self.nodes[parent_id]["children"].append(node_id)
            
    def add_nodes(self, parent_ids, children_ids_list, data_list=None):
        '''Adds a list of nodes to the tree, with connections between corresponding parent and child nodes by index'''
        if data_list is None:
            data_list = [None] * len(parent_ids)
        for parent_id, children_ids, data in zip(parent_ids, children_ids_list, data_list):
            for child_id in children_ids:
                self.add_node(child_id, parent_id, data)

    def add_parent(self, parent_id, children_ids, data=None):
        if parent_id not in self.nodes:
            self.nodes[parent_id] = {"data": data, "children": [], "parent": None}
        for child_id in children_ids:
            self.nodes[child_id] = {"data": data, "children": [], "parent": parent_id}
            self.nodes[parent_id]["children"].append(child_id)

    def remove_node(self, node_id):
        parent_id = self.nodes[node_id]["parent"]
        if parent_id:
            self.nodes[parent_id]["children"].remove(node_id)
        del self.nodes[node_id]

    def add_layer(self, node_ids, data_list=None):
        '''Just adds the list of nodes to the tree, with no connections between them'''
        if data_list is None:
            data_list = [None] * len(node_ids)
        for node_id, data in zip(node_ids, data_list):
            self.add_node(node_id, data=data)


    def save_to_file(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.nodes, f)

    def load_from_file(self, file_path):
        with open(file_path, 'r') as f:
            self.nodes = json.load(f)
            
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
            self.tree.add_node(node, data=subtree.nodes[node]['data'])
        traversing_tree = True
        while(traversing_tree):
            if self.are_all_children_documents(current_node):
                traversing_tree = False
                self.add_node(subtree.root, current_node)
            else:
                current_node = subtree.nodes[current_node]['children'][0]
                
    def are_all_children_documents(self, node_id):
        return all(child in self.document_roots for child in self.nodes[node_id]['children'])