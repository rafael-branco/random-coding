#https://edabit.com/challenge/6hh5BsRivRwMhiZrt

def isPrime(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True

def sum_ff(num):
    arr = []
    for i in range(1, num):
        if num % i == 0 and not isPrime(i):
            arr.append(i)

    if(len(arr) != 0):
        print(arr, end=" ")
        sum = 0
        for n in arr:
            for i in range(2, n):
                if n % i == 0:
                    sum += i
        return sum

    else:
        return 0


print(sum_ff(69))
print(sum_ff(12))
print(sum_ff(420))
print(sum_ff(619))
