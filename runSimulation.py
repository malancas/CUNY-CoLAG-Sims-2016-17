from .Child import Child
from .convergencePatterns import convergencePatterns
import time
import random
import csv
import datetime
import os

class runSimulation(object):
    def __init__(self, si, lc):
        self.totalSentenceCount = 0.0
        self.totalConvergentChildren = 0.0
        self.sentenceInfo = si
        self.targetGrammar = lc
        self.selectedSentences = []
        self.outputFile = ''
        self.outputFile2 = ''

    # Prints the percentage of converged children
    # and the average sentence count of converged children
    def printResults(self, maxChildren):
        try:
            print('Percentage of converged children: '), (self.totalConvergentChildren / maxChildren) * 100, '%'
        except ZeroDivisionError:
            print('Zero Error')

        try:
            print('Average sentence count of converged children: '), (self.totalSentenceCount / self.totalConvergentChildren)
        except ZeroDivisionError:
            print('Average sentence count of converged children: 0')               


    # Write the header columns to the output file
    def writeOutputHeader(self):
        with open(self.outputFile2,"a+") as outFile:
            writer = csv.writer(outFile)
            writer.writerow(('TCV', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Grammar'))
            writer.writerow(['p{}'.format(i) for i in range(1,14)] * 2)
        with open(self.outputFile,"a+") as outFile:
            writer = csv.writer(outFile)
            writer.writerow(['p{}'.format(i) for i in range(1,14)])


    # Writes the time (particular sentence) that each parameter of each eChild converged on
    # as well as writing the final grammar of the learner to the output file
    def writeResults(self, eChild):
        with open(self.outputFile2,"a+") as outFile:
            writer = csv.writer(outFile)

            tcv = eChild.timeCourseVector
            grammar = eChild.grammar
            writer.writerow( (tcv[0][0], tcv[1][0], tcv[2][0], tcv[3][0], tcv[4][0], tcv[5][0], 
            tcv[6][0], tcv[7][0], tcv[8][0], tcv[9][0], tcv[10][0], tcv[11][0], tcv[12][0],
            grammar[0], grammar[1], grammar[2], grammar[3], grammar[4], grammar[5], grammar[6],
            grammar[7], grammar[8], grammar[9], grammar[10], grammar[11], grammar[12]) )

        with open(self.outputFile,"a+") as outFile:
            writer = csv.writer(outFile)
            tcv = eChild.timeCourseVector
            writer.writerow( (tcv[0][0], tcv[1][0], tcv[2][0], tcv[3][0], tcv[4][0], tcv[5][0], 
                tcv[6][0], tcv[7][0], tcv[8][0], tcv[9][0], tcv[10][0], tcv[11][0], tcv[12][0]) )


    # Fills runSimulation object's selectedSentences array with sentences who
    # belong to the language that correspond to targetGrammar
    def makeSelectedSentenceList(self):
        lc = str(self.targetGrammar)
        for i in range(0, len(self.sentenceInfo)):
            # Get the code from the current sentence and compare it to lc
            if self.sentenceInfo[i].split('\t',1)[0] == lc:
                self.selectedSentences.append(self.sentenceInfo[i])


    # Returns the name of the language
    # that languageCode corresponds to
    def getLanguage(self):
        if self.targetGrammar == 611:
            return 'English'
        elif self.targetGrammar == 584:
            return 'French'
        elif self.targetGrammar == 2253:
            return 'German'
        elif self.targetGrammar == 3856:
            return 'Japanese'


    # The child, or learner, processes sentences belonging to the chosen language
    # until its grammar is identical to the language's or it has processed the
    # chosen number of sentences (maxSentences). The timeCourseVector data of the
    # learner is then written to the output file
    def doesChildLearnGrammar(self, eChild, maxSentences):
        start = time.clock()

        while not eChild.grammarLearned and eChild.sentenceCount < maxSentences:
            eChild.consumeSentence(random.choice(self.selectedSentences))
            eChild.setParameters(eChild.sentenceCount)
            eChild.sentenceCount += 1

            eChild.totalTime = time.clock() - start

            self.writeResults(eChild)

            # Return the time course vector so it can be used to find convergence patterns
            return eChild.timeCourseVector


    # Runs a simulation containing maxLearners number of learners
    # Each learner runs the doesChildLearnGrammar function and processes
    # sentences with the chosen constraints
    def runLearners(self, maxSentences, maxLearners, convergenceFlag, plotFlag):
        # Create the name and path of the output file
        baseName = self.getLanguage() + '_' + str(maxLearners)  + '_' + str(maxLearners) + datetime.datetime.now().isoformat().replace(':','.')
        tempPathName = './results/{}'.format(baseName)
        tempFileName = baseName + '_tcv.csv'
        tempFileName2 = baseName + '_grammar_tcv.csv'
        os.makedirs(tempPathName)
        self.outputFile = os.path.join(tempPathName, tempFileName)
        self.outputFile2 = os.path.join(tempPathName, tempFileName2)
        self.writeOutputHeader()

        # Stores the time course vectors of each learner after processing the specified number
        # of sentences
        tcvList = []

        for i in range(0, maxLearners):
            tcvList.append(self.doesChildLearnGrammar(Child(), maxSentences))
            print('Finished #{}'.format(i+1))

            # If convergenceFlag is set to true, make a convergencePatterns instance 
            # and find resulting convergence patterns
            if convergenceFlag:
                patterns = convergencePatterns(self.outputFile[:-7])
                patterns.findConvergencePatterns(tcvList)

            # If plotFlag is set to true, corresponding plots are produced and saved
            if plotFlag:
                os.system("./pset_plot.py {}".format(self.outputFile))
                os.system("./convergenceTime_plot.py {}".format(self.outputFile))
