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
search engine;

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

Copy **urlsearch** to ~/bin, ensure it is executable. Create symlinks as
appropriate to it in the same place, for example:

::

    $ pwd
    /home/users/ben/bin
    $ ln -s urlsearch google
    $ ln -s urlsearch wiki
    $ ln -s urlsearch trac

*Ben Bass 2012 @codedstructure*
