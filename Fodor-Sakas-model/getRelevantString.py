'''
def getRelevanceString (Gset, n)

# takes a Python set of bit strings of n characters (of 0 or 1), and 
# returns a single string (retStr) of n characters where each character retStr[i]
# is either a '0', '1', '*', or '~' where:
# a '0' means all the strings in Gset have a '0' in position i,
# a '1' means all the strings in Gset have a '1' in position i,
# a '~' means there exists a pair of strings in Gset that differ ONLY in position i, that is
#         there is a pair of string with Hamming distance of one that differ in position i
# a '*" otherwise

So for example consider the following Gset where each bitstring is n=4 characters long:
"1000"
"1101"
"1100"
"1001"

The function would return the string:

"1~0~"

Because all the strings in Gset have a '1' in position 0, and a '0' in position 2.
And Hamming("1000","1001") == 1 and differ in position 3, and
        Hamming("1101","1001") == 1 and differ in position 1

The function will be run about 60,000 times on Gsets of CoLAG grammar strings of length 13 where the Gsets can range from 2 to 3072 on average around 1,500 so a brute force approach (60,000 * 13 parameters * 1,500 = over a billion comparisons) might be too slow so keep an eye on efficiency.
'''
def getRelevanceString(gSet, n):
    # Initialize each element in strDict to a dictionary that corresponds to the
    # index and value of each element in the first element of gSet
    strDict = []

    for index, b in gSet[0]:
        strDict.append({b: 1})
    
    # Refstr is set to the first string and will change
    # after processing for strings
    refStr = gSet[0]

    # Keeps track of the indices where values differ between
    # the currently analyzed string and refStr
    diffIndices = []
    for (bitStr in range(1,gSet.length)):
        for index, b in bitStr:
            # Checks whether the current element in bitStr exists in strDict
            # at that index. If not, it is added and the corresponding
            # index is added to diffIndices
            if not b in strDict[index]:
                strDict[index][b] = 1
                diffIndices.append(index)
            else:
                strDict[index][b] += 1
        
        # If the number of differing indices is one,
        # then the differing index in refStr is replaced with a '~'
        if diffIndices.length() == 1:
            refStr[diffIndex[0]] = '~'

        # If the number is greater than one,
        # then the differing indices is replaced with a '*'
        elif diffIndeces.length() >= 1:
            for ind in diffIndices:
                refStr[ind] = '*'
                
        # diffIndices is emptied to use for the next string
        diffIndices = []

    return refStr
