from Child import Child
import time
import random
import csv

class runSimulation(object):
	def __init__(self):
		self.totalSentenceCount = 0
		self.totalConvergentChildren = 0
		self.sentenceInfo = []
		self.selectedSentences = []
		self.childList = []


	def printResults(self, maxChildren):
		print 'Percentage of converged children: ', (self.totalConvergentChildren / maxChildren) * 100, '%'
		try:
			print 'Average sentence count of converged children: ', (self.totalSentenceCount / self.totalConvergentChildren)
		except ZeroDivisionError:
			print "Average sentence count of converged children: 0"

	def makeSelectedSentenceList(self, grammarID):
		for i in range(0, len(self.sentenceInfo)):
			if self.sentenceInfo[i][:3] == grammarID:
				self.selectedSentences.append(self.sentenceInfo[i])


	def doesChildLearnGrammar(self, count, eChild):
		start = time.time()

		while not eChild.grammarLearned and eChild.sentenceCount < 100000:
			eChild.consumeSentence(random.choice(self.selectedSentences))
			eChild.setParameters()
			eChild.sentenceCount += 1

		eChild.totalTime = time.time() - start

		#write to file: 1st column = yes/no converged, 2nd column = target grammar id, 3rd column = final grammar id, 
		#4th column = binary grammar as string, 13 additional columns for each number in the binary final grammar
		if eChild.grammarLearned:
			self.totalSentenceCount += eChild.sentenceCount
			self.totalConvergentChildren += 1

			timeFile = open('/home/malancas/Programming/Hunter/research/timeResults.txt', 'a')
			timeFile.write('eChild#{0} {1} \n'.format(count, eChild.totalTime))
			timeFile.close()
		else:
			nonConvergedFile = open('/home/malancas/Programming/Hunter/research/nonConverged.txt', 'a')
			nonConvergedFile.write('eChild#{0} {1} \n'.format(count, eChild.grammar))
			nonConvergedFile.close()

		return eChild


	def runSimulation(self, num):
		for i in range(0,num):
			print i
			self.childList.append(self.doesChildLearnGrammar(i, Child()))
			print "Finished #{}".format(i)
