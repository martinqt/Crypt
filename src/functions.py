from operator import itemgetter
from collections import deque
import os, sys
sys.path.insert(0, os.getcwd()+'/src/functions')
from file import *
from groups import *

#sort a dict, keeping the key => value association
def sortDict(d):
     return dict(sorted(d.items(), key=lambda x: x[1])[::-1])

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
def writeCharCount(input, frequency = False, file = 'output/chars.txt'):
    split = sortDict(getCharCount(input, frequency))
    content = ''

    for i in split:
        content += '\n'+str(i)+' => '+str(split[i])
    
    write(file, content)

#transform the key value to generate a colored html output
def htmlFormatDict(dict, smart = True):
    for i in dict:
        if smart and dict[i] == '-':
            if i == ' ':
                dict[i] = '<span style="color: red;">-</span>'
            else:
                dict[i] = '<span style="color: red;">'+i+'</span>'
        else:
            dict[i] = '<span style="color: green;">'+dict[i]+'</span>'

    return dict

#apply the dict to the input
def transform(input, replaceDict):
    return input.translate(str.maketrans(replaceDict))
