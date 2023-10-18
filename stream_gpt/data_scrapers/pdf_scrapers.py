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
import json
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.high_level import extract_pages

scrapers = [
    'pdfplumber_scraper',
    'pypdf2_scraper',
    'pytesseract_scraper',
    'pdfminer_scraper'
]

def pdf_to_text(path):
    '''
    Extract text from a PDF using all available scrapers and have ChatGPT pick the best extraction.
    '''
    all_text = []  # Store results from each scraper
    for scraper_name in scrapers:
        scraper = globals()[scraper_name]
        try:
            extracted_text = scraper(path)
            all_text.append(extracted_text)
            
            # Save the extracted text for review
            with open(f'data/raw_library/{len(all_text)}{scraper_name}.json', 'w') as f:
                json.dump(extracted_text, f)
        except Exception as e:
            raise Exception(f'{scraper} failed: {e}')

    # Collect random samples from each scraper result for comparison
    samples = []
    rand_chunk_indices = [random.randint(0, len(all_text[0])-1) for _ in range(3)]
    for scraper_index, scraped_chunks in enumerate(all_text, 1):
        sample = ' '.join([scraped_chunks[i][:100] for i in rand_chunk_indices])
        sample = f'<Sample {scraper_index}>: {sample}\n'
        samples.append(sample)

    # Ask ChatGPT to determine the best sample
    best_sample_index = inference.choose_best_scraped_text(samples)
    
    return all_text[best_sample_index]

    

def pdfminer_scraper(path):
    extracted_text = []
    
    for page_layout in extract_pages(path):
        page_text = []  # Temporary list to store text from each element of the current page
        for element in page_layout:
            if isinstance(element, LTTextBoxHorizontal):
                page_text.append(element.get_text())
                
        # Concatenate all the text elements of the current page and append to the main list
        extracted_text.append(' '.join(page_text))
                
    return extracted_text

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