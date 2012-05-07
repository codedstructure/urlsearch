#!/usr/bin/env python

# Search query from command line; open browser as appropriate
# Ben Bass 2012 @codedstructure

import os
import sys
import urllib
import webbrowser
import socket

# allow multiple symlinks, use their name as site
site = os.path.basename(sys.argv[0])

# Defaults
query_path = 'search?q={terms}'
quote_fn = urllib.quote_plus

# special cases, aliases etc
if site == 'wiki':
    site = 'wikipedia.org'
    query_path = 'w/index.php?search={terms}'
elif site == 'pylib':
    site = 'docs.python.org'
    query_path = 'library/{terms}'
elif site == 'jquery':
    site = 'api.jquery.com'
    query_path = '{terms}/'
elif site == 'duckduckgo':
    query_path = '{terms}'
    quote_fn = urllib.quote

# support for local domains, gTLD searching etc
if '.' not in site:
    for suffix in '', '.com', '.org', '.net', '.co.uk':
        try:
            if socket.getaddrinfo(site + suffix, 'http'):
                site = site + suffix
                break
        except socket.gaierror:
            pass

# Following is for searching trac instances
# '#123' should go to ticket 123
terms = ' '.join(sys.argv[1:])
try:
    int(terms)
except ValueError:
    pass
else:
    # a lone number refers to a ticket. Can't use #1234,
    # as is interpreted as a comment by bash and doesn't
    # get here
    terms = '#' + terms

terms = quote_fn(terms)
query = query_path.format(terms=terms)

# suppress stdout from subprocess created by webbrowser.open
# (e.g. 'Created new window in existing browser session.')
os.dup2(os.open(os.devnull, os.O_WRONLY), 1)
# start a browser window for the search
webbrowser.open('http://{site}/{query}'.format(site=site, query=query))
