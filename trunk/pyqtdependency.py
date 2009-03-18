#!/usr/bin python

'''qtdependency.py a script to grab all Qt classes from a .py script
and see from which Qt module should those classes be imported'''

__author__ = 'Robert Basic contactme@robertbasic.com'
__version__ = '0.0.1'
__license__ = 'MIT http://www.opensource.org/licenses/mit-license.php'

import sys
import os
import re
import urllib2
import string

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Bah! I need a file to process!"
        sys.exit()
    modules = {}
    classes = []
    '''patt finds from rows like:
        class Spam(QWidget):
        qidget = QWidget()
        action = QAction(QIcon(...))'''
    patt = re.compile('.*(Q[A-Z]{1}[a-zA-Z]+)[(.*]')
    '''On row 15 there's only 1 anchor tag with the module name in it'''
    patt2 = re.compile('(Q[a-zA-Z]+)</a>')
    file = sys.argv[1]
    fp = open(file, 'rb')
    lines = fp.readlines()
    fp.close()

    for line in lines:
        match = patt.search(line)
        if match is not None:
            match = match.group(1)
            if match not in classes:
                classes.append(match)
    
    for cl in classes:
        url = 'http://doc.trolltech.com/4.4/%s.html' % string.lower(cl)
        resp = urllib2.urlopen(url)
        '''The module name is in row 15, go there'''
        for i in range(0,15):
            if i < 14:
                resp.next()
            elif i == 14:
                match = patt2.search(resp.readline())
                match = match.group(1)
            else:
                break

        if match in modules:
            modules[match].append(cl)
        else:
            modules[match] = [cl]

    print modules
