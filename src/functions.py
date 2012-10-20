from operator import itemgetter

#sort an array, keeping the key => value association
def asort(d):
     return sorted(d.items(), key=lambda x: x[1])[::-1]

#write the content into the file
def write(file, content):
    file = open(file, 'w')
    file.write(content)
    file.close()

#read the content of the file
def read(file):
    file = open(file, 'r')
    content = file.read()
    file.close()
    
    return content

#append content to a file
def append(file, content):
    file = open(file, 'a+')
    file.write(content)
    file.close()

#shortcut of write(file, '')
def clear(file):
    write(file, '')

#count the number of each char in the string
def getCharCount(string):
    tmp = dict()
    for i in string:
        if not i in tmp:
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
def writeCharCount(input, file = 'chars.txt'):
    split = asort(getCharCount(input))
    content = ''
    for key, value in split:
        content += '\n'+str(key)+' => '+str(value)
    
    write(file, content)

#transform the key value to generate a colored html output
def htmlFormatDict(dict):
    for i in dict:
        dict[i] = '<span style="color: red;">'+dict[i]+'</span>'

    return dict

#get the sorted result of getGroupsCount()
def getSortedGroupsCount(content, groups):
    tmpGroups = list()
    for i,j in list(getGroupsCount(content, groups)):
        tmpGroups.append([i, j])

    return sorted(tmpGroups, key=itemgetter(1))[::-1]

#count the number of each group
def getGroupsCount(content, groups):
    for elmt in groups:
        group = ''.join(elmt)
        result = content.count(group)

        if result != 0:
            yield [group, result]

#generate and write groups analysis
def doGroupsAnalysis(input, groups, file = 'groups.txt'):
    #counting groups
    clear(file)
    sortedGroups = getSortedGroupsCount(input, groups)

    for i, j in sortedGroups:
        append(file, '\n'+str(i)+' => '+str(j))

    append(file, '\n \n'+str(len(sortedGroups))+' groups')

#apply the dict to the input
def transform(input, replaceDict):
    return input.translate(str.maketrans(replaceDict))
