from Child import Child
from convergencePatterns import convergencePatterns
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
		self.languageCode = lc
		self.selectedSentences = []
		self.tcvOutputFile = ''
                self.grammarOutputFile = ''


	# Prints the percentage of converged children
	# and the average sentence count of converged children
	def printResults(self, maxChildren):
		try:
			print 'Percentage of converged children: ', (self.totalConvergentChildren / maxChildren) * 100, '%'
		except ZeroDivisionError:
			print "Zero error"

		try:
			print 'Average sentence count of converged children: ', (self.totalSentenceCount / self.totalConvergentChildren)
		except ZeroDivisionError:
			print "Average sentence count of converged children: 0"               


	# Writes the time (particular sentence) that each parameter of each eChild converged on in the TCV output file
        # Writes the final grammar of the learner to the grammar output file
	def writeResults(self, eChild, count):
		# Change outputfile format to include timestamp
		tcvFile = open(self.tcvOutputFile, 'a')
                grammarFile = open(self.grammarOutputFile, 'a')
                
		try:
			tcvWriter = csv.writer(tcvFile)
                        grammarWriter = csv.writer(grammarFile)
			if not count:
                                header = ('p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13')
				tcvWriter.writerow(header)
                                grammarWriter.writerow(header)
                                
                        tcv = eChild.timeCourseVector
			tcvWriter.writerow( (tcv[0][0], tcv[1][0], tcv[2][0], tcv[3][0], tcv[4][0], tcv[5][0], 
				tcv[6][0], tcv[7][0], tcv[8][0], tcv[9][0], tcv[10][0], tcv[11][0], tcv[12][0]) )
                        grammar = eChild.grammar
                        grammarWriter.writerow( (grammar[0], grammar[1], grammar[2], grammar[3], grammar[4], grammar[5], grammar[6],
                        grammar[7], grammar[8], grammar[9], grammar[10], grammar[11], grammar[12]) )
		finally:
			tcvFile.close()
                        grammarFile.close()


	# Fills runSimulation object's selectedSentences array with sentences who
	# belong to the language that correspond to languageCode
	def makeSelectedSentenceList(self):
		lc = str(self.languageCode)

		for i in range(0, len(self.sentenceInfo)):
			# Get the code from the current sentence and compare it to lc
			if self.sentenceInfo[i].split('\t',1)[0] == lc:
				self.selectedSentences.append(self.sentenceInfo[i])


	# Returns the name of the language
	# that languageCode corresponds to
	def getLanguage(self):
		if self.languageCode == 611:
			return 'English'
		elif self.languageCode == 584:
			return 'French'
		elif self.languageCode == 2253:
			return 'German'
		elif self.languageCode == 3856:
			return 'Japanese'


	# The child, or learner, processes sentences belonging to the chosen language
	# until its grammar is identical to the language's or it has processed the
	# chosen number of sentences (maxSentences). The timeCourseVector data of the
	# learner is then written to the output file
	def doesChildLearnGrammar(self, count, eChild, maxSentences):
		start = time.clock()

		while not eChild.grammarLearned and eChild.sentenceCount < maxSentences:
			eChild.consumeSentence(random.choice(self.selectedSentences))
			eChild.setParameters(eChild.sentenceCount)
			eChild.sentenceCount += 1

		eChild.totalTime = time.clock() - start

		self.writeResults(eChild, count)

		# Return the time course vector so it can be used to find convergence patterns
		return eChild.timeCourseVector


	# Runs a simulation containing maxLearners number of learners
	# Each learner runs the doesChildLearnGrammar function and processes
	# sentences with the chosen constraints
	def runLearners(self, maxSentences, maxLearners, convergenceFlag, plotFlag):
		# Create the name and path of the output file
		tempPathName = self.getLanguage() + '_' + str(maxLearners) + datetime.datetime.now().isoformat().replace(':','.')
                os.makedirs('results/{}'.format(tempPathName))
		self.tcvOutputFile = os.path.join('./results/{}'.format(tempPathName), tempPathName + '_TCV_.csv')
		self.grammarOutputFile = os.path.join('./results/{}'.format(tempPathName), tempPathName + '_grammar_.csv')                

		# Stores the time course vectors of each learner after processing the specified number
		# of sentences
		tcvList = []

		for i in range(0, maxLearners):
			tcvList.append(self.doesChildLearnGrammar(i, Child(), maxSentences))
			print "Finished #{}".format(i+1)

		# If convergenceFlag is set to true, make a convergencePatterns instance 
		# and find resulting convergence patterns
		if convergenceFlag:
			patterns = convergencePatterns()
			patterns.findConvergencePatterns(tcvList)

		# If plotFlag is set to true, corresponding plots are produced and saved
		if plotFlag:
			os.system("./pset_plot.py {}".format(self.outputFile))
			os.system("./convergenceTime_plot.py {}".format(self.outputFile))
