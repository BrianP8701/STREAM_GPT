'''
    This file contains functions that are used to manipulate, chunk, filter text.
'''

def chunk_text(text, chunk_char_size=6000):
    '''
        This method breaks your text into chunks of chunk_char_size with 10% overlap.

        Args:
        - text   (string): The actual text you want to be saved in the tree
        - prompt (string): Describe how you want the text to be saved in the tree

        Returns:
        - chunks (list): List of chunks of text
    '''
    overlap_size = int(chunk_char_size * 0.10)
    chunks = []
    start_idx = 0

    while start_idx < len(text):
        end_idx = start_idx + chunk_char_size
        chunks.append(text[start_idx:end_idx])
        start_idx += (chunk_char_size - overlap_size)  # Move start index forward, less the overlap

    return chunks
