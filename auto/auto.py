# -*-coding:Utf-8 -*

from itertools import product
from lib import *

###### The script
table = readPickled('table.py')
content = read('input.txt')
content = 'le el'
key = dict()
groups = list(product(''.join(getCharList(content)), repeat=2))
failRow = score = 0
#left is the coded side
left = right = list()

#for group in groups:
#    left.append(''.join(group))
#    right.append(''.join(group))

left = ['le', 'el']
right = ['el', 'le']

while failRow < 1000:
    key = buildKey(left, right)
    print(transform(content, key))
    failRow = 1001
