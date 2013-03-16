# -*-coding:Utf-8 -*

from itertools import product
from lib import *

###### The script
table = readPickled('table.py')
content = read('input.txt')
key = dict()
groups = list(product(''.join(getCharList(content)), repeat=2))
failRow = 0
score = pscore = 1
#left is the coded side
pright = left = right = list()

for group in groups:
    left.append(''.join(group))
    right.append(''.join(group))

pright = right

while failRow < 1000:
    key = buildKey(left, right)
    text = transform(content, key)
    score = evaluate(text, table)

    if score > pscore:
        pscore = score
        pright = right
        pass
    else:
        right = pright
        failRow += 500
        pass
    print(score)
