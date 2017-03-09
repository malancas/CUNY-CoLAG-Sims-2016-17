#!/opt/anaconda/bin/python
from sys import argv, exit
from csv import writer
from argparse import ArgumentParser
from os import path, makedirs
from datetime import datetime
from collections import defaultdict
from Child import Child

parser = ArgumentParser(prog='Sentence Triggers', description='Record which pieces of a sentence trigger a parameter')

parser.add_argument('integers', metavar='int', type=int, nargs=1,
                        help='The chosen language\'s grammar id is the only argument (English = 611, French = 584, German = 2253, Japanese = 3856)')

# The only argument is the decimal representation
# of a target grammar
args = parser.parse_args()
targetGrammar = args.integers[0]
languageName = ''
if targetGrammar == '611':
    languageName = 'English'
elif targetGrammar == '584':
    languageName = 'French'
elif targetGrammar == '2253':
    languageName = 'German'
elif targetGrammar == '3856':
    languageName = 'Japanese'

# Create the path and filename of the results file
tempFileName = languageName + '_sentenceParameterTrigger_' + datetime.now().isoformat().replace(':','.') + '.csv'
tempPathName = './results/sentenceParameterTriggers'
if not path.isdir(tempPathName):
    makedirs(tempPathName)
outputFile = path.join(tempPathName, tempFileName)


# Open the sentence file and read in the lines
infoFile = open('EngFrJapGerm.txt', 'rU')
allSentences = infoFile.readlines()
infoFile.close()

# Set up flags and counters used to determine
# when all sentences belonging to the chosen
# grammar have been found
foundAllTargetSentences = False
foundTargetGrammar = False
selectedSentences = []
i = 0

# Cycle through the read in lines to find
# the target sentences
while not foundAllTargetSentences:
    currGrammar = allSentences[i].split('\t',1)[0]
    if currGrammar == targetGrammar:
        selectedSentences.append(allSentences[i])
        foundTargetGrammar = True
    if foundTargetGrammar and currGrammar != targetGrammar:
        foundAllTargetSentences = True
    i += 1

# Set up the sample learner and dictionary used to record
# which sentences trigger which parameters
sentenceParameterTriggers = defaultdict(lambda: [])
sampleLearner = Child()
oldGrammar = [0,0,0,0,0,0,1,0,0,0,1,0,1]

# After processing each sentence, the sample learner's
# grammar will be compared to the old one. Differences will
# be noted and the sentence that caused the change along with the
# morphed parameter will be added to the dictionary
for sentence in selectedSentences:
    sentenceStr = sentence.rsplit('\t', 3)[2]
    sampleLearner.consumeSentence(sentence)
    sampleLearner.setParameters()
    for i, parameter in enumerate(oldGrammar):
        if parameter != sampleLearner.grammar[i] and (not 'p{}'.format(i+1) in sentenceParameterTriggers[sentenceStr]):
            sentenceParameterTriggers[sentenceStr].append('p{}'.format(i+1))
    oldGrammar = [0,0,0,0,0,0,1,0,0,0,1,0,1]

# The output file will opened and the corresponding
# sentences and parameters added line by line
with open(outputFile, 'a+') as outFile:
    writer = writer(outFile)
    for key in sentenceParameterTriggers:
        writer.writerow((key, sentenceParameterTriggers[key]))
