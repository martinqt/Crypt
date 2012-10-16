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
    tmp = {}
    for i in string:
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] = 1
    
    return tmp

#return the list of the chars present in the string
def getCharList(string):
    chars = list()

    for char in string:
        if char in chars:
            continue
        else:
            chars.append(char)

    return chars

#write the char count into a file
def writeCharCount(string, file = 'chars.txt'):
    split = asort(getCharCount(string))
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
