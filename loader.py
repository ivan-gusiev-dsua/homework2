import bs4
import logging
import requests

import loader_cache

# set up logging
FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
logging.basicConfig(format=FORMAT,filename='loader.log')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(FORMAT)
ch.setFormatter(formatter)
log = logging.getLogger('loader')
log.addHandler(ch)
log.setLevel(logging.DEBUG)

log.info('Starting scraper.')

bank_root = 'https://bank.gov.ua/control/uk/publish/category?cat_id=70779'
log.info('root URL: %s', bank_root)

def get_soup(url):
	req = loader_cache.get_text(url)
	data = req.text
	soup = bs4.BeautifulSoup(data, 'html5lib')
	return soup

root_soup = get_soup(bank_root)
announce_div = root_soup.findAll("div", { "class" : "announces_block" })
log.info(len(announce_div))

