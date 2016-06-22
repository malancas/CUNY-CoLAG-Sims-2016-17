import time
import random
import pickle
from Child import Child
from runSimulation import runSimulation


def main():
    runSim1 = runSimulation()

    infoFile = open('EngFrJapGerm.txt','rU') # 0001001100011
    runSim1.sentenceInfo = infoFile.readlines()
    infoFile.close()

    #611 is the English id
    runSim1.makeSelectedSentenceList('611')

    runSim1.runSimulation(100)
    print "Finished \n"

    runSim1.printResults(100)    

if __name__ == '__main__':
    start = time.time() 
    main()
    end = time.time() - start
    print "Time to complete:", end