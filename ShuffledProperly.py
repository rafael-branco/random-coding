#https://edabit.com/challenge/XALogvSrMr3LRwXPH

def is_shuffled_well(arr):
    count = 0
    check = False
    temp = []
    last_result = 0
    for i in range(0, len(arr)):
        
        if(i != len(arr)-1):
            res = arr[i] - arr[i+1]

            if abs(res) == 1 and check and last_result == res:
                count += 1
            elif abs(res) == 1 and not check:
                count = 2
                check = True
            elif (last_result == 1 and res == -1) or (last_result == -1 and res == 1):
                temp.append(count)
                count = 2
            else:
                check = False
                temp.append(count)
                count = 0

            last_result = res
            
    temp.append(count)

    for item in temp:
        if(item >= 3):
            return False

    return True

print(is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]))
print(is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]))
print(is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]))
print(is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))


