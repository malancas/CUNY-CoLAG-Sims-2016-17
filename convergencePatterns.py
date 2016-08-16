from Child import Child
from collections import defaultdict


class convergencePatterns(object):
	def __init__(self):
		self.pairDict = defaultdict(lambda: defaultdict(lambda: 0))
		self.trioDict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0)))
		self.quartetDict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0))))


	def percentage(self, num, total):
  		return 100 * float(num)/float(total)


	def printConvergencePairs(self, pairDict):
		for m in range(0, 13):
			for n in range(0, 13):
				if (m != n):
					try:
						print "P({0} < {1})".format(m, n)
						print parameterConvergencePairs[m][n]
						print '\n'
					except KeyError:
						print "."


	# Will check for different sentence convergence foursome
	# combinations exist. Different combinations are added to quarterDict
	# if they don't appear, otherwise the count within their corresponding
	# dictionary entry is incremented
	def findQuartetConvergencePatterns(self, sortedTCV, i, j, m):
		firstParm = sortedTCV[i][1]
		secondParm = sortedTCV[j][1]
		thirdParm = sortedTCV[m][1]

		# Check the remaining elements of sortedTCV for different combinations
		for x in range(m + 1, 13):
			fourthParm = sortedTCV[x][1]
		
			quartetDict[firstParm][secondParm][thirdParm][fourthParm] += 1


	# Will check for different sentence convergence threesome
	# combinations exist. Different combinations are added to trioDict
	# if they don't appear, otherwise the count within their corresponding
	# dictionary entry is incremented
	def findTrioConvergencePatterns(self, sortedTCV, i, j):
		firstParm = sortedTCV[i][1]
		secondParm = sortedTCV[j][1]

		for m in range(j + 1, 13):
			thirdParm = sortedTCV[m][1]

			trioDict[firstParm][secondParm][thirdParm] += 1

			findQuartetConvergencePatterns(sortedTCV, i, j, m)


	# Checks if key value pairs exist for each possible pairing in the current
	# sorted time course vector. If not, a pair is made and a count recording
	# the number of times the ordering appears in every learner. If the pair
	# already exists, the count is incremented
	def findConvergencePairs(self, sortedTCV):
		for i in range(0, 12):
			for j in range(i+1, 13):
				firstParm = sortedTCV[i][1]
				secondParm = sortedTCV[j][1]

				pairDict[firstParm][secondParm] += 1

				findTrioConvergencePatterns(sortedTCV, i, j)	


	# Will track the different convergence patterns (the order in which each parameter converges)
	# that appear in a learner's time course vector.
	# Currently, it will track pairs, triplets, and quartets of parameter combinations
	def findConvergencePatterns(self, childList):
		# The dictionary will store the stats describing
		# order of parameter convergence
		# Replace with defaultdict?

		for child in childList:
			# Sort the learner's timeCourseVector based on the convergence
			# time of each parameter
			sortedTCV = sorted(child.timeCourseVector, key=lambda parameter: parameter[0])
			assert(len(sortedTCV) == 13)

			findConvergencePairs(sortedTCV)
