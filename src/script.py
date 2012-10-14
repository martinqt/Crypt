from functions import *
from itertools import product
from key import *

#the encrypted message
content = read('input.txt')
#the chars in the message
charList = charList(content)
#list of the possible groups
groups = product(''.join(charList), repeat=2)

#get the key
replaceDict = getKey()

#counting groups
write('groups.txt', '')
sortedGroups = getSortedGroupsCount(content, groups)

for i, j in sortedGroups:
    append('groups.txt', '\n'+str(i)+' => '+str(j))

append('../groups.txt', '\n \n'+str(len(sortedGroups))+' groups')

#replacing chars using the key
result = content.translate(str.maketrans(replaceDict))

#generate html output
htmlResult = content+'<hr/>'
htmlResult += content.translate(str.maketrans(htmlFormatDict(replaceDict)))

#print output in the console
print(result)

#write output
write('output.txt', result)
write('output.html', htmlResult)
writeCharCount(content)
