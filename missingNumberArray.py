def missingnumber(inputlist):
    listcount = len(inputlist) +1
    sumoflist = (listcount*(listcount+1))/2
    sumofinputlist = sum(inputlist)
    missingelement = sumoflist - sumofinputlist
    return missingelement

A = [1, 2, 4, 5, 6]
print(missingnumber(A))
# print(missingnumber(A))