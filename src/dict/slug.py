import re, fileinput, sys

filename = sys.argv[1]

words = list()
replacement = {
    'é': 'e',
    'è': 'e',
    'ê': 'e',
    'à': 'a',
    'â': 'a',
    'î': 'i',
    'ï': 'i',
    'ù': 'u',
    'ô': 'o',
}
content = ''
pattern = re.compile('('+'|'.join(replacement.keys())+')')
i = 0

for line in fileinput.input([filename]):
    words.append(line)
    tmp = pattern.sub(lambda x: replacement[x.group()], line)
    if tmp != line:
        words.append(tmp)

file = open(filename, 'w')
file.write(''.join(words))
file.close()
