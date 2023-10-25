import pytest
import json
from stream_gpt.data_scrapers.web_scraper import apify_website_content_crawler
from stream_gpt.constants.keys import APIFY_KEY

@pytest.mark.skip(reason="Already tested")
def test_web_scraper():
    scraped_data = apify_website_content_crawler('https://docs.llamaindex.ai/en/stable/', APIFY_KEY)
    with open('llama_index_docs', 'w') as f:
        json.dump(scraped_data, f, indent=4) 