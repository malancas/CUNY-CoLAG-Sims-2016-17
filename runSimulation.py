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
			if self.sentenceInfo[i][:3] == grammarID or self.sentenceInfo[i][:4] == grammarID:
				self.selectedSentences.append(self.sentenceInfo[i])


	def writeResults(self, eChild, count):
		data = [eChild.grammarLearned, eChild.grammar, eChild.expectedGrammar, eChild.totalTime]
		f = open('German_results_100000_2.csv', 'a')
		w = csv.writer(f, delimiter = ',')
		if count == 0:
			w.writerow(["Grammar Learned?", "Learned Grammar", "Expected Grammar", "Total Time"])
		w.writerow(data)
		f.close()


	def doesChildLearnGrammar(self, count, eChild):
		eChild.timeCourseVector = [[-1, 0]] * 13
		for i in range(0,13):
			eChild.timeCourseVector[i][1] = i+1

		start = time.clock()

		while not eChild.grammarLearned and eChild.sentenceCount < 1000:
			eChild.consumeSentence(random.choice(self.selectedSentences))
			eChild.setParameters(count)
			eChild.sentenceCount += 1

		eChild.totalTime = time.clock() - start

		#write to file: 1st column = yes/no converged, 2nd column = target grammar id, 3rd column = final grammar id, 
		#4th column = binary grammar as string, 13 additional columns for each number in the binary final grammar
		self.writeResults(eChild, count)
		return eChild


	def runSimulation(self, num):
		for i in range(0,num):
			self.childList.append(self.doesChildLearnGrammar(i, Child()))
			print "Finished #{}".format(i)
