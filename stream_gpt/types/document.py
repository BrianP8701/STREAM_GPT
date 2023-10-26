import json
from typing import Dict, Any
import os

class Document:
    def __init__(self, metadata: Dict[str, Any]={}, text: str=''):
        self.metadata = metadata
        self.text = text
    
    def save_to_file(self, path):
        '''
        Include the path to the folder you want to save the document in.
        The name of the file will be the title of the document, which is already in the metadata.
        '''
        document_data = {
            'metadata': self.metadata,
            'text': self.text
        }
        
        if self.metadata['type']=='pdf':
            file_path = os.path.join(path, self.metadata['title'].replace('/', '_').replace(' ', '_')) + '.json'
        elif self.metadata['type']=='github_repo':
            file_path = os.path.join(path + self.metadata['path'].replace('/', '_').replace(' ', '_')) + '.json'
        elif self.metadata['type']=='website':
            file_path = os.path.join(path + self.metadata['title'].replace('/', '_').replace(' ', '_')) + '.json'
        else:
            raise Exception(f'Invalid document type: {self.metadata["type"]}')
        
        # Create the directory if it doesn't exist
        os.makedirs(path, exist_ok=True)
        
        with open(file_path, 'w') as file:
            json.dump(document_data, file, indent=4)
    
    @classmethod
    def load_from_file(cls, file_path: str):
        with open(file_path, 'r') as file:
            document_data = json.load(file)
        return cls(
            metadata=document_data.get('metadata', {}),
            text=document_data.get('text', '')
        )
        