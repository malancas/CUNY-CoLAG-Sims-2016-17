from .. import runSimulation
import pytest


def test_makeSelectedSentences():
	infoFile = open('EngFrJapGerm.txt','rU')
	runSim1 = runSimulation.runSimulation(infoFile.readlines())
	infoFile.close()

    # These four ids are present in EngFrJapGerm: French=584, English=611, German=2253, Japanese=3856
	runSim1.makeSelectedSentenceList('611')
	assert runSim1.selectedSentences
	assert len(runSim1.selectedSentences) == 540

	runSim1.selectedSentences = []
	runSim1.makeSelectedSentenceList('584')
	assert len(runSim1.selectedSentences) == 756

	runSim1.selectedSentences = []
	runSim1.makeSelectedSentenceList('2253')
	assert len(runSim1.selectedSentences) == 1134

	runSim1.selectedSentences = []
	runSim1.makeSelectedSentenceList('3856')
	assert len(runSim1.selectedSentences) == 1092

	runSim1.selectedSentences = []
	runSim1.makeSelectedSentenceList('612')
	assert not runSim1.selectedSentences

	runSim1.selectedSentences = []
	runSim1.makeSelectedSentenceList('')
	assert not runSim1.selectedSentences