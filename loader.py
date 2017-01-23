# coding=utf-8

import bs4
import dateparser
import logging
import requests

import loader_cache
import loader_parse

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

MAX_PAGES = 100
log.info('Max pages set to %s', MAX_PAGES)

bank_host = 'https://bank.gov.ua/'
bank_root = bank_host + 'control/uk/publish/category?cat_id=70779'
log.info('Root URL: %s', bank_root)

def get_soup(url):
	if url.startswith('control'): url = bank_host + url
	data = loader_cache.get_text(url)
	soup = bs4.BeautifulSoup(data, 'html5lib')
	return soup

def process_announcement(ann):
	ann_date = ann.find('div', { 'class' : 'announce_date' })
	ann_link = ann.find('a')
	date = loader_parse.parse_date(ann_date.text.strip())
	log.debug('[%s] -> %s', ann_date.text.strip(), date)
	link = ann_link['href']
	text = ann_link.text.strip()

def process_page(url):
	soup = get_soup(url)
	announcements = soup.findAll('td', { 'class' : 'padd_ann' })
	log.debug('Found %s announcements on URL %s', len(announcements), url)

	for ann in announcements:
		process_announcement(ann)

	return True if (len(announcements) > 0) else False

def process_year(url):
	process_page(url)
	for i in range(1, MAX_PAGES):
		page_url = url + '&page=' + str(i)
		if (not process_page(page_url)): break

root_soup = get_soup(bank_root)
announce_div = root_soup.findAll('div', { 'class' : 'announces_block' })[0]

years = set()
for link in announce_div.findAll('a'):
	years.add(link['href'])
log.debug('Found %s year links', len(years))

process_year(list(years)[0])
