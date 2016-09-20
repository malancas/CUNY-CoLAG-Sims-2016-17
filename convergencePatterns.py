from Child import Child
from collections import defaultdict
import csv
import datetime
from itertools import chain, permutations
import os


class convergencePatterns(object):
	def __init__(self, op):
		# Each defaultdict is used to store every pair, trio, and quartet of parameter convergence orders
		# found in the learners.
                self.outputPath = op
		self.pairDict = defaultdict(lambda: defaultdict(lambda: 0))
		self.trioDict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0)))
		self.quartetDict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0))))


        def writePairResults(self):
		f = open(self.outputPath[:-4] + '_pairConvergenceResults.csv', 'a')
		try:
                        # Make csv writer and lambda function to write the 
                        # row headers and corresponding pairs to a new output file
			writer = csv.writer(f)
                        f = lambda x,y: 'p{}<p{}'.format(x,y)

			print 'Hello'
		finally:
			f.close()

        
        # Creates column headers for each output file
        # Will print every possible permutation for the
        # chosen number of parameters for comparison
        def writeHeader(self, n):
                columnHeader = 'p{}' + ' < p{}' * (n-1)
                perms = (list(permutations(range(1,14), n)))
                f = lambda perms: columnHeader.format(*perms)
                return map(f, perms)


        def writeTrioResults(self):
                os.makedirs(self.outputPath)
                outFile = os.path.join(self.outputPath + '_quartetConvergenceResults.csv')
                f = open(outFile, 'a')

                try:
                        writer = csv.writer(f)
                        # For each possible trio permutation, add the sum of the fourth dict elements and feed them into writerow with an auxiliary function
                        writer.writerow(self.writeHeader(3))
                finally:
                        f.close()


        def writeQuartetResults(self):
                os.makedirs(self.outputPath)
                outFile = os.path.join(self.outputPath + '_quartetConvergenceResults.csv')
                f = open(outFile, 'a')

                try:
                        writer = csv.writer(f)
                        k = lambda perms: self.quartetDict[perms[0]][perms[1]][perms[2]][perms[3]]
                        writer.writerow(self.writeHeader(4))
                        writer.writerow(map(k,permutations(range(1,14),4)))
                finally:
                        f.close()


	def writeResults(self, outputFileName):
		#The function will write to files using a default name format
		self.trioOutputFile = outputFileName[:-4] + '_TrioConvergenceResults.csv'
		self.quartetOutputFile = outputFileName[:-4] + '_QuartetConvergenceResults.csv'

		self.writePairResults()
		print 'Pair results written to file'


	def percentage(self, num, total):
  		return 100 * float(num)/float(total)


	def printConvergencePairs(self):
		for m in range(0, 13):
			for n in range(0, 13):
				if (m != n):
					try:
						print "P({0} < {1})".format(m, n)
						print self.pairDict[m][n]
						print '\n'
					except KeyError:
						print ""


	# Will check for different sentence convergence foursome
	# combinations exist. Different combinations are added to quarterDict
	# if they don't appear, otherwise the count within their corresponding
	# dictionary entry is incremented
	def findQuartetConvergencePatterns(self, sortedTCV):
		for i in range(0, 13):
			for j in range(i+1, 13):
				for k in range(j+1, 13):
					for l in range(k+1, 13):
						firstParm = sortedTCV[i][1]
						secondParm = sortedTCV[j][1]
						thirdParm = sortedTCV[k][1]
						fourthParm = sortedTCV[l][1]

						self.quartetDict[firstParm][secondParm][thirdParm][fourthParm] += 1


	# Will check for different sentence convergence threesome
	# combinations exist. Different combinations are added to trioDict
	# if they don't appear, otherwise the count within their corresponding
	# dictionary entry is incremented
	def findTrioConvergencePatterns(self, sortedTCV):
		for i in range(0, 13):
			for j in range(i+1, 13):
				for k in range(j+1, 13):
					firstParm = sortedTCV[i][1]
					secondParm = sortedTCV[j][1]
					thirdParm = sortedTCV[k][1]
					self.trioDict[firstParm][secondParm][thirdParm] += 1


	# Checks if key value pairs exist for each possible pairing in the current
	# sorted time course vector. If not, a pair is made and a count recording
	# the number of times the ordering appears in every learner. If the pair
	# already exists, the count is incremented
	def findConvergencePairs(self, sortedTCV):
		for i in range(0, 12):
			for j in range(i+1, 13):
				firstParm = sortedTCV[i][1]
				secondParm = sortedTCV[j][1]

				self.pairDict[firstParm][secondParm] += 1


	# Will track the different convergence patterns (the order in which each parameter converges)
	# that appear in a learner's time course vector.
	# Currently, it will track pairs, triplets, and quartets of parameter combinations
	def findConvergencePatterns(self, tcvList):
		for tcv in tcvList:
			# Sort the learner's timeCourseVector based on the convergence
			# time of each parameter
			sortedTCV = sorted(tcv, key=lambda parameter: parameter[0])
			assert(len(sortedTCV) == 13)

			self.findConvergencePairs(sortedTCV)
			self.findTrioConvergencePatterns(sortedTCV)
			self.findQuartetConvergencePatterns(sortedTCV)
