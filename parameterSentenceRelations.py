#!/opt/anaconda/bin/python
import sys

targetGrammar = sys.argv[1]
infoFile = open('EngFrJapGerm.txt', 'rU')
allSentences = infoFile.readlines()
infoFile.close()

foundAllTargetSentences = False
foundTargetGrammar = False
selectedSentences = []
i = 0
while not foundAllTargetSentences:
    currGrammar = allSentences[i].split('\t',1)[0]
    if currGrammar == targetGrammar:
        selectedSentences.append(allSentences[i])
        foundTargetGrammar = True
    if foundGrammar and currGrammar != targetGrammar:
        foundAllTargetSentences = True
    i += 1

sentenceParameterRelations = {}
sampleGrammar = [0,0,0,0,0,0,1,0,0,0,1,0,1]
for sentence in selectedSentences:
    # Process each sentence through grammar,
    # compare old and new grammar to find 
    # parameters the sentences trigger 
