Pass a .py script to pyqtdependency.py and it will return a list of used Qt classes and from which Qt module should those classes be imported from.

Opens the .py script and looks for classes like QWidget(), QAction(), etc. and reads from the official Qt docs (http://docs.trolltech.com/4.4/) the Qt module from which each class should be imported.

Usage:
```
./pyqtdependency.py /path/to/foo.py
```