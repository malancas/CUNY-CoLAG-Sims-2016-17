#!/usr/bin/python
from getRelevanceString import getRelevanceString

idDict = {}
n = -1
with open('COLAG_2011_ids.txt', 'r') as infile:
    content = infile.readlines()
    for line in content:
        grammId, sentId, structId = line.split('\t')
        bitstring = format(int(grammId), '16b')

        if n == -1:
            n = len(bitstring)

        if structId in idDict:
            if not bitstring in idDict[structId]:
                idDict[structId].append(bitstring)
        else:
            idDict[structId] = [bitstring]

relevanceDict = {}
for key, value in idDict.items():
    relevanceDict[key] = getRelevanceString(value, n)

newLines = []

with open('COLAG_2011_ids.txt', 'r') as f:
    for line in f.readlines():
        grammId, sentId, structId = line.split('\t')
        newLines.append(' '.join([line.rstrip('\n'), '\t', relevanceDict[structId], '\n']))

with open('COLAG_2011_ids_relevance.txt', 'w') as f:
    f.writelines(newLines) 

print('New file created!')
