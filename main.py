import time
import random
import pickle
from Child import Child
from runChildren import runChildren


def main():
    runChildren1 = runChildren()

    infoFile = open('EngFrJapGerm.txt','rU') # 0001001100011
    runChildren1.sentenceInfo = infoFile.readlines()
    infoFile.close()

    #611 is the English id
    runChildren1.makeSelectedSentenceList('611')

    runChildren1.runSimulation(99)

    runChildren1.printResults()    

if __name__ == '__main__':
    start = time.time() 
    main()
    end = time.time() - start
    print "Time to complete:", end