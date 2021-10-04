#https://edabit.com/challenge/4Y5Zk5f9LckvWjFf3

def special_reverse(str, letter):
    temp = str.lower()
    temp = temp.split(" ")
    for i in range(0, len(temp)):
        if temp[i][0] == letter:
            temp[i] = temp[i][::-1]
    
    newStr = " "

    newStr = newStr.join(temp,)

    return newStr

print(special_reverse("word searches are super fun", "s"))


