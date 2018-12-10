#!/usr/bin/env python3

# Example:
#
#     % python3 followers-graph.py 0xlynn chordbug
#     2017/04/21	224
#     2017/04/22	238
#     2017/04/27	288
#     2017/05/07	328
#     2017/05/08	329
#     ....
#
# You can paste the result into a spreadsheet program and plot it.

import requests
import sys

if len(sys.argv) <= 1:
    sys.exit('usage: %s username1 username2 username3...' % sys.argv[0])

for username in sys.argv[1:]:
    response = requests.get('http://web.archive.org/cdx/search/cdx',
        params={'url': 'https://twitter.com/%s/*' % username,
            'output': 'json', 'filter': 'mimetype:application/json'})
    for row in response.json()[1:]:
        time = row[1]
        url = row[2]
        tweet = requests.get('https://web.archive.org/web/%s/%s' % (time, url)).json()
        date = time[:4] + '/' + time[4:6] + '/' + time[6:8]
        print(date, tweet['user']['followers_count'], sep='\t')
