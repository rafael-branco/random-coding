#https://edabit.com/challenge/eraBhwF8HkJDAa2pS

def max_value(arr):
    max = arr[0]
    for item in arr:
        if item > max:
            max = item
    return max

def pirates_killed(gold, ineq):
    max = max_value(gold)
    diff = []
    for i in range(0, len(gold)):
        diff.append(max - gold[i])

    for i in range(0, len(gold)):
        if(ineq[i] < diff[i]):
            return True
    return False


print(pirates_killed([3, 5, 8, 3, 4], [10, 4, 2, 5, 5]))
print(pirates_killed([3, 5, 8, 3, 4], [10, 4, 2, 5, 1]))
print(pirates_killed([3,3,10], [7,7,0]))
print(pirates_killed([3,3,10], [6,6,0]))
