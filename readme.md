Crypt
=====

This is a small helper for decryption project. It's also my first python script so any comment on the
way of using python is welcome.

Installing
----------

Go to http://www.python.org/download/ and get, at least, the 3.0 version.

Using it
--------

To use it, simply run ``watcher.bat`` to run the watcher. If you have not installed python 
to the default location, you'll need to edit the ``watcher.bat`` file and replace ``C:\Python33\python``
by tour python install dir. Any change in one of the ``*.py`` file will trigger the generation.

This has been tested with the 3.3 version of python on a windows 7 laptop.

This is currently not intended to decrypt multiple messages but only the one in the input file. In the future it 
might also crypt messages.
