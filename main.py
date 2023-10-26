from stream_gpt.data_scrapers.global_scraper import GlobalScraper
from stream_gpt.constants.keys import APIFY_KEY, GITHUB_KEY
from stream_gpt.data_scrapers.web_scraper import WebScraper
import json
# global_scraper = GlobalScraper(apify_key=APIFY_KEY, github_key=GITHUB_KEY)
# documents = global_scraper.scrape('repo', 'https://github.com/BrianP8701/STREAM_GPT')

# for document in documents:
#     document.save_to_file('data/library/scraped_github_repos/stream_gpt/')

web_scraper = WebScraper(apify_key=APIFY_KEY)
with open('data/library/scraped_websites/openaidocs.json', 'r') as f:
    dataset_items = json.load(f)

documents = web_scraper.convert_scraped_data_to_documents(dataset_items)

for document in documents:
    document.save_to_file('data/library/scraped_websites/openai_docs/')