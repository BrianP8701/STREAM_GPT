'''
This file contains functions that scrape text from PDFs.
'''
import pdfplumber
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract

def pdfplumber_scraper(path):
    all_text = []
    with pdfplumber.open(path) as pdf:
        # Loop through each page
        for page_num in range(len(pdf.pages)):
            # Get the specific page
            page = pdf.pages[page_num]
            
            # Extract text from the page
            text = page.extract_text()      
            all_text.append(text)

    return all_text

def pypdf2_scraper(path):
    pdf_reader = PdfReader(open(path, 'rb'))
    num_pages = len(pdf_reader.pages)
    
    text_list = []  
    
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text_content = page.extract_text()
        text_list.append(text_content)
    return text_list

def pytesseract_scraper(path):
    imgs = convert_from_path(path)
    chunks = []
    for img in imgs:
        chunks.append(pytesseract.image_to_string(img))
    return chunks