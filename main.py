import time
from Child import Child
from runSimulation import runSimulation


def main():
    runSim1 = runSimulation()

    infoFile = open('EngFrJapGerm.txt','rU') # 0001001100011
    runSim1.sentenceInfo = infoFile.readlines()
    infoFile.close()

    #French=584, English=611, German=2253, Japanese=3856
    runSim1.makeSelectedSentenceList('2253')
    #print "selected sentences: ", len(runSim1.selectedSentences)

    runSim1.runSimulation(100000)
    print "Finished \n"

    runSim1.printResults(100000)    

if __name__ == '__main__':
    start = time.time() 
    main()
    end = time.time() - start
    print "Time to complete:", end