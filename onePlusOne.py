import traceback

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def worded_math(strMath):
    numbers = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    temp = strMath.lower().split(" ")
    if len(temp) == 3:
        try:
            a = numbers[temp[0]]
            b = numbers[temp[2]]
            result = 0
            if temp[1].lower() == "plus":
                result = sum(a,b)
            elif temp[1].lower() == "minus":
                result = sub(a, b)
            else:
                print("Operator error")
                return None
            
            for key, value in numbers.items():
                if value == result:
                    return key.capitalize()
            print("Out of Range")
            return None

        except Exception:
            traceback.print_exc()
            return None

print(worded_math("one plUs two"))
print(worded_math("one plUs FIVE"))

         