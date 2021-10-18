# https://edabit.com/challenge/HYjQKDXFfeppcWmLX

def is_curzon(n):
    r1 = pow(2, n) + 1
    r2 = 2 * n + 1
    return r1 % r2 == 0

print(is_curzon(5))
print(is_curzon(10))
print(is_curzon(14))