
def find_cadence(arr):

    for i in range(0, len(arr)):
        arr[i] = arr[i].upper()

    a = arr[-2]
    b = arr[-1]


    if a == "V" and b == "I":
        return "perfect"
    elif a == "IV" and b == "I":
        return "plagal"
    elif a == "V" and b != "I":
        return "interrupted"
    elif b == "V":
        return "imperfect"
    else: 
        return "no cadence"

print(find_cadence(["ii", "V", "I"]))
print(find_cadence(["I", "IV", "I", "V", "vi"]))