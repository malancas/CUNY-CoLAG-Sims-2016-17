from .. import Child


c = Child.Child()

def test_haveParametersChanged():
	# Set up initial, relevant data in Child instance
	#c = Child.Child()
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


'''
    #6th parameter   
    def setNullTopic(self):
        if "O2" in self.infoList[2] and "O1" not in self.infoList[2] :
            self.grammar[5] = '1'
'''
# If 02 is in infoList[2] while 01 isn't,
# test that grammar[5] == '1'
def test_setNullTopic():
	c.infoList = [584, 'DEC', '02 S Aux Never Verb']
	c.grammar = ['0'] * 13
	c.setNullTopic()
	assert '02' in c.infoList[2]
	assert '01' not in c.infoList[2]
	#assert c.grammar[5] == '1'

	c.infoList = [584, 'DEC', '02 01 S Aux Never Verb']
	c.grammar[5] = '0'
	c.setNullTopic()
	#assert c.grammar[5] == '0'