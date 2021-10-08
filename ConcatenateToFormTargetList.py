#https://edabit.com/challenge/23htQEtZobC8cfwcm

def canConcatenate(listOfLists, lst):
    tempList = []

    if len(listOfLists) != 1:
        rows = len(listOfLists)
        for i in range(0, rows):
            col = len(listOfLists[i])
            for j in range(0, col):
                tempList.append(listOfLists[i][j])
        tempList = sorted(tempList)
        lst = sorted(lst)
        result = tempList == lst
        print(result)
    return result

canConcatenate([[1, 2, 3, 4], [5, 6], [7]], [1, 2, 3, 4, 5, 6, 7])
canConcatenate([[2, 1, 3], [5, 4, 7, 6]], [7, 6, 5, 4, 3, 2, 1])
canConcatenate([[2, 1, 3], [5, 4, 7, 6, 7]], [1, 2, 3, 4, 5, 6, 7])
canConcatenate([[2, 1, 3], [5, 4, 7]], [1, 2, 3, 4, 5, 6, 7])
        