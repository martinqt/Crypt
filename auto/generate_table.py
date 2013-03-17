# -*-coding:Utf-8 -*

from lib import *
from itertools import product

content = read('text.txt')

content = unicode(content, 'utf-8')
groups = list(product(''.join(getCharList(content)), repeat=2))

analysis = doGroupsAnalysis(content.lower(), groups)
writePickled('table.py', analysis)
print(analysis)
