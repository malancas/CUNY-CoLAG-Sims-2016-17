import time
import random
import pickle
from Child import Child

def doesChildLearnGrammar(eChild, sentenceInfo, totalSentenceCount, totalConvergedChildren):
    start = time.time()

    while eChild.grammarLearned == False and eChild.sentenceCount < 100000:
        eChild.consumeSentence(random.choice(sentenceInfo))
        eChild.setParameters()
        eChild.sentenceCount += 1


    eChild.totalTime = time.time() - start
    
    if eChild.grammarLearned:
        totalSentenceCount += eChild.sentenceCount
        totalConvergedChildren += 1


def printResults(childList, totalConvergedChildren, totalSentenceCount):
    print "Percentage of converged children: ", totalConvergedChildren / 100, "%"
    print "Average sentence count of converged children: ", (totalSentenceCount / totalConvergedChildren)


def main():

    infoFile = open('EngFrJapGerm.txt','rU') # 0001001100011
    sentenceInfo = infoFile.readlines()
    infoFile.close()
    eChild = Child()
    totalSentenceCount = 0
    totalConvergedChildren = 0

    doesChildLearnGrammar(eChild, sentenceInfo, totalSentenceCount, totalConvergedChildren)

    print eChild.grammar
    print eChild.expectedGrammar
    print eChild.sentenceCount
    

if __name__ == '__main__':
    start = time.time() 
    main()
    end = time.time() - start
    print "Time to complete:", end