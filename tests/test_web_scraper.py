import pytest
import json
from stream_gpt.data_scrapers.web_scraper import selenium_scrape_site, bs4_scrape_site

def test_bs4_scraper():
    text = bs4_scrape_site('https://docs.llamaindex.ai/en/stable/')
    assert len(text) > 0
    with open('data/test/Glockkey.json', 'w') as f:
        json.dump(text, f)
        