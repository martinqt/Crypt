# -*-coding:Utf-8 -*

from src.functions import *
from itertools import product
from src.key import *
import os, sys

outputFormat = ''

for arg in sys.argv:
    if arg == '--frequency':
        outputFormat = 'frequency'
    if arg == '--percent':
        outputFormat = 'percent'

#the encrypted message
input = read('input.txt')
#the chars in the message
charList = getCharList(input)
#list of the possible groups
groups = product(''.join(charList), repeat=2)
#get the key
replaceDict = getKey()

#generate and write groups analysis
doGroupsAnalysis(input, groups, outputFormat)

#replacing chars using the key
result = transform(input, replaceDict)

#generate html output
htmlResult = input+'<hr/>'
htmlResult += transform(input, htmlFormatDict(replaceDict))

#print output in the console
print(result)

#write output
write('output/output.txt', result)
write('output/output.html', htmlResult)
writeCharCount(input, outputFormat)
