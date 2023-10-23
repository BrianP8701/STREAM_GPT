from stream_gpt.data_scrapers.pdf_scraper import pdfminer_scraper, pdf_to_text, pdfplumber_scraper, pypdf2_scraper, pytesseract_scraper
import json
import pytest

@pytest.mark.skip(reason="Already tested")
def test_pdfminer_scraper():
    text = pdfminer_scraper('data/raw_library/STREAM_Report.pdf')
    assert len(text) > 0
    with open('data/raw_library/STREAM_Report.json', 'w') as f:
        json.dump(text, f)

@pytest.mark.skip(reason="Already tested")
def test_pdf_to_text():
    text = pdf_to_text('data/raw_library/STREAM_Report.pdf')