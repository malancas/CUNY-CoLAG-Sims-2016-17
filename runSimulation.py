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
		joinedTcv = ['eChild #{}'.format(count+1)]
		for i in range(0,13):
			joinedTcv.append(eChild.timeCourseVector[i][0])
			#joinedTcv.append(eChild.timeCourseVector[i][1])
		joinedTcv.append(' ')
		joinedTcv = ','.join(map(str, joinedTcv))

		f = open('French_results_100000_tcv.csv', 'a')
		w = csv.writer(f, delimiter = ',')
		if count == 0:
			w.writerow(['observation', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13'])
		w.writerow([f.write(joinedTcv)])
		f.close()


	def doesChildLearnGrammar(self, count, eChild):
		start = time.clock()

		while not eChild.grammarLearned and eChild.sentenceCount < 1000:
			eChild.consumeSentence(random.choice(self.selectedSentences))
			eChild.setParameters(eChild.sentenceCount)
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
