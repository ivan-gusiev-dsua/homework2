import datetime
import logging
import os
import time


log = logging.getLogger('loader')
root_dir = './data'
now = datetime.datetime.utcnow()
datafile = root_dir + '/' + now.strftime('%Y%m%d%H%M') + '_data.csv'

def ensure_dir(dir):
	if not os.path.exists(dir):
		log.warn('Directory %s does not exist, creating', dir)
		os.makedirs(dir)

def data_append(text):
	ensure_dir(root_dir)
	with open(datafile, "a") as text_file:
		text_file.write(text.encode('utf-8'))

def news_append(date, link, text):
	data_append(str(date) + '|' + link + '|' + text + '\n')
