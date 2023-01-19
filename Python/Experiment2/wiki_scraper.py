from gpt_index import SimpleWebPageReader, GPTSimpleVectorIndex
from dotenv import load_dotenv
from sitemap_parser import *
import re

load_dotenv()

scrapeUrl = 'https://www.defichainwiki.com/'
indexFileTarget = './indices/index_vector.json'

urls = getUrlsToScrape(scrapeUrl)


print('🔭 Scrape %s found pages..' % len(urls))
documents = SimpleWebPageReader(html_to_text=True).load_data(urls)
print('✅ Scraped %s pages' % len(documents))


print('Remove long strings')
for document in documents:
    document.text = re.sub(
        r'(?<=\S)[^\s]{' + str(3714) + ',}(?=\S)', '', document.text)

print('Get list index via GPT API..')
index = GPTSimpleVectorIndex(documents)

print('💾 Saving index to:', indexFileTarget)
index.save_to_disk(indexFileTarget)
