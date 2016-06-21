import time
import random
import pickle
from Child import Child

def doesChildLearnGrammar(count, eChild, sentenceInfo, totalSentenceCount, totalConvergedChildren):
    start = time.time()

    while eChild.grammarLearned == False and eChild.sentenceCount < 100000:
        eChild.consumeSentence(random.choice(sentenceInfo))
        eChild.setParameters()
        eChild.sentenceCount += 1


    eChild.totalTime = time.time() - start
    
    if eChild.grammarLearned:
        totalSentenceCount += eChild.sentenceCount
        totalConvergedChildren += 1
        
        timeFile = open('/home/malancas/Programming/Hunter/research/timeResults.txt','w')
        timeFile.write('eChild #' + count + " " + eChild.totalTime)
        timeFile.close()
    else:
        nonConvergedFile = open('/home/malancas/Programming/Hunter/research/nonConverged.txt','w')
        nonConvergedFile.write('eChild#' + count + ' ' + eChild.grammar)
        nonConvergedFile.close()

    return eChild


def printResults(childList, totalConvergedChildren, totalSentenceCount):
    print "Percentage of converged children: ", totalConvergedChildren / 100, "%"
    print "Average sentence count of converged children: ", (totalSentenceCount / totalConvergedChildren)

def main():

    infoFile = open('EngFrJapGerm.txt','rU') # 0001001100011
    sentenceInfo = infoFile.readlines()
    infoFile.close()
    
    englishSentences = []
    for i in range(0, len(sentenceInfo)):
        if sentenceInfo[i][:3] == "611":
            englishSentences.append(i)

    totalSentenceCount = 0
    totalConvergedChildren = 0
    childList = []

    for i in range(0,99):
        count = i
        childList.append(count, doesChildLearnGrammar(Child(), englishSentences, totalSentenceCount, totalConvergedChildren))

    printResults(childList, totalConvergedChildren, totalSentenceCount)    

if __name__ == '__main__':
    start = time.time() 
    main()
    end = time.time() - start
    print "Time to complete:", end