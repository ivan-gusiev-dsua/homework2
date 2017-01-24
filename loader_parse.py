# coding=utf-8

import dateparser
import datetime
import logging
import regex

log = logging.getLogger('loader')

def ukr_month(text):
	if text.startswith('с'.decode('utf-8')) and text.endswith('чня'.decode('utf-8')):
		return 01
	elif text.startswith('к'.decode('utf-8')):
		return 04
	else:
		return None

bank_format = regex.compile('^(\d+)\s+(\p{L}+)\s+(\d+)$', regex.UNICODE)
def parse_hard(text):
	match = bank_format.match(text)
	if match:
		day = int(match.group(1))
		month = ukr_month(match.group(2))
		year = int(match.group(3))

		if month:
			return datetime.datetime(year, month, day)
		else:
			return None
	else:
		return None

def parse_date(text):
	reg = parse_hard(text)
	if (reg):
		return reg
	else:
		dpp = dateparser.parse(text)
		if dpp:
			return dpp
		else:
			log.warn('Could not parse date %s', text)
			return None
