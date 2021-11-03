def xo(s):
    s = s.lower()
    o = 0
    x = 0
    
    for c in s:
        if c == 'o':
            o += 1
        elif c == 'x':
            x += 1

    if x > 0 or o > 0:
        return x == o
    else:
        return True