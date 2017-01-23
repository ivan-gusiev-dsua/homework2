# coding=utf-8

import dateparser
import datetime
import logging
import regex

log = logging.getLogger('loader')

def ukr_month(text):
	if text.startswith('с'.decode('utf-8')):
		return 01
	elif text.startswith('к'.decode('utf-8')):
		return 04
	else:
		print text
		return None

bank_format = regex.compile('^(\d+)\s+(\p{L}+)\s+(\d+)$', regex.UNICODE)
def parse_hard(text):
	log.warn('Parsing hard: [%s]', text)
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
	simple = dateparser.parse(text)
	if (simple):
		return simple
	else:
		return parse_hard(text)
