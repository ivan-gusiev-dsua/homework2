import base64
import logging
import os
import requests
import time


log = logging.getLogger('loader')
root_dir = './cache'

def get_filename(url):
	return base64.b64encode(url)

def get_path(filename):
	return root_dir + '/' + filename

def ensure_dir(dir):
	if not os.path.exists(dir):
		log.warn('Directory %s does not exist, creating', dir)
		os.makedirs(dir)

def exists_file(filename):
	return os.path.exists(get_path(filename))

def download_text(url):
	log.debug('Downloading %s', url)
	time.sleep(1)
	req = loader_cache.get_text(url)
        data = req.text

def read_file(filename):
	with open(get_path(filename), 'r') as text_file:
		return text_file.read()

def save_file(filename, text):
	 with open(get_path(filename), "w") as text_file:
		text_file.write(text)

def get_text(url):
	ensure_dir(root_dir)
	filename = get_filename(url)
	if exists_file(filename):
		return read_file(filename)
	else:
		text = download_text(url)
		save_file(filename, text)
		return text

