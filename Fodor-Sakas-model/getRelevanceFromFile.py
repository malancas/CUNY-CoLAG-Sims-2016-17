'''
COLAG_2011_ids.txt.   The format is:

grammID \t sentID \t structID

I need a new file COLAG_2011_ids_relevance.txt. The format should be:

grammID \t sentID \t structID \t relevanceString

What I'd first do is create a dictionary from COLAG_20011_ids.txt where:

key:StructID; value:set( all 13 character grammar bit strings that generate the structID )

# your code would have to convert GrammIDs to bitstrings; there's probably a nifty
#   way to do this in Python, I know the other direction x = int("100101001001", 2), and 
#    I know there's a bin() function but you would have to pad leading 0's so that there are 
#    strings of exactly 13 characters.

Then I'd create another dictionary:

key: structID ; value string

Run your function getRelevanceString using the first dictionary, and save the resulting relevance string in the second dictionary.

Then finally use the second dictionary to create the output file by appending the relevance string assigned to each structID to the original COLAG_2011_ids.txt data.
'''
idDict = {}
with open('COLAG_2011_ids.txt', "r") as infile:
    content = infile.readlines()
    for line in content:
        line.split('\t')
