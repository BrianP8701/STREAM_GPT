from apify_client import ApifyClient
from stream_gpt.constants.keys import APIFY_KEY
import json

def apify_website_content_crawler(url, includeUrlGlobs=[], excludeUrlGlobs=[]):
    """
    Use Apify's Website Content Crawler to scrape content from a given URL.

    This function leverages Apify's Website Content Crawler to extract content from websites. 
    It allows users to specify URLs to include or exclude from crawling and uses predefined 
    selectors to interact with and modify content during the scraping process.

    Parameters:
    - url (str): The starting URL for the web crawling process.
    - includeUrlGlobs (list, optional): List of URL glob patterns to be exclusively included in the crawl.
    - excludeUrlGlobs (list, optional): List of URL glob patterns to be excluded from the crawl.

    Returns:
    - list: A list of dataset items collected during the crawl.

    Note:
    - This function requires the APIFY_KEY to be set and valid.
    - For more details on Apify's Website Content Crawler, visit: https://apify.com/apify/website-content-crawler

    Example:
    >>> result = apify_website_content_crawler("https://example.com", ["https://example.com/blog/*"], ["https://example.com/private/*"])
    >>> print(result)
    """
    # Initialize the ApifyClient with your API token
    client = ApifyClient(APIFY_KEY)

    # Prepare the Actor input
    run_input = {
        "startUrls": [{ "url": url}],
        "includeUrlGlobs": includeUrlGlobs,
        "excludeUrlGlobs": excludeUrlGlobs,
        "initialCookies": [],
        "proxyConfiguration": { "useApifyProxy": True },
        "removeElementsCssSelector": """nav, footer, script, style, noscript, svg,
    [role=\"alert\"],
    [role=\"banner\"],
    [role=\"dialog\"],
    [role=\"alertdialog\"],
    [role=\"region\"][aria-label*=\"skip\" i],
    [aria-modal=\"true\"]""",
        "clickElementsCssSelector": "[aria-expanded=\"false\"]",
    }

    # Run the Actor and wait for it to finish
    run = client.actor("apify/website-content-crawler").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)

    dataset_items = client.dataset(run['defaultDatasetId']).list_items().items
    return dataset_items