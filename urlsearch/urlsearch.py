#!/usr/bin/env python

# Search query from command line; open browser as appropriate
# Ben Bass 2012-2014 @codedstructure


__version__ = '0.3'

import os
import sys
import webbrowser
import socket
# support Python2 and Python3
try:
    from urllib.parse import quote, quote_plus
except ImportError:
    from urllib import quote, quote_plus

try:
    from configparser import RawConfigParser
except ImportError:
    from ConfigParser import RawConfigParser


class UrlSearcher(object):
    def __init__(self, site, search, configfile=None):
        self.site = site
        self.search = search
        # Defaults - these (plus 'site') can be overridden by config file
        self.query_path = 'search?q={terms}'
        self.tld_list = ['.com', '.org', '.net', '.co.uk']
        self.quote_fn = quote_plus
        self.hash_num = False

        if configfile is None:
            configfile = self.get_config_file()

        self.read_config(configfile)

    def get_config_file(self):
        return ['.urlsearchrc', os.path.expanduser('~/.urlsearchrc')]

    def read_config(self, configpath):
        parser = RawConfigParser({
            'query': self.query_path,
            'quote_plus': 'on' if self.quote_fn is quote_plus else 'off',
            'site': self.site,
            'tlds': ' '.join(self.tld_list),
            'hash_prefix_numbers': 'on' if self.hash_num else 'off'})
        parser.read(configpath)

        section = self.site
        if parser.has_section(section):
            # we allow a single level of indirection to support limited
            # aliases. Inheritance is not currently supported
            if parser.has_option(section, 'alias'):
                self.site = parser.get(section, 'alias')
                return self.read_config(configpath)

            self.query_path = parser.get(section, 'query')
            self.quote_fn = (quote_plus
                             if parser.getboolean(section, 'quote_plus')
                             else quote)
            tlds = parser.get(section, 'tlds')
            self.tld_list = tlds.replace(',', ' ').split()
            self.hash_num = parser.getboolean(section, 'hash_prefix_numbers')
            self.site = parser.get(section, 'site')

    def open(self):
        query = self.process()

        # suppress stdout from subprocess created by webbrowser.open
        # (e.g. 'Created new window in existing browser session.')
        os.dup2(os.open(os.devnull, os.O_WRONLY), 1)
        # start a browser window for the search
        webbrowser.open('http://{site}/{query}'.format(site=self.site,
                                                       query=query))

    def process(self):
        if self.hash_num:
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

        # support for local domains, gTLD searching etc
        if '.' not in self.site:
            for suffix in [''] + self.tld_list:
                try:
                    if socket.getaddrinfo(self.site + suffix, 'http'):
                        self.site += suffix
                        break
                except (socket.gaierror, socket.error):
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
