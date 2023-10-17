'''
This file contains functions that scrape text from PDFs.

I want this to be an automatic part of the pipeline, just pass in
a path to a pdf, and get back strings.

After using each a little bit, I found, annoyingly, that each of these
sometimes might break down on some pdfs for no seemeingly good reason.
Issues, like mashing together words, interpreting pictures or math equations
as a bunch of weird characters, adding spaces between each letter, etc.

To get around this, I just use all three of them on a pdf, and then
ask ChatGPT to look at samples from each of them and pick the one that
looks the best. Of course, in the rare case where all three of them
break down, your going to have some ugly data.
'''
import pdfplumber
from pypdf import PdfReader
from pdf2image import convert_from_path
import pytesseract
from stream_gpt.utils import inference
import random

scrapers = [
    'pdfminer_scraper',
    'pdfplumber_scraper',
    'pypdf2_scraper',
    'pytesseract_scraper'
]

def pdf_to_text(path):
    '''
    Try to extract text from a pdf using all of the scrapers in this file.
    Use ChatGPT to pick the best one.
    '''
    # Try each scraper
    all_text = [] # [[chunk1, chunk2, ...], [chunk1, chunk2, ...], ...
    for scraper_name in scrapers:
        scraper = globals()[scraper_name]
        try:
            extracted_text = scraper(path)
            all_text.append(extracted_text)
        except Exception as e:
            raise Exception(f'{scraper} failed: {e}')
        
    # now i need to get samples from each of these in proper token size, and ask chatgpt which one is best
    # Get 3 random samples from each of the scrapers of 100 characters each. Concateate samples from each sample into their own string.
    samples = [] # [sample1, sample2, ...]
    
    # make a list of 3 random numbers between 0 and len(all_text[0])
    rand_chunk_indices = [random.randint(0, len(all_text[0])) for i in range(3)]
    for scraped_chunks in all_text:
        # Get first 100 chars of rand_chunK_indices in scraped_chunks and concatenate them together
        samples.append(''.join([scraped_chunks[i][:100] for i in rand_chunk_indices]))
    
    # Ask chatgpt to pick the best one
    
    
    
def pdfminer_scraper(path):
    from pdfminer.high_level import extract_text
    return extract_text(path)

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