from Child import Child
from convergencePatterns import convergencePatterns
from multiprocessing import Process, Lock, Queue
import time
import random
import csv

class runSimulation(object):
	def __init__(self, si):
		self.totalSentenceCount = 0
		self.totalConvergentChildren = 0
		self.sentenceInfo = si
		self.selectedSentences = []
		self.firstWrite = True
		self.lock = Lock()


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


	# Runs a simulation containing maxLearners number of learners
	# Each learner runs the doesChildLearnGrammar function and processes
	# sentences with the chosen constraints
	def runSimulation(self, maxLearners, maxSentences, outputFile):
		tcvList = []
		processes = []
		q = Queue()

		for i in range(maxLearners):
			c = Child(queue=q)
			processes.append(c)
			c.start()
			if self.firstWrite:
				self.firstWrite = False
		for proc in processes:
			proc.join()
			proc.queue.get()
			
			tcvList.append(proc.timeCourseVector)

		
		# Make a convergencePatterns instance and find resulting convergence patterns
		patterns = convergencePatterns()
		patterns.findConvergencePatterns(tcvList)