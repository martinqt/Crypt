Crypt
=====

This is a small helper for decryption project. It's also my first python script so any comment on the
way of using it is welcome.

Installing
----------

Go to http://www.python.org/download/ and get, at least, the 3.0 version.

Using it
--------

To use it, simply run ``watcher.bat`` to run the watcher. If you have an error telling you that python is not defined, 
you'll need to edit the ``watcher.bat`` file and replace ``python`` by the complete path to python the binary, for instance
``C:\Python33\python``.

Any change in one of the ``*.py`` file will trigger the generation.

This has been tested with the 3.3 version of python on a windows 7 laptop.

This is currently not intended to decrypt multiple messages but only the one in the input file. In the future it 
might also crypt messages.
