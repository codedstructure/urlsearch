=========
urlsearch
=========

Usage
-----

::

    Usage: URLSEARCH_NAME query
      opens appropriate search query in a browser

urlsearch provides a shortcut to start a web search from the command line.
It is designed to be symlinked from command names which refer to the target
search engine; several are already included by default:

* ``google``
* ``bing``
* ``ddg`` (DuckDuckGo)
* ``pylib`` (search Python library reference)
* ``pypi`` (search the Python Package Index)
* ``wiki`` (search Wikipedia)

Features:

* simple special casing of query path and naming (see 'wiki' as an example)
* supports trac ticket searches (e.g. #1234) by omitting the leading '#', which would otherwise be interpreted as a comment by the shell and dropped.
* supports local domains - if name can be resolved locally it will be used in preference to appending a suffix

Examples
--------

*These assume 'google', 'wiki', and 'trac' are urlsearch commands*::

    $ google photon mapping
    $ trac r19201
    $ wiki path tracing


Default installation
--------------------

Note the default installation adds a number of new commands to your ``PATH``, as
listed in the **Usage** overview above.

::

    $ pip install urlsearch
    $ google python webbrowser  # open web page

Manual installation
-------------------

Cloning the repository locally and editing the content of `scripts` by deleting
or creating symlinks is recommended to get a more custom set of search links.

::

    ~$ hg clone https://bitbucket.org/codedstructure/urlsearch
    ~$ cd urlsearch/scripts
    scripts$ rm google
    scripts$ ln -s urlsearch trac
    scripts$ cd ..
    urlsearch$ python3 setup.py install

CHANGES
-------

0.2:
    * change to use setuptools
    * add pypi search

0.1:
    * first release

TODO
----

Improved support for manually adding search types including simple special
casing is planned.

*Ben Bass 2012-2014 @codedstructure*
