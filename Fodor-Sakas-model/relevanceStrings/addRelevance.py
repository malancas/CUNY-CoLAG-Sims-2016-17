#!/usr/bin/python
from getRelevanceString import getRelevanceString

idDict = {}
n = -1

# StructIds may appear in multiple times throughout the file
# Create a dictionary in which the key corresponds to a unique
# structId and the value is a list of differing bitstrings that
# all align with that structId
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
    # Process all the bitstrings in each iDict value to
    # produce a relevanceString for that structId
    relevanceDict[key] = getRelevanceString(value, n)

newLines = []

with open('COLAG_2011_ids.txt', 'r') as f:
    for line in f.readlines():
        grammId, sentId, structId = line.split('\t')
        newLines.append(' '.join([line.rstrip('\n'), '\t', relevanceDict[structId], '\n']))

with open('COLAG_2011_ids_relevance.txt', 'w') as f:
    f.writelines(newLines)

print('New file created!')
