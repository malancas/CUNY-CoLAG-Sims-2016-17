from Child import Child
import plot
import time
import random
import csv

class runSimulation(object):

	def __init__(self, si):
		self.totalSentenceCount = 0
		self.totalConvergentChildren = 0
		self.sentenceInfo = si
		self.selectedSentences = []


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


	# Fills runSimulation object's selectedSentences array with sentences who
	# belong to the language that correspond to languageCode
	def makeSelectedSentenceList(self, languageCode):
		for i in range(0, len(self.sentenceInfo)):
			if self.sentenceInfo[i][:3] == languageCode or self.sentenceInfo[i][:4] == languageCode:
				self.selectedSentences.append(self.sentenceInfo[i])


	# Writes the time (particular sentence) that each parameter of each eChild converged on
	def writeResults(self, eChild, count, outputFile):
		joinedTcv = ['eChild #{}'.format(count+1)]
		for i in range(0,13):
			joinedTcv.append(eChild.timeCourseVector[i][0])
		joinedTcv.append(' ')
		joinedTcv = ','.join(map(str, joinedTcv))

		f = open(outputFile, 'a')
		w = csv.writer(f, delimiter = ',')
		if not count:
			w.writerow(['observation', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13'])
		w.writerow([f.write(joinedTcv)])
		f.close()


	# The child, or learner, processes sentences belonging to the chosen language
	# until its grammar is identical to the language's or it has processed the
	# chosen number of sentences (maxSentences). The timeCourseVector data of the
	# learner is then written to the output file
	def doesChildLearnGrammar(self, count, eChild, maxSentences, outputFile):
		start = time.clock()

		while not eChild.grammarLearned and eChild.sentenceCount < maxSentences:
			eChild.consumeSentence(random.choice(self.selectedSentences))
			eChild.setParameters(eChild.sentenceCount)
			eChild.sentenceCount += 1

		eChild.totalTime = time.clock() - start

		self.writeResults(eChild, count, outputFile)
		return eChild


	# Runs a simulation containing maxLearners number of learners
	# Each learner runs the doesChildLearnGrammar function and processes
	# sentences with the chosen constraints
	def runSimulation(self, maxLearners, maxSentences, outputFile):
		childList = []
		for i in range(0, maxLearners):
			childList.append(self.doesChildLearnGrammar(i, Child(), maxSentences, outputFile))
			print "Finished #{}".format(i)
		plot.findProbabilities(childList, maxLearners)
