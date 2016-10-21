#!/opt/anaconda/bin/python
import sys
import csv
from collections import defaultdict
from Child import Child

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
    if foundTargetGrammar and currGrammar != targetGrammar:
        foundAllTargetSentences = True
    i += 1

sentenceParameterTriggers = defaultdict(lambda: [])
sampleLearner = Child()
oldGrammar = [0,0,0,0,0,0,1,0,0,0,1,0,1]
print(len(selectedSentences))
for sentence in selectedSentences:
    sentenceStr = sentence.rsplit('\t', 3)[2]
    sampleLearner.consumeSentence(sentence)
    sampleLearner.setParameters()
    for i in range(13):
        if oldGrammar[i] != sampleLearner.grammar[i]:
            print('Doesnt match')
            sentenceParameterTriggers[sentenceStr].append('p{}'.format(i+1))
    oldGrammar = sampleLearner.grammar

with open('sentenceParameterTrigger_results.csv', 'a+') as outFile:
    writer = csv.writer(outFile)
    for key in sentenceParameterTriggers:
        writer.writerow((key, sentenceParameterTriggers[key]))
