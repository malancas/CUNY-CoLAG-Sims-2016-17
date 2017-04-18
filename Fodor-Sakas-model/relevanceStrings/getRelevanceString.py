def getRelevanceString(gSet, n):
    if not gSet: return ''

    # Initialize each element in strDict to a dictionary that corresponds to the
    # index and value of each element in the first element of gSet
    strDict = []

    for b in enumerate(gSet[0]):
        strDict.append({b: 1})
    
    # Refstr is set to the first string and will change
    # after processing for strings
    refStr = gSet[0]

    # Keeps track of the indices where values differ between
    # the currently analyzed string and refStr
    diffIndices = []
    for i in range(1, len(gSet)):
        if (len(gSet[i]) != n):
            print("Strings in gSet must have length n")
            return None

        bitStr = gSet[i]
        for index, b in enumerate(bitStr):
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
        if len(diffIndices) == 1:
            refStr = refStr[:diffIndices[0]] + '~' + refStr[diffIndices[0]+1:]

        # If the number is greater than one,
        # then the differing indices is replaced with a '*'
        elif len(diffIndices) >= 1:
            for ind in diffIndices:
                refStr = refStr[:ind] + '*' + refStr[ind+1:]
                
        # diffIndices is emptied to use for the next string
        diffIndices = []

    return refStr
