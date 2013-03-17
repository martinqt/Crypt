# -*-coding:Utf-8 -*

from itertools import product
from lib import *
import sys, itertools

###### The script
table = readPickled('table.py')
content = read('input.txt')
groups = list(product(''.join(getCharList(content)), repeat=2))
failRow = printcounter = 0
score = pscore = evaluate(content, table)
#left is the coded side
pright = left = right = list()
#left = getCharList(content)
left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',',\
    '.', '\'', '?', '!', ' ']

#groups = ['1a', 'bc', 'de', 'fg']

#for group in groups:
#    left.append(''.join(group))

right = list(left)
pright = list(right)
same = best = worth = 0

try:
    cont = sys.argv[1]
except IndexError:
    cont = ''
if cont == '--continue':
    print('Restoring previous session...')
    sys.stdout.flush()
    right = readPickled('right.py')
else:
    print('Starting new session')
    sys.stdout.flush()
    key = dict()

print('Here we go!!!')
sys.stdout.flush()

failTarget = 1000

#Main loop

while failRow < failTarget:
    right = randomSwap(right)
    key = buildKey(left, right)
    text = transform(content, key)
    score = evaluate(text, table)

    if score == pscore:
        same += 1
    elif score > pscore:
        pscore = score
        pright = list(right)
        failRow = 0
        best += 1
    else:
        right = list(pright)
        failRow += 1
        worth += 1

    if (printcounter == 200):
        writePickled('right.py', list(right))
        print('Not dead... yet anyway ^^ ('+str(failRow)+'/'+str(failTarget)+')')
        sys.stdout.flush()
        printcounter = 0
    printcounter += 1
#Post process
print('Compleeeeeeeeeeeeeeeted (at last :)')
sys.stdout.flush()

print('Same: '+str(same)+'\nBest: '+str(best)+'\nWorth: '+str(worth))
writePickled('right.py', right)
key = buildKey(left, right)
tmp = transform(content, key)
write('output.txt', tmp)
score = evaluate(tmp, table)
write('score.txt', str(score))
print('\n'+tmp)
print('\n \nAnd saved (hopefully ;)')
print('Ps: Never said I found the answer ;)\n')

print(buildKey(left, right))
