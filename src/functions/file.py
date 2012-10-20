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
