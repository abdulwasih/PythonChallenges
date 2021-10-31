def missingnumber(inputlist):
    listcount = len(inputlist)
    sumoflist = (listcount*(listcount+1))/2
    sumofinputlist = sum(inputlist)
    missingelement = sumoflist - sumofinputlist
    return missingelement

    