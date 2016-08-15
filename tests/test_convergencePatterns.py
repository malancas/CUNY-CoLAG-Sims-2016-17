from .. import convergencePatterns
import unittest
import random
from .. import Child
import pytest


'''
Checks that there is a value greater than zero
within all possible dictionary key pairs.
The function will check for pairings with currKey and
any paired key must appear after it in timeCourseVector
'''
def checkForKeyPairs(currKey, currKeyIndex, timeCourseVector, dict):
	for i in range(2, 13):
		secondKey = timeCourseVector[i][1]
		if i > currKeyIndex:
			assert dict[currKey][secondKey] > 0
		else:
			with pytest.raises(KeyError):
				dict[currKey][secondKey] > 0

def test_pairConvergenceNonExistentDictEntry():
	c1 = Child.Child()
	c1.timeCourseVector = [[3, 5], [4, 1], [10, 12], [11, 11], [14, 2], [14, 8], [24, 3], [26, 6], [30, 4], [31, 9], [56, 7], [60, 13], [61, 10]]
	sampleChildList = [c1]
	sampleDict = {}

	convergencePatterns.findConvergencePatterns(sampleChildList, sampleDict)
	
	''' 
	After running findConvergencePatterns, sampleDict should contain a number of key
	and inner key pairs. The outer key should always appear before the inner key in the
	sample time course vector
	Every parameter is checked in the for loop 
	'''
	for i in range(0, 13):
		checkForKeyPairs(c1.timeCourseVector[i][1], i, c1.timeCourseVector, sampleDict)


def test_nonExistentDictEntry():
	'''
	Create a time course vector for testing.
	The first element of each inner list represents the
	time at which the parameter converged. The second 
	element indicates the specific parameter by number
	'''
	sampleTCV = [[3, 5], [4, 1], [10, 12], [11, 11], [14, 2], [14, 8], [24, 3], [26, 6], [30, 4], [31, 9], [56, 7], [60, 13], [61, 10]]

	# Make a sample dictionary, that will contain a number of dictionaries
	# of varying levels
	sampleDict = {5 : {}, 12 : {11 : {}, 4 : {}}, 2 : {}, 6 : {1 : {8 : {}}}}

	convergencePatterns.findQuartetConvergencePatterns(sampleDict, sampleTCV, 1, 11, 3)
	print sampleDict[1]
	#assert(sampleDict.haskey(5).)
	#assert (sampleDict.get(1).get(11).get(3).get(6) > 0)

def randomTesting():
	# Create a time course vector for testing.
	# The first element of each inner list represents the
	# time at which the parameter converged. The second 
	# element indicates the specific parameter by number
	# The first element be random, inclusive number between one and five
	sampleTCV = []
	for i in range(1, 14):
		print "hello"
		#sampleTCV.append([randit(1, 5), i])

	# Make a sample dictionary, that will contain a number of dictionaries
	# of varying levels
	#sampleDict = {randit(1, 5) : {}, randit(1, 5) : {randit(1, 5) : {randit(1, 5) : {}}}, randit(1, 5) : {randit(1, 5) : {}}}

	#findQuartetConvergencePatterns(sampleDict, sampleTCV, 1, 11, 3)