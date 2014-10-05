#!/usr/bin/env python

# Search query from command line; open browser as appropriate
# Ben Bass 2012-2014 @codedstructure


__version__ = '0.2'

import os
import sys
# support Python2 and Python3
try:
    from urllib.parse import quote, quote_plus
except ImportError:
    from urllib import quote, quote_plus
import webbrowser
import socket


class UrlSearcher(object):

    def __init__(self, site, search):
        self.site = site
        self.search = search
        # Defaults
        self.query_path = 'search?q={terms}'
        self.quote_fn = quote_plus

    def open(self):
        query = self.process()

        # suppress stdout from subprocess created by webbrowser.open
        # (e.g. 'Created new window in existing browser session.')
        os.dup2(os.open(os.devnull, os.O_WRONLY), 1)
        # start a browser window for the search
        webbrowser.open('http://{site}/{query}'.format(site=self.site,
                                                       query=query))

    def process(self):
        # Following is for searching trac instances
        # '#123' should go to ticket 123
        try:
            int(self.search)
        except ValueError:
            pass
        else:
            # a lone number refers to a ticket. Can't use #1234,
            # as is interpreted as a comment by the shell and doesn't
            # get here
            self.search = '#' + self.search

        # special cases, aliases etc
        if self.site == 'wiki':
            self.site = 'wikipedia.org'
            self.query_path = 'w/index.php?search={terms}'
        elif self.site == 'pylib':
            self.site = 'docs.python.org'
            self.query_path = 'library/{terms}'
        elif self.site == 'pypi':
            self.site = 'pypi.python.org'
            self.query_path = 'pypi?:action=search&term={terms}&submit=search'
        elif self.site == 'jquery':
            self.site = 'api.jquery.com'
            self.query_path = '{terms}/'
        elif self.site in('duckduckgo', 'ddg'):
            self.site = 'duckduckgo'
            self.query_path = '{terms}'
            self.quote_fn = quote

        # support for local domains, gTLD searching etc
        if '.' not in self.site:
            for suffix in '', '.com', '.org', '.net', '.co.uk':
                try:
                    if socket.getaddrinfo(self.site + suffix, 'http'):
                        self.site = self.site + suffix
                        break
                except socket.gaierror:
                    pass

        terms = self.quote_fn(self.search)
        query = self.query_path.format(terms=terms)

        return query


def main():
    # allow multiple symlinks, use their name as site
    site = os.path.basename(sys.argv[0])
    search = ' '.join(sys.argv[1:])

    # blacklist 'urlsearch'
    if (os.path.basename(sys.argv[0]) ==
            os.path.splitext(os.path.basename(__file__))[0]):
        raise SystemExit("Should be used via named symlinks")

    urlsearch = UrlSearcher(site, search)
    urlsearch.open()
