from stream_gpt.data_scrapers.pdf_scraper import PDFScraper
import json
import pytest

@pytest.mark.skip(reason="Already tested")
def test_pdf_scraper():
    PDF_Scraper = PDFScraper()
    document = PDF_Scraper.scrape('data/raw_library/STREAM_Report.pdf', metadata={'title':'STREAM Report'})
    document.save_to_file('data/test/')