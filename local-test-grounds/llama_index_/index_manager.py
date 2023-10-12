import sys

from llama_index.node_parser import SimpleNodeParser, HierarchicalNodeParser

from llama_index import VectorStoreIndex
from llama_index import SimpleDirectoryReader
from llama_index.schema import NodeWithScore
from gcs_handler import GCSHandler

class IndexManager(object):

    def __new__(cls):
        """ Make it a Singleton"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(IndexManager, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.node_parser = HierarchicalNodeParser.from_defaults()

        self.documents = SimpleDirectoryReader('./data', recursive=True).load_data()

        self.index = VectorStoreIndex([])
        for doc in self.documents:
            self.index.insert(doc)

        self.nodes = self.node_parser.get_nodes_from_documents(self.documents)

    def insert_document(self, doc):
        self.index.insert(doc)

    def get_doc_from_messages(self, messages):
        retriever = self.index.as_retriever()
        retrieved_nodes: list[NodeWithScore] = retriever.retrieve(messages[-1]['message'])

        return '\n'.join([node.text for node in retrieved_nodes])
    
    

'''
Make sure to first set the environment variable to the service account key.:
    export GOOGLE_APPLICATION_CREDENTIALS="GOOGLE_APPLICATION_CREDENTIALS.json"
'''
# def main():
#     bucket_name = 'oi-hackathon'

#     # To download a file:
#     gcs_handler.download_file('gcs_file_name.txt', 'local_file_path.txt')

#     # To list all files in the bucket:
#     gcs_handler.list_files()

# if __name__ == "__main__":
#     main()
