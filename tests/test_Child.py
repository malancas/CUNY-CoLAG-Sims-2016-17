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
        c.infoList = [611, 'IMP', ['0','0','0']]
	assert c.findIndex('0') == 0
	assert c.findIndex('0.01') == -1

	c.infoList[2] = ['0','0','434']
	assert c.findIndex('434') == 2
	assert c.findIndex('435') == -1
	assert c.findIndex('433') == -1


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


# c.grammar[0] will be set to '1' if O1 appears in any index
# other than 0 and S appears after it in c.sentence 
def test_setSubjPos():
	# Since '01' and 'S' don't appear in the infoList.
	# grammar[0] will remain '0'
	c.infoList = [584, "DEC", 'Adv S Aux Never Verb']
	c.sentence = c.infoList[2].split()
	c.grammar = [0,0,0,0,0,0,1,0,0,0,1,0,1]
	assert c.grammar[0] == 0
	c.setSubjPos()
	assert c.grammar[0] == 0

	# '01' and 'S' are both in infoList[2] but since
	# '01' is in the initial position, grammar[0]
	# won't change
	c.infoList = [584, "DEC", '01 S Aux Never Verb']
	c.sentence = c.infoList[2].split()
	assert c.grammar[0] == 0
	c.setSubjPos()
	assert c.grammar[0] == 0

	# grammar[0] will change since both are present
	# and 01 isn't in the initial spot but appears
	# before S
	c.infoList = [584, "DEC", 'Aux O1 S Never Verb']
        c.infoList[2] = c.infoList[2].split()
	assert c.grammar[0] == 0
	c.setSubjPos()
	assert c.grammar[0] == 1

	# S and 01 are in the wrong order, therefore
	# grammar[0] won't change
	c.grammar[0] = 0
	c.infoList = [584, "DEC", 'Aux S O1 Never Verb']
	c.infoList[2] = c.infoList[2].split()
	assert c.grammar[0] == 0
	c.setSubjPos()
	assert c.grammar[0] == 0

	# Neither S or 01 appear in infoList[2]
	c.infoList = [584, "DEC", 'Aux Never Verb']
	c.infoList[2] = c.infoList[2].split()
	assert c.grammar[0] == 0
	c.setSubjPos()
	assert c.grammar[0] == 0

	# Only 01 appears in infoList[2]
	c.infoList = [584, "DEC", 'Aux O1 Never Verb']
	c.infoList[2] = c.infoList[2].split()
	assert c.grammar[0] == 0
	c.setSubjPos()
	assert c.grammar[0] == 0

	c.infoList = [584, "DEC", 'Aux O1 Never S Verb']
	c.infoList[2] = c.infoList[2].split()
	assert c.grammar[0] == 0
	c.setSubjPos()
	assert c.grammar[0] == 1

	c.infoList = [584, "DEC", 'Aux Never Verb O1 S']
        c.infoList[2] = c.infoList[2].split()
	c.grammar[0] = 0
	c.setSubjPos()
	assert c.grammar[0] == 1


# c.grammar[0] will be set to '0'
# if O1 appears before S in sentence
# in any index
def test_noSubjPos():
	# grammar[0] won't change since 
	# S appears after O1
	c.infoList[2] = 'Aux Never Verb O1 S'.split()
	c.grammar[0] = 1
	c.noSubjPos()
	assert c.grammar[0] == 1

	c.infoList[2] = 'S Aux Never Verb O1'.split()
	c.noSubjPos()
	assert c.grammar[0] == 0

	c.grammar[0] = 1
	c.infoList[2] = 'Aux Never Verb S O1'.split()
	c.noSubjPos()
	assert c.grammar[0] == 0

	c.grammar[0] = 1
	c.infoList[2] = 'Aux Never Verb S'.split()
	c.noSubjPos()
	assert c.grammar[0] == 1

	c.infoList[2] = 'Aux Never Verb O1'.split()
	c.noSubjPos()
	assert c.grammar[0] == 1


'''
c.grammar[1] will be set to '1' if either scenario occurs:
(1) If O3 followed directly by P appears in c.sentence
and O3 is in any index position other than 0

(2) If c.infoList[1] == 'IMP' and Verb followed directly
by O1 appear in c.sentence
'''
def test_setHead():
        # Testing for scenario one
	c.infoList[2] = 'Aux Never Verb O3 P'.split()
	c.grammar[1] = 0
	c.setHead()
	assert c.grammar[1] == 1

	c.infoList[2] = 'Aux Never O3 Verb P'.split()
	c.grammar[1] = 0
	c.setHead()
	assert c.grammar[1] == 0

	c.infoList[2] = 'O3 P Aux Never Verb'.split()
	c.setHead()
	assert c.grammar[1] == 0

	c.infoList[2] = 'O3 Aux P Never Verb'.split()
	c.setHead()
	assert c.grammar[1] == 0


