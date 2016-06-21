import time
import random
import pickle
from Child import Child

MAX_SENTENCE_COUNT = 1000000

def doesChildLearnGrammar(eChild, sentenceInfo, totalSentenceCount, totalConvergedChildren):
    start = time.time()
    while not eChild.grammarLearned and eChild.sentenceCount < MAX_SENTENCE_COUNT:
        eChild.consumeSentence(random.choice(sentenceInfo))
        eChild.setParameters()
        eChild.sentenceCount += 1

    eChild.totalTime = time.time() - start
    
    if eChild.grammarLearned:
        totalSentenceCount += eChild.sentenceCount
        totalConvergedChildren += 1

    return eChild

def printResults(childList, totalConvergedChildren, totalSentenceCount):
    print "Percentage of converged children: ", totalConvergedChildren / 100, "%"
    print "Average sentence count of converged children: ", (totalSentenceCount / totalConvergedChildren)


def main():

    infoFile = open('EngFrJapGerm.txt','rU') # 0001001100011
    sentenceInfo = infoFile.readlines()
    infoFile.close()
    #print ''.join('v{}: {}'.format(v, i) for v, i in enumerate(sentenceInfo))
    eChild = Child()
    
    eChild.sentenceCount = 0
    
    while eChild.grammarLearned == False and eChild.sentenceCount < 100000:
        eChild.consumeSentence(random.choice(sentenceInfo))
        eChild.setParameters()
        eChild.sentenceCount += 1

    print eChild.grammar
    print eChild.expectedGrammar
    print eChild.sentenceCount
    

if __name__ == '__main__':
    start = time.time() 
    main()
    end = time.time() - start
    print "Time to complete:", end