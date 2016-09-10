from .. import Child


c = Child.Child()

def test_haveParametersChanged():
	# Set up initial, relevant data in Child instance
	c.oldGrammar = [0,0,0,0,0,1,1,1,1,1,0,0,0]
	c.grammar = [0,0,0,0,0,1,1,1,1,1,0,0,0]
	c.timeCourseVector = [[1,i] for i in range(1,14)]

	c.haveParametersChanged(5)

	# Assert that none of data has changed after
	# the function has run
	assert c.oldGrammar == [0,0,0,0,0,1,1,1,1,1,0,0,0]
	assert c.grammar == [0,0,0,0,0,1,1,1,1,1,0,0,0]
	assert c.timeCourseVector == [[1,i] for i in range(1,14)]

	# This grammar is the opposite of the original
	# and should cause the oldGrammar and timeCourseVector
	# to change after running haveParametersChanged
	c.grammar = [1,1,1,1,1,0,0,0,0,0,1,1,1]

	c.haveParametersChanged(6)

	# Assert oldGramar, grammar, and timeCourseVector
	# have changed accordingly
	assert c.oldGrammar == [1,1,1,1,1,0,0,0,0,0,1,1,1]
	assert c.grammar == [1,1,1,1,1,0,0,0,0,0,1,1,1]
	assert c.timeCourseVector == [[6,i] for i in range(1,14)]

	c.grammar = [0,1,1,1,1,0,0,0,0,0,1,1,1]

	c.haveParametersChanged(10)

	assert c.oldGrammar == [0,1,1,1,1,0,0,0,0,0,1,1,1]
	assert c.grammar == [0,1,1,1,1,0,0,0,0,0,1,1,1]
	temp1 = [[10,1]]
	temp2 = [[6,i] for i in range(2, 14)]
	assert c.timeCourseVector == temp1 + temp2


# Test various combinations of lists
# and values to draw out border cases
def test_findIndex():
	sampleList = [0,0,0]
	assert c.findIndex([0,0,0], 0) == 0
	assert c.findIndex([0,0,0], 0.01) == -1
	assert c.findIndex([0,0,434], 434) == 2
	assert c.findIndex([0,0,434], 435) == -1
	assert c.findIndex([0,0,434], 433) == -1


def test_isQuestion():
	c.infoList = [584, 'Q', 'Adv S Aux Never Verb']
	assert c.isQuestion()

	c.infoList = [584, 'Q ', 'Adv S Aux Never Verb']
	assert not c.isQuestion()

	c.infoList = [584, 'q', 'Adv S Aux Never Verb']
	assert not c.isQuestion()

	c.infoList = [584, "Q", 'Adv S Aux Never Verb']
	assert c.isQuestion()


def test_isImperative():
	c.infoList = [584, 'IMP', 'Adv S Aux Never Verb']
	assert c.isImperative()

	c.infoList = [584, 'IMp', 'Adv S Aux Never Verb']
	assert not c.isImperative()

	c.infoList = [584, '  IMP', 'Adv S Aux Never Verb']
	assert not c.isImperative()

	c.infoList = [584, 'imp', 'Adv S Aux Never Verb']
	assert not c.isImperative()

	c.infoList = [584, "IMP", 'Adv S Aux Never Verb']
	assert c.isImperative()


def test_isDeclarative():
	c.infoList = [584, 'DEC', 'Adv S Aux Never Verb']
	assert c.isDeclarative()

	c.infoList = [584, 'DEc', 'Adv S Aux Never Verb']
	assert not c.isDeclarative()

	c.infoList = [584, '  DEC', 'Adv S Aux Never Verb']
	assert not c.isDeclarative()

	c.infoList = [584, 'dec', 'Adv S Aux Never Verb']
	assert not c.isDeclarative()

	c.infoList = [584, "DEC", 'Adv S Aux Never Verb']
	assert c.isDeclarative()


def test_setSubjPos():
	# Since '01' and 'S' don't appear in the infoList.
	# grammar[0] will remain '0'
	c.infoList = [584, "DEC", 'Adv S Aux Never Verb']
	c.sentence = c.infoList[2].split()
	c.grammar = "0 1 0 0 0 0 1 0 0 0 1 0 1".split()
	assert c.grammar[0] == '0'
	c.setSubjPos()
	assert c.grammar[0] == '0'

	# '01' and 'S' are both in infoList[2] but since
	# '01' is in the initial position, grammar[0]
	# won't change
	c.infoList = [584, "DEC", '01 S Aux Never Verb']
	c.sentence = c.infoList[2].split()
	assert c.grammar[0] == '0'
	c.setSubjPos()
	assert c.grammar[0] == '0'

	# grammar[0] will change since both are present
	# and 01 isn't in the initial spot but appears
	# before S
	c.infoList = [584, "DEC", 'Aux O1 S Never Verb']
	c.sentence = c.infoList[2].split()
	assert c.grammar[0] == '0'
	c.setSubjPos()
	assert c.grammar[0] == '1'

	# S and 01 are in the wrong order, therefore
	# grammar[0] won't change
	c.grammar[0] = '0'
	c.infoList = [584, "DEC", 'Aux S O1 Never Verb']
	c.sentence = c.infoList[2].split()
	assert c.grammar[0] == '0'
	c.setSubjPos()
	assert c.grammar[0] == '0'

	# Neither S or 01 appear in infoList[2]
	c.infoList = [584, "DEC", 'Aux Never Verb']
	c.sentence = c.infoList[2].split()
	assert c.grammar[0] == '0'
	c.setSubjPos()
	assert c.grammar[0] == '0'

	# Only 01 appears in infoList[2]
	c.infoList = [584, "DEC", 'Aux O1 Never Verb']
	c.sentence = c.infoList[2].split()
	assert c.grammar[0] == '0'
	c.setSubjPos()
	assert c.grammar[0] == '0'

	c.infoList = [584, "DEC", 'Aux O1 Never S Verb']
	c.sentence = c.infoList[2].split()
	assert c.grammar[0] == '0'
	c.setSubjPos()
	assert c.grammar[0] == '1'

	c.infoList = [584, "DEC", 'Aux Never Verb O1 S']
	c.sentence = c.infoList[2].split()
	c.grammar[0] = '0'
	c.setSubjPos()
	assert c.grammar[0] == '1'


def test_noSubjPos():
	# grammar[0] won't change since 
	# S appears after O1
	c.infoList = [584, "DEC", 'Aux Never Verb O1 S']
	c.sentence = c.infoList[2].split()
	c.grammar[0] = '0'
	c.noSubjPos()
	assert c.grammar[0] == '0'