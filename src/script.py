from functions import *
from itertools import product
from key import *

#the encrypted message
input = read('input.txt')
#the chars in the message
charList = getCharList(input)
#list of the possible groups
groups = product(''.join(charList), repeat=2)

#get the key
replaceDict = getKey()

#counting groups
clear('groups.txt')
sortedGroups = getSortedGroupsCount(input, groups)

for i, j in sortedGroups:
    append('groups.txt', '\n'+str(i)+' => '+str(j))

append('groups.txt', '\n \n'+str(len(sortedGroups))+' groups')

#replacing chars using the key
result = input.translate(str.maketrans(replaceDict))

#generate html output
htmlResult = input+'<hr/>'
htmlResult += input.translate(str.maketrans(htmlFormatDict(replaceDict)))

#print output in the console
print(result)

#write output
write('output.txt', result)
write('output.html', htmlResult)
writeCharCount(input)
