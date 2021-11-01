def get_sum(a,b):
    
    if a > b:
        temp = a
        a = b
        b = temp
    sum = 0
    if a != b:

        for i in range(a, b+1):
            sum += i
        
        return sum
    else:
        return a

print(get_sum(-1, 2))
    