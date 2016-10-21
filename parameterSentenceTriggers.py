#!/opt/anaconda/bin/python
import sys
import csv
import os
from collections import defaultdict
from Child import Child

targetGrammar = sys.argv[1]
languageName = ''
if targetGrammar == '611':
    languageName = 'English'
elif targetGrammar == '584':
    languageName = 'French'
elif targetGrammar == '2253':
    languageName = 'German'
elif targetGrammar == '3856':
    languageName = 'Japanese'

tempFileName = languageName + '_sentenceParameterTrigger_results.csv'
tempPathName = './results/sentenceParameterTriggers'
if not os.path.isdir(tempPathName):
    os.makedirs(tempPathName)
outputFile = os.path.join(tempPathName, tempFileName)
if os.path.isfile(outputFile):
    answer = input('File already exists. Overwrite? Y/N: ')
    if answer == 'N' or answer == 'n':
        sys.exit(0)

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
for sentence in selectedSentences:
    sentenceStr = sentence.rsplit('\t', 3)[2]
    sampleLearner.consumeSentence(sentence)
    sampleLearner.setParameters()
    for i, parameter in enumerate(oldGrammar):
        if parameter != sampleLearner.grammar[i]:
            sentenceParameterTriggers[sentenceStr].append('p{}'.format(i+1))
    oldGrammar = sampleLearner.grammar

with open(outputFile, 'a+') as outFile:
    writer = csv.writer(outFile)
    for key in sentenceParameterTriggers:
        writer.writerow((key, sentenceParameterTriggers[key]))
