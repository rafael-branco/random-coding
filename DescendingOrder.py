def descending_order(num):
    res = list(map(str, str(num)))
    res.sort(reverse=True)
    return int(''.join(res))


print(descending_order(15261))