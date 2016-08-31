from Child import Child
from collections import defaultdict
import csv
import datetime


class convergencePatterns(object):
	def __init__(self):
		# Each defaultdict is used to store every pair, trio, and quartet of parameter convergence orders
		# found in the learners.
		self.pairDict = defaultdict(lambda: defaultdict(lambda: 0))
		self.trioDict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0)))
		self.quartetDict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0))))


	def writePairResults(outputFile):
		f = open(outputFile, 'a')
		try:
			writer = csv.writer(f)
			# Add the parameters that appear second in pairs to the top row
			writer.writerow( ('p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13') )

			# Add parameters that appear first in pairs to individual rows
			# followed by related pair results
			for i in range(1,14):
				print "nothing2"
				#writer.writerow( ('p'+i, self.pairDict[i][j] for j in range(1,14)) )
		finally:
			f.close()


	def writeResults(outputFile = ''):
		# If no ouput file names are given or the given filename doesn't end with csv, 
		#the function will write to files using a default name format
		if outputFile.endswith('csv'):
			writePairResults(outputFile)
		else:
			print 'No chosen filename or filename doesn\'t end with .csv.'
			print 'Writing to default filename'
			writePairResults('pairConvergenceResults-' + datetime.datetime.now().isoformat().replace(':', '.') + '.csv')


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
