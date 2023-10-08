from termcolor import colored
from PIL import Image
from PyPDF2 import PdfReader
import pytesseract
from pdf2image import convert_from_path
import pytesseract
import io
import os
import json

def pdf_to_text_ocr(pdf_path):  
    '''
    Returns a list of strings, each string representing the text on a page of the PDF
    
    Uses pytesseract to perform OCR on each page of the PDF
    More accurate but more computationally expensive than pdf_to_text
    '''
    imgs = pdf_to_pngs(pdf_path)
    return pngs_to_string(imgs)

def pdf_to_text(pdf_path):
    '''
    Returns a list of strings, each string representing the text on a page of the PDF

    Uses PyPDF2 to extract text from each page of the PDF
    More computationlly efficient but less accurate than pdf_to_text_ocr
    '''
    pdf_reader = PdfReader(open(pdf_path, 'rb'))
    num_pages = len(pdf_reader.pages)
    
    text_list = []  
    
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text_content = page.extract_text()
        text_list.append(text_content)
    return text_list

def pdf_to_pngs(pdf_path):
    return convert_from_path(pdf_path)

def pngs_to_string(imgs):
    chunks = []
    for img in imgs:
        print(type(img))
        chunks.append(pytesseract.image_to_string(img))
    return chunks

def save_images_to_folder(image_list, folder_path, file_prefix="image"):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    for idx, img in enumerate(image_list):
        if img.format != 'PNG':
            img = img.convert('RGB')
        filename = f"{file_prefix}{idx}.png"
        full_path = os.path.join(folder_path, filename)
        img.save(full_path, "PNG")

def pretty_print_conversation(messages):
    role_to_color = {
        "system": "red",
        "user": "green",
        "assistant": "blue",
        "function": "magenta",
    }
    
    for message in messages:
        if message["role"] == "system":
            print(colored(f"system: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "user":
            print(colored(f"user: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and message.get("function_call"):
            print(colored(f"assistant: {message['function_call']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and not message.get("function_call"):
            print(colored(f"assistant: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "function":
            print(colored(f"function ({message['name']}): {message['content']}\n", role_to_color[message["role"]]))

def save_list_to_file(my_list, file_path):
    """
    Saves a list to a JSON file.
    """
    with open(file_path, 'w') as f:
        json.dump(my_list, f)
        
def read_list_from_file(file_path):
    """
    Reads a list from a JSON file.
    """
    with open(file_path, 'r') as f:
        return json.load(f)
    
def save_ideas_to_json(json_string, key, file_path):
    # Parse the JSON-like string
    data = json.loads(json_string)

    # Extract the ideas from the parsed JSON
    ideas = [entry["idea"] for entry in data.get("indexed_text", [])]
    
    # Initialize an empty dictionary to hold the JSON data
    json_data = {}
    
    # Check if the file already exists
    try:
        with open(file_path, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        pass  # File doesn't exist, continue with an empty dictionary
    
    # Add the new ideas to the JSON data
    json_data[key] = ideas
    
    # Save the updated JSON data to the file
    with open(file_path, 'w') as f:
        json.dump(json_data, f, indent=4)
        
        
        
def concatenate_together(input_list, x):
    """
    Takes a list of strings and concatenates every x strings together,
    separated by a space. If the total number of strings is not perfectly divisible by 5,
    the remaining strings will still be concatenated.
    """
    output_list = []
    temp_list = []

    for i, item in enumerate(input_list):
        temp_list.append(item)
        
        # Check if we've collected x elements or if we've reached the end of the list
        if (i + 1) % x == 0 or i == len(input_list) - 1:
            concatenated = ' '.join(temp_list)
            output_list.append(concatenated)
            temp_list = []

    return output_list

def save_key_value_to_json(key, value, file_path):
    # Initialize an empty dictionary to hold the JSON data
    json_data = {}
    
    # Check if the JSON file already exists
    try:
        with open(file_path, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, continue with an empty dictionary
        pass
    
    # Add the new key-value pair to the JSON data
    json_data[key] = value
    
    # Save the updated JSON data to the file
    with open(file_path, 'w') as f:
        json.dump(json_data, f, indent=4)
        
def split_chunk(input_str):
    """
    Splits the input string into two overlapping parts.
    The first part contains the first 60% of the string from the left.
    The second part contains the last 60% of the string from the right.
    """
    
    length = len(input_str)
    left_split_index = int(length * 0.6)  # Calculate 60% index from the left
    right_split_index = int(length * 0.4)  # Calculate 40% index from the left, which is equivalent to 60% from the right

    left_part = input_str[:left_split_index]  # Extract the left 60%
    right_part = input_str[-right_split_index:]  # Extract the right 60%

    return left_part, right_part


def extract_ideas(json_str):
    """
    Extracts the 'ideas' from a valid JSON string.
    The JSON should be an object containing a key 'indexed_text' with an array value.
    Each element in the array should be a dictionary with an 'idea' key.
    """
    print('ahhhhhhhhh')
    print(json_str)
    data = json.loads(json_str)
    if 'indexed_text' not in data:
        return []
    ideas = [item['idea'] for item in data['indexed_text']]
    return ideas

def join_strings_with_newline(strings_list):
    """
    Join a list of strings into one string with a newline between each string.
    
    Args:
    - strings_list (list): List of strings.
    
    Returns:
    - str: Concatenated string with newlines.
    """
    return '\n'.join(strings_list)