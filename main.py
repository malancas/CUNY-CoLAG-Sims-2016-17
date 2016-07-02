import time
from Child import Child
from runSimulation import runSimulation


def main():
    open('German_results_100_2.csv', 'w').close()
    runSim1 = runSimulation()

    infoFile = open('EngFrJapGerm.txt','rU') # 0001001100011
    runSim1.sentenceInfo = infoFile.readlines()
    infoFile.close()

    #French=584, English=611, German=2253, Japanese=3856
    runSim1.makeSelectedSentenceList('2253')
    #print "selected sentences: ", len(runSim1.selectedSentences)

    runSim1.runSimulation(100)
    print "Finished \n"

    runSim1.printResults(100)    

if __name__ == '__main__':
    start = time.time() 
    main()
    end = time.time() - start
    print "Time to complete:", end