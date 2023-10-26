from abc import ABC, abstractmethod

class Scraper(ABC):
    def scrape():
        pass
    
    @abstractmethod
    def convert_scraped_data_to_documents():
        '''
        The fudamental unit of data used in STREAM-GPT is the Document.
        '''
        pass