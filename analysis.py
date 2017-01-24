# coding: utf-8
import pandas as pd
import sys

if len(sys.argv) < 2:
	print 'usage: python analysis.py <filename>'
	sys.exit(1)

doc = pd.read_csv(sys.argv[1], sep='|', index_col=0, names=['date', 'link', 'text'], parse_dates=[0])
doc.groupby(pd.TimeGrouper(freq="M"))
group = doc.groupby(pd.TimeGrouper(freq="M"))
plt = group.count()["link"].plot()
plt.get_figure().savefig('my.png')
