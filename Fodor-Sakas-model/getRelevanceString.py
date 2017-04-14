def getRelevanceString(gSet, n):
    if not gSet: return ''

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
        if (bitStr.length != n):
            print("Strings in gSet must have length n")
            return None

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
