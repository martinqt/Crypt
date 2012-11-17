from operator import itemgetter
from collections import deque
import os, sys
from key import *
sys.path.insert(0, os.getcwd()+'/src/functions')
from file import *
from groups import *

#sort a dict, keeping the key => value association
def asort(dict, descending = True, fromKey = False):
     if not fromKey:
        tmp = sorted(dict.items(), key=lambda x: x[1])
        if descending:
            return tmp[::-1]
        else:
            return tmp
     else:
        tmp = sorted(dict.items(), key=lambda x: x[0])
        if descending:
            return tmp[::-1]
        else:
            return tmp

#count the number of each char in the string
def getCharCount(string, outputFormat = ''):
    tmp = dict()

    for i in string:
        if not i in tmp:
            if outputFormat == 'frequency':
                tmp[i] = string.count(i)/len(string)
            elif outputFormat == 'percent':
                tmp[i] = string.count(i)/len(string)*100
            else:
                tmp[i] = string.count(i)

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
def writeCharCount(input, outputFormat = '', file = 'output/chars.txt'):
    split = asort(getCharCount(input, outputFormat))
    content = ''

    for key, value in split:
        content += '\n'+str(key)+' => '+str(value)
    
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
            dict[i] = '<span style="color: blue;">'+dict[i]+'</span>'

    return dict

def writeHtmlFile():
    input = read('input.txt')
    replaceDict = getKey()

    htmlResult = input+'<hr/>'
    htmlResult += transform(input, htmlFormatDict(replaceDict))

    write('output/output.html', htmlResult)

#apply the dict to the input
def transform(input, replaceDict):
    return input.translate(str.maketrans(replaceDict))
