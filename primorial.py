# https://edabit.com/challenge/fRjfrCYXWJAaQqFXF

def isPrime(n):
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True


def primorial(n):
    arr = []
    x = 2
    while len(arr) != n:
        if isPrime(x):
            arr.append(x)
        x += 1

    result = 1

    for k in arr:
        result *= k
    
    print(arr)

    return result

print(primorial(8))



        


