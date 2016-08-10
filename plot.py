from Child import Child
import sys

# Calculates the percentage that part
# represents of whole
def percentage(num, total):
  return 100 * float(num)/float(total)


def findProbabilities(childList, maxLearners):
	# The dictionary will store the stats describing
	# order of parameter convergence
	parameterConvergence = {}

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
				if not i in parameterConvergence:
					parameterConvergence[i] = {j : 1}
				elif not j in parameterConvergence.get(i):
					parameterConvergence.get(i)[j] = 1
				else:
					parameterConvergence[i][j] += 1

	#sys.exit(0)


	for m in range(0, 13):
		for n in range(0, 13):
			if (m != n):
				try:
					print "P({0} < {1})".format(m, n)
					print parameterConvergence[m][n]
					print '\n'
				except KeyError:
					print "."
