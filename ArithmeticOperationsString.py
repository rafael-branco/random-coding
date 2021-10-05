def isOperation(arr):
    operators = ['+', '-', '//', '*']

    for op in operators:
        if(arr[1] == op):
            if(arr[0].isdigit() and arr[2].isdigit()):
                return True
            else:
                return False
    
    return False
                



def arithmetic_operation(str):
    temp = str.split(" ")
    if len(temp) != 3:
        return None
    elif isOperation(temp):
        num1 = int(temp[0])
        num2 = int(temp[2])
        if temp[1] == '+':
            return num1 + num2
        elif temp[1] == '-':
            return num1 - num2
        elif temp[1] == '//':
            if num2 == 0:
                return -1
            else:
                return num1 / num2

        elif temp[1] == '*':
            return num1 * num2
        else:
            return None
    else:
        return None

print(arithmetic_operation("10 // 0"))
