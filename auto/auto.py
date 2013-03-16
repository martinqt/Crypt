# -*-coding:Utf-8 -*

from itertools import product
from lib import *
import sys

###### The script
table = readPickled('table.py')
content = read('input.txt')
try:
    arg = sys.argv[1]
except IndexError:
    arg = ''
if arg == '--continue':
    print('Restoring previous session...')
    sys.stdout.flush()
    key = readPickled('key.py')
else:
    print('Starting new session')
    sys.stdout.flush()
    key = dict()
groups = list(product(''.join(getCharList(content)), repeat=2))
failRow = printcounter = 0
score = pscore = 1
#left is the coded side
pright = left = right = list()

#groups = ['1a', 'bc', 'de', 'fg']

for group in groups:
    left.append(''.join(group))

right = list(left)
pright = list(right)
alpha = 0

print('Here we go!!!')
sys.stdout.flush()

while failRow < 1000:
    #print(right)
    right = randomSwap(right)
    #print(right)
    key = buildKey(left, right)
    #print(key)
    text = transform(content, key)
    score = evaluate(text, table)

    if score > pscore:
        #print('better')
        pscore = score
        pright = list(right)
        failRow = 0
        alpha += 1
    else:
        #print('worst')
        right = list(pright)
        failRow += 1

    if (printcounter == 200):
        key = buildKey(left, right)
        writePickled('key.py', key)
        print('Not dead... yet anyway^^ ('+str(failRow)+'/1000)')
        sys.stdout.flush()
        printcounter = 0
    printcounter += 1

print('Compleeeeeeeeeeeeeeeted (at last :)')
sys.stdout.flush()

print(alpha)
key = buildKey(left, right)
writePickled('key.py', key)
print(transform(content, key))

print('And saved (hopefully ;)')