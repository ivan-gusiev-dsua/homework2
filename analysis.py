# coding: utf-8
import os
import pandas as pd
import sys

if len(sys.argv) < 2:
	print 'usage: python analysis.py <filename>'
	sys.exit(1)

# prepare
root_dir = './results'

def ensure_dir(dir):
	if not os.path.exists(dir):
		print 'Directory {0} does not exist, creating'.format(dir)
		os.makedirs(dir)

def get_path(filename):
	return root_dir + '/' + filename

ensure_dir(root_dir)


# read file
doc = pd.read_csv(sys.argv[1], sep='|', index_col=0, names=['date', 'link', 'text'], parse_dates=[0])

# group by month
group = doc.groupby(pd.TimeGrouper(freq='M'))

# plot
plt = group.count()['link'].plot()
plt.get_figure().savefig(get_path('result.png'))

# calculate
group_counts = group.agg({'link':'count'})
delta = group_counts.index.max() - group_counts.index.min()
total = float(group_counts['link'].sum())
frequency = total / delta.days

# save
with open(get_path('result.txt'), 'w') as f:
	f.write('Published {0} news in {1} days, resulting in {2} articles per day ({3} per week)'.format(total, delta.days, frequency, frequency * 7))


