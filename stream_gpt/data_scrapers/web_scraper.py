import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from stream_gpt.constants.local_paths import CHROME_DRIVER

def selenium_scrape_site(base_url):
    driver = webdriver.Chrome(CHROME_DRIVER)  # Adjust path if necessary
    visited_links = set()
    extracted_text = {}
    
    def scrape_page(url):
        if url in visited_links:
            return
        visited_links.add(url)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        extracted_text[url] = soup.text
        for a_tag in soup.find_all('a', href=True):
            next_url = urljoin(base_url, a_tag['href'])
            scrape_page(next_url)
    
    scrape_page(base_url)
    driver.quit()  # Don't forget to close the browser
    return extracted_text

# TODO: {"https://platform.openai.com/docs/introduction": "OpenAI PlatformYou need to enable JavaScript to run this app."}

def bs4_scrape_site(base_url):
    visited_links = set()
    extracted_text = {}
    
    def scrape_page(url):
        print(url)
        if url in visited_links:
            return
        visited_links.add(url)
        response = requests.get(url)
        if response.status_code != 200:
            print(f'Failed to retrieve {url}')
            return
        soup = BeautifulSoup(response.text, 'html.parser')
        extracted_text[url] = soup.text
        # Finding all the anchor tags in the page
        for a_tag in soup.find_all('a', href=True):
            # Joining relative URLs with the base URL
            next_url = urljoin(base_url, a_tag['href'])
            # Recursively scrape the linked page
            scrape_page(next_url)
    
    scrape_page(base_url)
    return extracted_text

