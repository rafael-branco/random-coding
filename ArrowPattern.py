def arrow(n):
    arr = []
    if n > 0:
        if n % 2 == 0:
            for i in range(1,n+1):
                temp = ""
                for y in range (0, i):
                    temp += ">"
                
                arr.append(temp)
            for i in range(n,0, -1):
                temp = ""
                for y in range (0, i):
                    temp += ">"
                
                arr.append(temp)
            

        else:
            for i in range(1,n):
                temp = ""
                for y in range (0, i):
                    temp += ">"
                
                arr.append(temp)
            for i in range(n,0,-1):
                temp = ""
                for y in range (0, i):
                    temp += ">"
                
                arr.append(temp)
    return arr

arr = arrow(3)
print()
for item in arr:
    print(item)
print()