from Child import Child
import time
import random
import csv

class runSimulation(object):

	def __init__(self, si):
		self.totalSentenceCount = 0
		self.totalConvergentChildren = 0
		self.sentenceInfo = si
		self.selectedSentences = []
		self.childList = []


	def printResults(self, maxChildren):
		try:
			print 'Percentage of converged children: ', (self.totalConvergentChildren / maxChildren) * 100, '%'
		except ZeroDivisionError:
			print "Zero error"

		try:
			print 'Average sentence count of converged children: ', (self.totalSentenceCount / self.totalConvergentChildren)
		except ZeroDivisionError:
			print "Average sentence count of converged children: 0"


	def makeSelectedSentenceList(self, grammarID):
		for i in range(0, len(self.sentenceInfo)):
			if self.sentenceInfo[i][:3] == grammarID or self.sentenceInfo[i][:4] == grammarID:
				self.selectedSentences.append(self.sentenceInfo[i])


	def writeResults(self, eChild, count, outputFile):
		joinedTcv = ['eChild #{}'.format(count+1)]
		for i in range(0,13):
			joinedTcv.append(eChild.timeCourseVector[i][0])
		joinedTcv.append(' ')
		joinedTcv = ','.join(map(str, joinedTcv))

		f = open(outputFile, 'a')
		w = csv.writer(f, delimiter = ',')
		if count == 0:
			w.writerow(['observation', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13'])
		w.writerow([f.write(joinedTcv)])
		f.close()


	def doesChildLearnGrammar(self, count, eChild, numberOfSentences, outputFile):
		start = time.clock()

		while not eChild.grammarLearned and eChild.sentenceCount < numberOfSentences:
			eChild.consumeSentence(random.choice(self.selectedSentences))
			eChild.setParameters(eChild.sentenceCount)
			eChild.sentenceCount += 1

		eChild.totalTime = time.clock() - start

		self.writeResults(eChild, count, outputFile)
		return eChild


	def runSimulation(self, num, numberOfSentences, outputFile):
		for i in range(0,num):
			self.childList.append(self.doesChildLearnGrammar(i, Child(), numberOfSentences, outputFile))
			print "Finished #{}".format(i)
