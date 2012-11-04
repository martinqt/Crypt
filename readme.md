Crypt
=====

This is a small helper for decryption project. It's also my first python script so any comment on the
way of using it is welcome.

This has been tested with the 3.3 version of python on a windows 7 laptop.

This is currently not intended to decrypt multiple messages but only the one in the input file. In the future it 
might also crypt messages.

Installing
----------

Go to http://www.python.org/download/ and get, at least, the 3.0 version. 

If you want to use the graphic interface, you'll also need to install PySide. Go to http://qt-project.org/wiki/PySideDownloads, 
select your OS and then the PySide version corresponding to your Python version. The version is at the end of the filename, for 
instance ``-py3.2`` or ``-py3.3``.

CLI Mode
--------

To use it, simply run ``watcher.bat`` to run the watcher. If you have an error telling you that python is not defined, 
you'll need to edit the ``watcher.bat`` file and replace ``python`` by the complete path to python the binary, for instance
``C:\Python33\python``. If you are not under windows, open a prompt, go to the project root dir and type ``python src/watcher.py``.

Any change in one of the ``*.py`` file or to the input file will trigger the generation.

The characters statistics provide a count result by default, wich means it will print the number of time the characters were 
encountred. If you want the frequency to be outputed in place of a simple count, just add ``--frequency`` after your call to 
the watcher or ``src/script.py`` file.

You can't pass the ``--frequency`` option if you're double-cliking the bat file. You'll have to either edit this file and add the 
parameter at the end of the line or call the bat file from the command line with the parameter.

All the results are published under the ``output`` dir.

GUI Mode
--------

To use the graphical interface, simply run the ``crypt.bat`` file on Windows or type ``python src/mainWindow.py`` in 
a command prompt.
