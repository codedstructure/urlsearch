# The content of URLSEARCHRC_CONFIG will be written to ~/.urlsearchrc.default
# if neither that file nor ~/.urlsearchrc exist when urlsearch is run

URLSEARCHRC_CONFIG = """[DEFAULT]
# Default options can be specified here.
#
# quote_plus quotes search terms as 'this+is+a+search'
#quote_plus = on
#
# hash_prefix_numbers precedes wholly numeric searches with a '#' character,
# intended for searches for tickets in tools such as Trac
#hash_prefix_numbers = off
#
# tlds is a space (and/or comma) separated list of TLDs to search (in order)
# when identifying the site to open. Note this is only used if no '.' appears
# within the site itself.
#tlds = .com .org .net .co.uk

# Site specific options should be given in a section where the section
# name is the entry point for urlsearch, i.e. the argv[0] value.
# As well as overriding the default options above, the 'site' and 'query'
# values can be specified.

# urlsearch matches the search format used by google and bind, so they don't
# appear in this config file, but google could appear as follows:
#[google]
#site = google.com
#query = search?q={terms}
#quote_plus = on
#hash_prefix_numbers = off

# Sets of options can be shared by creating a section with a single 'alias'
# option pointing to another section title.

[wiki]
site = wikipedia.org
query = w/index.php?search={terms}

[pylib]
site = docs.python.org
query = library/{terms}

[pypi]
site = pypi.python.org
query = pypi?:action=search&term={terms}&submit=search

[jquery]
site = api.jquery.com
query = {terms}

[ddg]
site = duckduckgo
query = {terms}
quote_plus = off

[duckduckgo]
alias = ddg
"""
