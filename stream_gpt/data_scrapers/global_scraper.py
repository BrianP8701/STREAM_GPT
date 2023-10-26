from stream_gpt.interfaces.scraper_interface import Scraper
from stream_gpt.data_scrapers.pdf_scraper import PDFScraper
from stream_gpt.data_scrapers.web_scraper import WebScraper
from stream_gpt.data_scrapers.github_repo_scraper import RepoScraper
from stream_gpt.types.document import Document
from typing import List

class GlobalScraper(Scraper):
    '''
    Consolidating all scrapers into one class for easier usage.
    
    # Usage example:
        global_scraper = GlobalScraper(apify_key='your_apify_key', github_key='your_github_key')
        pdf_document = global_scraper.scrape('pdf', path='path_to_pdf', metadata={'title': 'some_title'})
        web_data = global_scraper.scrape('web', url='http://example.com', includeUrlGlobs=['*example.com/*'])
        repo_data = global_scraper.scrape('repo', repo_url='https://github.com/username/repo')
    '''
    def __init__(self, apify_key, github_key):
        self.pdf_scraper = PDFScraper()
        self.web_scraper = WebScraper(apify_key)
        self.repo_scraper = RepoScraper(github_key)

    def scrape(self, scraper_type, *args, **kwargs) -> List[Document]:
        if scraper_type == 'pdf':
            return self.pdf_scraper.scrape(*args, **kwargs)
        elif scraper_type == 'web':
            return self.web_scraper.scrape(*args, **kwargs)
        elif scraper_type == 'repo':
            return self.repo_scraper.scrape(*args, **kwargs)
        else:
            raise ValueError(f"Unknown scraper type: {scraper_type}")
        
    def convert_scraped_data_to_documents():
        pass