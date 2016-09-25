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

        
        # Creates column headers for each output file
        # Will print every possible permutation for the
        # chosen number of parameters for comparison
        def getHeader(self, n):
                columnHeader = 'p{}' + ' < p{}' * (n-1)
                perms = (list(permutations(range(1,14), n)))
                f = lambda perms: columnHeader.format(*perms)
                return map(f, perms)


        def parametersAreDifferent(self,p1,p2,p3,p4):
                return  p3 != p1 and p3 != p2 and p4 != p1 and p4 != p2


        def getPairDictTotal(self, permList):
                p1, p2 = permList[0], permList[1]
                total = 0
                perms = (list(permutations(range(1,14),2)))
                for perm in perms:
                        if self.parametersAreDifferent(p1,p2,perm[0],perm[1]):
                                total += self.quartetDict[p1][p2][perm[0]][perm[1]]
                return total

        # 156 total permutations
        def writePairResults(self):
                outFile = os.path.join(self.outputPath + '_PairConvergenceResults.csv')
                with open(outFile, 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow(self.getHeader(2))
                        permList = list(permutations(range(1,14),2))
                        writer.writerow(map(self.getPairDictTotal,permList))


        def getTrioDictTotal(self, permList):
                p1, p2, p3 = permList[0], permList[1], permList[2]
                total = 0
                for i in range(1,14):
                        if i != p1 and i != p2 and i != p3:
                                total += self.quartetDict[p1][p2][p3][i]
                return total


        '''
        Will record the number of times each threesome permutation of parameters 1-13
        occurs. Since the total number of permutations exceed the cell limit of a row,
        the header and results will be printed to multiple rows
        '''
        def writeTrioResults(self):
                outFile = os.path.join(self.outputPath + '_TrioConvergenceResults.csv')
                with open(outFile, 'a') as f:
                        writer = csv.writer(f)
                        header = self.getHeader(3)
                        perms = list(permutations(range(1,14),3))
                        writer.writerow(header[:1024])
                        writer.writerow(map(self.getTrioDictTotal,perms[:1024]))
                        writer.writerow(header[1024:])
                        writer.writerow(map(self.getTrioDictTotal,perms[1024:]))


        '''
        Will record the number of times each foursome permutation of parameters 1-13
        occurs. Since the total number of permutations exceed the cell limit of a row,
        the header and results will be printed to multiple rows
        '''
        def writeQuartetResults(self):
                outFile = os.path.join(self.outputPath + '_QuartetConvergenceResults.csv')
                with open(outFile, 'a') as f:
                        writer = csv.writer(f)
                        header = self.getHeader(4)
                        perms = list(permutations(range(1,14),4))
                        numberOfRows = len(perms) / 1024
                        startIndex = 0
                        endIndex = 1024
                        k = lambda perms: self.quartetDict[perms[0]][perms[1]][perms[2]][perms[3]]
                        for i in range(numberOfRows):
                                writer.writerow(header[startIndex:endIndex])
                                writer.writerow(map(k,perms[startIndex:endIndex]))
                                startIndex = endIndex + 1
                                endIndex = startIndex + 1024


	def writeResults(self):
		self.writePairResults()
		print 'Pair results written to file'

                self.writeTrioResults()
		print 'Trio results written to file'

                self.writeQuartetResults()
		print 'Quartet results written to file'


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

			self.findQuartetConvergencePatterns(sortedTCV)
                self.writeResults()
