from Child import Child
import sys

def percentage(part, whole):
  return float(part)/float(whole)

def findProbabilities(childList, maxLearners):
	twoParameters = [[0] * 13] * 13

	for child in childList:
		for i in range(0, 13):
			for j in range(0, 13):
				if (i != j) and (child.timeCourseVector[i][0] < [j][0]):
					twoParameters[i][j] += 1
					print "i: {0}, j: {1}".format(i, j)

	
	for m in range(0, 13):
		for n in range(0, 12):
			if (m != n):
				print "P({0} < {1})".format(m, n)
				print twoParameters[m][n]
				print percentage(twoParameters[m][n], maxLearners), "%"
				print '\n'