'''
c.grammar[1] will be set to '0' if either scenario occurs
(1) If O3 and P both appear in c.infoList[2] and the index
of P is greater than zero and lower than O3's

(2) The sentence type is imperative and both O1 and Verb
appear in c.infoList[2]. Verb must directly follow O1.
'''
def test_noHead():
        # Testing for scenario 1
        c.infoList[2] = 'Aux Never Verb O3 P'.split()
	c.grammar[1] = 1
	c.noHead()
	assert c.grammar[1] == 1

        c.infoList[2] = 'Aux Never Verb P O3'.split()
	c.grammar[1] = 1
	c.noHead()
	assert c.grammar[1] == 0

	c.infoList[2] = 'P O3 Aux Never Verb'.split()
	c.grammar[1] = 1
	c.noHead()
	assert c.grammar[1] == 1

	c.infoList[2] = 'Aux P Never Verb O3'.split()
	c.noHead()
	assert c.grammar[1] == 1

	c.infoList[2] = 'Aux P O3 Never Verb'.split()
	c.noHead()
	assert c.grammar[1] == 0

        # Testing for scenario 2
        c.grammar[1] = 1
        c.infoList[1] = 'IMP'
	c.infoList[2] = 'Verb Aux O1 P'.split()
	c.noHead()
	assert c.grammar[1] == 1

        c.infoList[1] = 'DEC'
	c.infoList[2] = 'Aux Verb O1'.split()
	c.noHead()
	assert c.grammar[1] == 1

        c.infoList[1] = 'IMP'
	c.infoList[2] = 'Aux Verb O1 P'.split()
	c.noHead()
	assert c.grammar[1] == 0


# Tests whether S, O1, O2, O3, or Adv appears
# first in c.infoList[2]
def test_containsTopicalizable():
        c.infoList[2] = 'O1 Aux Verb P'.split()
        assert c.containsTopicalizable()
        
        c.infoList[2] = 'O2 Aux Verb P'.split()
        assert c.containsTopicalizable()

        c.infoList[2] = 'O3 Aux Verb P'.split()
        assert c.containsTopicalizable()

        c.infoList[2] = 'S Aux Verb P'.split()
        assert c.containsTopicalizable()

        c.infoList[2] = 'Adv Aux Verb P'.split()
        assert c.containsTopicalizable()

        c.infoList[2] = 'P O1 O2 O3 S Adv'.split()
        assert not c.containsTopicalizable()

        c.infoList[2] = 'O1 Adv Aux Verb P'.split()
        assert c.containsTopicalizable()


'''
If the sentence is a question check whether
(1) 'ka' is in infoList[2]

(2) 'ka' isn't in infoList[2] while 'Aux' is
'''
def test_setHeadCP():
        # Testing for scenario #1
        c.grammar[2] = 0
        c.infoList[1] = 'Q'
        c.infoList[2] = 'O1 Adv Aux Verb P ka'.split()
        c.setHeadCP()
        assert c.grammar[2] == 1

        c.grammar[2] = 0
        c.infoList[2] = 'O1 Adv ka Verb P Aux'.split()
        c.setHeadCP()
        assert c.grammar[2] == 0

        c.infoList[2] = 'O1 Adv ka Verb P'.split()
        c.setHeadCP()
        assert c.grammar[2] == 0

        # Testing for scenario #2
        c.infoList[2] = 'O1 Adv Verb P Aux'.split()
        c.setHeadCP()
        assert c.grammar[2] == 1

        c.grammar[2] = 0
        c.infoList[1] = 'IMP'
        c.infoList[2] = 'O1 Adv Verb P ka'.split()
        c.setHeadCP()
        assert c.grammar[2] == 0

        c.infoList[2] = 'O1 Adv Verb P Aux'.split()
        c.setHeadCP()
        assert c.grammar[2] == 0


'''
Grammar[1] is set to 0 if both O3 and P
are in the sentence and P isn't the first element in the
sentence but appears immediately before O3 in the sentence

Grammar[1] is set to 1 if the sentence is imperative
and 01 and Verb are in the sentence. Additionally,
Verb must appear immediately before O1
'''
def test_noHead():
        # Testing for scenario #1
        c.grammar[1] = 1
        c.infoList[1] = 'Q'
        c.infoList[2] = 'O3 Adv Verb P Aux'.split()
        c.noHead()
        assert c.grammar[1] == 1

        c.infoList[2] = 'P O3 Adv Verb Aux'.split()
        c.noHead()
        assert c.grammar[1] == 1

        c.infoList[2] = 'Adv P O3 Verb Aux'.split()
        c.noHead()
        assert c.grammar[1] == 0

        c.grammar[1] = 1
        c.infoList[2] = 'Adv P Verb O3 Aux'.split()
        c.noHead()
        assert c.grammar[1] == 1

        # Testing for scenario #2
        c.grammar[1] = 0
        c.infoList[1] = 'IMP'
        c.infoList[2] = 'Adv P Verb O1 Aux'.split()
        c.noHead()
        assert c.grammar[1] == 1

        c.grammar[1] = 0
        c.infoList[2] = 'Adv P Verb Aux O1'.split()
        c.noHead()
        assert c.grammar[1] == 0

        c.infoList[2] = 'Adv P O1 Verb Aux'.split()
        c.noHead()
        assert c.grammar[1] == 0
