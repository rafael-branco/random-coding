def get_middle(s):
    if len(s) <= 2:
        return s
    else:
        l = len(s)
        if l % 2 == 0:
            return s[int((l/2)-1):int((l/2)+1)]
        else:
            return s[int((l-1)/2)]

print(get_middle("tet"))