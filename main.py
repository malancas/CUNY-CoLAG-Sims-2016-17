import time
import random
import pickle
from Child import Child


def main():
    MAX_SENTENCE_COUNT = 1000

    infoFile = open('/home/malancas/Programming/Hunter/research/EngFrJapGerm.txt','rU') # 0001001100011
    sentenceInfo = infoFile.readlines()
    infoFile.close()
    #print ''.join('v{}: {}'.format(v, i) for v, i in enumerate(sentenceInfo))
    eChild = Child()
    
    count = 0
    
    while eChild.grammarLearned == False :
        eChild.consumeSentence(random.choice(sentenceInfo))
       # print eChild.infoList
        eChild.setParameters()
        if count == 1000:
            eChild.grammarLearned = True
        count+=1
    print eChild.grammar
    print eChild.expectedGrammar
    print eChild.sentenceCount
    
    
    errFile = open('/home/malancas/Programming/Hunter/research/error.txt','w')
    errFile.write("Japanese: " + str(eChild.sentenceCount))
    errFile.close()
    

if __name__ == '__main__':
    start = time.time() 
    main()
    end = time.time() - start
    print "Time to complete:", end