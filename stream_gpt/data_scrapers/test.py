import pdf_scrapers as ps
import json

text = ps.pypdf2_scraper("raw_library/Distributed_Systems_Tanenbaum.pdf")

with open('blanky.json', 'w') as f:
    json.dump(text, f)