from Child import Child

# Calculates the percentage that part
# represents of whole
def percentage(num, total):
  return 100 * float(num)/float(total)


def printConvergencePairs(pairDict):
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
def findQuartetConvergencePatterns(quartetDict, sortedTCV, i, j, m):
	firstParm = sortedTCV[i][1]
	secondParm = sortedTCV[j][1]
	thirdParm = sortedTCV[m][1]

	if not firstParm in quartetDict:
		quartetDict[firstParm] = {secondParm : {thirdParm : {}}}

	elif not secondParm in quartetDict[firstParm]:
		quartetDict[firstParm][secondParm] = {thirdParm : {}}
	
	elif not thirdParm in quartetDict[firstParm][secondParm]:
		quartetDict[firstParm][secondParm][thirdParm] = {}

	# Check the remaining elements of sortedTCV for different combinations
	for x in range(m + 1, 13):
		fourthParm = sortedTCV[x][1]
		
		if not fourthParm in quartetDict[firstParm][secondParm][thirdParm]:			
			quartetDict[firstParm][secondParm][thirdParm][fourthParm] = 1
		else:
			quartetDict[firstParm][secondParm][thirdParm][fourthParm] += 1


# Will check for different sentence convergence threesome
# combinations exist. Different combinations are added to trioDict
# if they don't appear, otherwise the count within their corresponding
# dictionary entry is incremented
def findTrioConvergencePatterns(trioDict, quartetDict, sortedTCV, i, j):
	firstParm = sortedTCV[i][1]
	secondParm = sortedTCV[j][1]

	if not firstParm in trioDict:
		trioDict[firstParm] = {secondParm : {}}
	elif not secondParm in trioDict[firstParm]:
		trioDict[firstParm][secondParm] = {}

	for m in range(j + 1, 13):
		thirdParm = sortedTCV[m][1]

		if not thirdParm in trioDict[firstParm][secondParm]:
			trioDict[firstParm][secondParm][thirdParm] = 1
		else:
			trioDict[firstParm][secondParm][thirdParm] += 1
		
		findQuartetConvergencePatterns(quartetDict, sortedTCV, i, j, m)

# Will track the different convergence patterns (the order in which each parameter converges)
# that appear in a learner's time course vector.
# Currently, it will track pairs, triplets, and quartets of parameter combinations
def findConvergencePatterns(childList, convergencePairs):
	# The dictionary will store the stats describing
	# order of parameter convergence
	# Replace with defaultdict?
	parameterConvergenceTrios = {}
	parameterConvergenceQuartets = {}

	for child in childList:
		# Sort the learner's timeCourseVector based on the convergence
		# time of each parameter
		sortedTCV = sorted(child.timeCourseVector, key=lambda parameter: parameter[0])
		assert(len(sortedTCV) == 13)

		# Checks if key value pairs exist for each possible pairing in the current
		# sorted time course vector. If not, a pair is made and a count recording
		# the number of times the ordering appears in every learner. If the pair
		# already exists, the count is incremented
		for i in range(0, 12):
			for j in range(i+1, 13):
				firstParm = sortedTCV[i][1]
				secondParm = sortedTCV[j][1]

				if not firstParm in convergencePairs:
					convergencePairs[firstParm] = {secondParm : 1}
				elif not secondParm in convergencePairs.get(firstParm):
					convergencePairs.get(firstParm)[secondParm] = 1
				else:
					convergencePairs[firstParm][secondParm] += 1

				findTrioConvergencePatterns(parameterConvergenceTrios, parameterConvergenceQuartets, sortedTCV, i, j)