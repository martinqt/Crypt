from functions import *
from itertools import product
from key import *
import os, sys
sys.path.insert(0, os.getcwd()+'/src/functions')
from file import *

frequency = False

for arg in sys.argv:
	if arg == '--frequency':
		frequency = True

#the encrypted message
input = read('input.txt')
#the chars in the message
charList = getCharList(input)
#list of the possible groups
groups = product(''.join(charList), repeat=2)
#get the key
replaceDict = getKey()

#generate and write groups analysis
doGroupsAnalysis(input, groups, frequency)

#replacing chars using the key
result = transform(input, replaceDict)

#generate html output
htmlResult = input+'<hr/>'
htmlResult += transform(input, htmlFormatDict(replaceDict))

#print output in the console
print(result)

#write output
write('output.txt', result)
write('output.html', htmlResult)
writeCharCount(input, frequency)
