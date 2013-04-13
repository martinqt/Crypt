import pickle
from operator import itemgetter
from itertools import product
import re
import random

#read the content of the file
def read(file):
    file = open(file, 'r')
    content = file.read()
    file.close()

    return content

#write the content into the file
def write(file, content):
    file = open(file, 'w')
    file.write(content)
    file.close()

def writePickled(filename, content):
    """Write a pickled file"""
    with open(filename, 'wb') as fileObj:
                pickle.dump(content, fileObj)

def readPickled(path):
    """Load a pickled file"""
    with open(path, 'rb') as fileObj:
        content = pickle.load(fileObj)

    return content

#apply the key to the content
def transform(content, key):
    rep = dict((re.escape(k), v) for k, v in key.items())
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], content)

    return text

#read the content of the file
def read(file):
    file = open(file, 'r')
    content = file.read()
    file.close()
    
    return content

#get the sorted result of getGroupsCount()
def getSortedGroupsCount(content, groups):
    tmpGroups = list()

    for i,j in list(getGroupsCount(content, groups)):
        tmpGroups.append([i, j])

    return tmpGroups
    #return sorted(tmpGroups, key=itemgetter(1))[::-1]

#count the number of each group
def getGroupsCount(content, groups):
    length = len(content)
    for elmt in groups:
        group = ''.join(elmt)

        result = content.count(group)

        if result != 0:
            yield [group, result]

#generate and write groups analysis
def doGroupsAnalysis(input, groups):
    result = list()
    sortedGroups = getSortedGroupsCount(input, groups)

    for i, j in sortedGroups:
        result.append((str(i), round(j, 3)))

    return result

def getCharList(input):
    """Return the list of the chars present in the string."""
    chars = list()

    for char in input:
        if char in chars:
            continue
        else:
            chars.append(char)

    return chars

def buildKey(left, right):
    """Build the replacement key."""
    import sys

    key = dict()
    i = 0

    while i < len(left):
        key[left[i]] = right[i]
        i += 1

    return key

def evaluate(text, table):
    """Compute the text's score."""
    groups = list(product(''.join(getCharList(text)), repeat=2))
    analysis = doGroupsAnalysis(text, groups)
    score = 1

    for elmt in analysis:
        a = [x for x in table if elmt[0] in x[0]]
        if a == list():
            score = score*elmt[1]*0.01
        else:
            score = score*elmt[1]*a[0][1]

    return score

def randomSwap(right):
    """Randomly randomly swap two elements of the list."""
    a = random.randint(0, len(right)-1)
    b = random.randint(0, len(right)-1)
    right[a], right[b] = right[b], right[a]

    return list(right)

def getCharCount(string, outputFormat = ''):
    """Count the number of each char in the string."""
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
