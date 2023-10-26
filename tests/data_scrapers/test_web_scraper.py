import pytest
import json
from stream_gpt.data_scrapers.web_scraper import WebScraper
from stream_gpt.constants.keys import APIFY_KEY

@pytest.mark.skip(reason="Already tested")
def test_web_scraper():
    web_scraper = WebScraper(APIFY_KEY)
    scraped_data = web_scraper.scrape('https://platform.openai.com/docs/introduction')
    for document in scraped_data:
        document.save_to_file('data/test/')