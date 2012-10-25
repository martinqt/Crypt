from operator import itemgetter
from collections import deque
from wordList import *
import os
import sys
sys.path.insert(0, os.getcwd()+'/src/functions')
from file import *

#sort an array, keeping the key => value association
def asort(d):
     return sorted(d.items(), key=lambda x: x[1])[::-1]

#count the number of each char in the string
def getCharCount(string, frequency = False):
    tmp = dict()

    for i in string:
        if not i in tmp:
            if not frequency:
                tmp[i] = string.count(i)
            else:
                tmp[i] = string.count(i)/len(string)

    return tmp

#return the list of the chars present in the string
def getCharList(input):
    chars = list()

    for char in input:
        if char in chars:
            continue
        else:
            if char == char:
                chars.append(char)

    return chars

#write the char count into a file
def writeCharCount(input, frequency = False, file = 'chars.txt'):
    split = asort(getCharCount(input, frequency))
    content = ''
    for key, value in split:
        content += '\n'+str(key)+' => '+str(value)
    
    write(file, content)

#transform the key value to generate a colored html output
def htmlFormatDict(dict, smart = True):
    for i in dict:
        if smart and dict[i] == '-':
            if i == ' ':
                dict[i] = '<span style="color: red;">@</span>'
            else:
                dict[i] = '<span style="color: red;">'+i+'</span>'
        else:
            dict[i] = '<span style="color: green;">'+dict[i]+'</span>'

    return dict

#get the sorted result of getGroupsCount()
def getSortedGroupsCount(content, groups, frequency = False):
    tmpGroups = list()

    for i,j in list(getGroupsCount(content, groups, frequency)):
        tmpGroups.append([i, j])

    return sorted(tmpGroups, key=itemgetter(1))[::-1]

#count the number of each group
def getGroupsCount(content, groups, frequency = False):
    for elmt in groups:
        group = ''.join(elmt)
        if not frequency:
            result = content.count(group)
        else:
            result = content.count(group)/len(content)

        if result != 0:
            yield [group, result]

#generate and write groups analysis
def doGroupsAnalysis(input, groups, frequency = False, file = 'groups.txt'):
    #counting groups
    clear(file)
    sortedGroups = getSortedGroupsCount(input, groups, frequency)

    for i, j in sortedGroups:
        append(file, '\n'+str(i)+' => '+str(j))

    append(file, '\n \n'+str(len(sortedGroups))+' groups')

#apply the dict to the input
def transform(input, replaceDict):
    return input.translate(str.maketrans(replaceDict))
