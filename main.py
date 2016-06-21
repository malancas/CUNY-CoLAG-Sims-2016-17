import time
import random
import pickle
from Child import Child

def doesChildLearnGrammar(eChild):
    start = time.time()
    while eChild.grammarLearned == False and eChild.count < MAX_SENTENCE_COUNT :
        eChild.consumeSentence(random.choice(sentenceInfo))
        eChild.setParameters()

        #if eChild.sentenceCount == MAX_SENTENCE_COUNT:
        #    eChild.grammarLearned = True

    eChild.totalTime = time.time() - start
    return eChild

def printResults(childList):
    totalConvergedChildren = 0
    totalSentenceCount = 0
    for ec in childList:
        if ec.grammarLearned:
            totalConvergence += 1
            totalSentenceCount = ec.sentenceCount
    print "Percentage of converged children: ", totalConvergedChildren / 100, "%"
    print "Average sentence count of converged children: ", (totalSentenceCount / totalConvergedChildren)


def main():
    MAX_SENTENCE_COUNT = 1000000

    infoFile = open('/home/malancas/Programming/Hunter/research/EngFrJapGerm.txt','rU') # 0001001100011
    sentenceInfo = infoFile.readlines()
    infoFile.close()
    #print ''.join('v{}: {}'.format(v, i) for v, i in enumerate(sentenceInfo))
    childList = []
    
    for in in range(0,99):
        childList.append(doesChildLearnGrammar(Child()))
    
    
    errFile = open('/home/malancas/Programming/Hunter/research/error.txt','w')
    errFile.write("Japanese: " + str(eChild.sentenceCount))
    errFile.close()
    

if __name__ == '__main__':
    start = time.time() 
    main()
    end = time.time() - start
    print "Time to complete:", end