def is_equal(arr):
    if len(arr) == 2:
        sum = [0,0]
        for i in range(0,len(arr)):
            temp = str(arr[i])
            for s in temp:
                sum[i] += int(s)
        
        return sum[0] == sum[1]
    else:
        return -1


print(is_equal([102,3]))

