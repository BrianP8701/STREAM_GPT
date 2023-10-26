from stream_gpt.data_scrapers.github_repo_scraper import RepoScraper
from stream_gpt.constants.keys import GITHUB_KEY
import json
import pytest

@pytest.mark.skip(reason="Already tested")
def test_github_repo_scraper():
    Repo_Scraper = RepoScraper(GITHUB_KEY)
    REPO_URL = 'https://github.com/BrianP8701/STREAM.AI'
    documents = Repo_Scraper.scrape(REPO_URL)
    for document in documents:
        document.save_to_file('data/test/')