from stream_gpt.data_scrapers.pdf_scrapers import pdfminer_scraper, pdfplumber_scraper, pypdf2_scraper, pytesseract_scraper
import json

def test_pdfminer_scraper():
    text = pdfminer_scraper('data/raw_library/STREAM_Report.pdf')
    assert len(text) > 0
    with open('data/raw_library/STREAM_Report.json', 'w') as f:
        json.dump(text, f)

