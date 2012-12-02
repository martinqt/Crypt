# -*-coding:Utf-8 -*

from ..functions import *

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
def doGroupsAnalysis(input, groups, frequency = False, filename = 'output/groups.txt'):
    clear(filename)
    sortedGroups = getSortedGroupsCount(input, groups, frequency)

    for i, j in sortedGroups:
        append(filename, '\n'+str(i)+' => '+str(j))

    append(filename, '\n \n'+str(len(sortedGroups))+' groups')
