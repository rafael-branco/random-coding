#https://edabit.com/challenge/quMt6typruySiNSAJ

def shuffle_count(num):
    if num > 0 and num % 2 ==0:
        arr = []
        temp = []
        for i in range(1, num + 1):
            arr.append(i)
            temp.append(0)
        
        halfPosition = int(num / 2)
        
        part1 = arr[0:halfPosition]
        part2 = arr[halfPosition: num]
        
        count = 0
        while temp != arr:
            count += 1
            j = 0
            k = 0
            for i in range(0, num):
                if i % 2 == 0:
                    temp[i] = part1[j]
                    j += 1
                else:
                    temp[i] = part2[k]
                    k += 1
            part1 = temp[0:halfPosition]
            part2 = temp[halfPosition: num]
            

        return count
    else:
        return None


print(shuffle_count(8))
print(shuffle_count(14))
print(shuffle_count(52))