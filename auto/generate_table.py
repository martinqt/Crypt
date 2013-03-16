# -*-coding:Utf-8 -*

from lib import *
from itertools import product

content = read('text.txt')
groups = list(product(''.join(getCharList(content)), repeat=2))

analysis = doGroupsAnalysis(content, groups)
writePickled('table.py', analysis)
print(analysis)
