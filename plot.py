from Child import Child
import sys

def percentage(part, whole):
  return 100 * float(part)/float(whole)


def findProbabilities(childList, maxLearners):
	twoParameters = [[0] * 13] * 13

	for child in childList:
		# Sort the learner's timeCourseVector based on the convergence
		# time of each parameter
		sortedTCV = sorted(child.timeCourseVector, key=lambda parameter: parameter[0])
		assert(len(sortedTCV) == 13)

		for i in range(0, 12):
			for j in range(i+1, 13):
				twoParameters[sortedTCV[i][1] - 1][sortedTCV[j][1] - 1] += 1				

	#sys.exit(0)

	for m in range(0, 13):
		for n in range(0, 13):
			if (m != n):
				print "P({0} < {1})".format(m, n)
				print twoParameters[m][n]
				print percentage(twoParameters[m][n], maxLearners), "%"
				print '\n'