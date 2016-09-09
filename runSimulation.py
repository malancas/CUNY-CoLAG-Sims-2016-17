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
		self.outputFile = ''


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


	# Writes the time (particular sentence) that each parameter of each eChild converged on
	def writeResults(self, eChild, count):
		# Change outputfile format to include timestamp
		f = open(self.outputFile, 'a')
		try:
			writer = csv.writer(f)
			if not count:
				writer.writerow( ('p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13') )

			writer.writerow( (eChild.timeCourseVector[0][0], eChild.timeCourseVector[1][0], eChild.timeCourseVector[2][0], 
				eChild.timeCourseVector[3][0], eChild.timeCourseVector[4][0], eChild.timeCourseVector[5][0], 
				eChild.timeCourseVector[6][0], eChild.timeCourseVector[7][0], eChild.timeCourseVector[8][0], 
				eChild.timeCourseVector[9][0], eChild.timeCourseVector[10][0], eChild.timeCourseVector[11][0], 
				eChild.timeCourseVector[12][0]) )
		finally:
			f.close()


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
		tempFileName = self.getLanguage() + '_' + str(maxLearners) + datetime.datetime.now().isoformat().replace(':','.') + '.csv'
		self.outputFile = os.path.join('./results/', tempFileName)

		# Stores the time course vectors of each learner after processing the specified number
		# of sentences
		tcvList = []

		for i in range(0, maxLearners):
			tcvList.append(self.doesChildLearnGrammar(i, Child(), maxSentences))
			print "Finished #{}".format(i)

		# If convergenceFlag is set to true, make a convergencePatterns instance 
		# and find resulting convergence patterns
		if convergenceFlag:
			patterns = convergencePatterns()
			patterns.findConvergencePatterns(tcvList)

		# If plotFlag is set to true, corresponding plots are produced and saved
		if plotFlag:
			os.system("./pset_plot.py {}".format(self.outputFile))
			os.system("./convergenceTime_plot.py {}".format(self.outputFile))
