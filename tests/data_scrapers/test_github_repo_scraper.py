from stream_gpt.data_scrapers.github_repo_scraper import fetch_github_repo_content
from stream_gpt.constants.keys import GITHUB_KEY
import json
import pytest

@pytest.mark.skip(reason="Already tested")
def test_github_repo_scraper():
    REPO_URL = 'https://github.com/BrianP8701/STREAM_GPT'
    content_dict = fetch_github_repo_content(REPO_URL, GITHUB_KEY)
    
    with open('stream_gpt_repo.json', 'w') as f:
        json.dump(content_dict, f, indent=4) 