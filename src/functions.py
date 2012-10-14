from operator import itemgetter

#sort an array, keeping the key => value association
def asort(d):
     return sorted(d.items(), key=lambda x: x[1])[::-1]

#sort a list of nested list
def lsort(l):
    sort_key = lambda s: (-len(s), s)
    l.sort(key=sort_key)

    return l

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

#count the number of each char in the string
def charCount(string):
    tmp = {}
    for i in string:
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] = 1
    
    return tmp

#return the list of the chars present in the string
def charList(string):
    chars = list()

    for char in string:
        if char in chars:
            continue
        else:
            chars.append(char)

    return chars

#write the char count into a file
def writeCharCount(string):
    split = asort(charCount(string))
    content = ''
    for key, value in split:
        content += '\n'+str(key)+' => '+str(value)
    
    write('chars.txt', content)

#transform the key to generate a colored html output
def htmlFormatDict(dict):
    for i in dict:
        dict[i] = '<span style="color: red;">'+dict[i]+'</span>'

    return dict

#sort the result of groupsCount()
def getSortedGroupsCount(content, groups):
    tmpGroups = list()
    for i,j in list(groupsCount(content, groups)):
        tmpGroups.append([i, j])

    return sorted(tmpGroups, key=itemgetter(1))[::-1]

#count the number of each group
def groupsCount(content, groups):
    for elmt in groups:
        group = ''.join(elmt)
        result = content.count(group)

        if result != 0:
            yield [group, result]
