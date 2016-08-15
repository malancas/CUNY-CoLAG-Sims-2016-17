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
	for i in range(1, 13):
		secondKey = timeCourseVector[i][1]
		if i > currKeyIndex:
			assert dict[currKey][secondKey] > 0
		else:
			with pytest.raises(KeyError):
				dict[currKey][secondKey] > 0


'''
Checks that valid triple key groups are present in dict and that
the value is greater than zero
'''
def checkForKeyTrios(currKey, currKeyIndex, secondKey, secondKeyIndex, timeCourseVector, dict):
	assert currKeyIndex < secondKeyIndex
	for i in range(1, 13):
		thirdKey = timeCourseVector[i][1]
		if i > secondKeyIndex:
			assert dict[currKey][secondKey][thirdKey] > 0
		else:
			with pytest.raises(KeyError):
				dict[currKey][secondKey][thirdKey] > 0


'''
Checks that valid triple key groups are present in dict and that
the value is greater than zero
'''
def checkForKeyQuartets(currKey, currKeyIndex, secondKey, secondKeyIndex, thirdKey, thirdKeyIndex, timeCourseVector, dict):
	assert currKeyIndex < secondKeyIndex < thirdKeyIndex
	for i in range(1, 13):
		fourthKey = timeCourseVector[i][1]
		if i > thirdKeyIndex:
			assert dict[currKey][secondKey][thirdKey][fourthKey] > 0
		else:
			with pytest.raises(KeyError):
				dict[currKey][secondKey][thirdKey][fourthKey] > 0


'''
Runs findConvergencePatterns with a sample dictionarie and time course vector.
Afterwords, checkForKeyPairs will test the contents of sampleDict to see if 
appropriate key pairs and values were added. py.test should be used to run these
tests
'''
def test_convergencePairDictEntries():
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


'''
Create a time course vector for testing.
The first element of each inner list represents the
time at which the parameter converged. The second 
element indicates the specific parameter by number
'''
def test_convergenceTriosDictEntries():
	# Make a sample dictionary, that will contain a number of dictionaries
	# of varying levels, and a sample time course vector
	sampleTCV = [[3, 5], [4, 1], [10, 12], [11, 11], [14, 2], [14, 8], [24, 3], [26, 6], [30, 4], [31, 9], [56, 7], [60, 13], [61, 10]]
	sampleDict = {}

	convergencePatterns.findTrioConvergencePatterns(sampleDict, {}, sampleTCV, 0, 1)
	for i in range(0, 12):
		for j in range(i+1, 13):
			checkForKeyTrios(sampleTCV[i][1], i, sampleTCV[j][1], j, sampleTCV, sampleDict)


'''
Create a time course vector for testing.
The first element of each inner list represents the
time at which the parameter converged. The second 
element indicates the specific parameter by number
'''
def test_convergenceQuartetsDictEntries():
	# Make a sample dictionary, that will contain a number of dictionaries
	# of varying levels, and a sample time course vector
	sampleTCV = [[3, 5], [4, 1], [10, 12], [11, 11], [14, 2], [14, 8], [24, 3], [26, 6], [30, 4], [31, 9], [56, 7], [60, 13], [61, 10]]
	sampleDict = {}

	convergencePatterns.findQuartetConvergencePatterns(sampleDict, sampleTCV, 0, 1, 2)
	for i in range(0, 11):
		for j in range(i+1, 12):
			for k in range(j+1, 13):
				checkForKeyQuartets(sampleTCV[i][1], i, sampleTCV[j][1], j, sampleTCV[k][1], k, sampleTCV, sampleDict)


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