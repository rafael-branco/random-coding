# https://edabit.com/challenge/FF6kYPHdAcJnoosr5

def factorial(number):
    if number > 0:
        temp = 1
        for x in range(1,number+1):
            temp = x * temp
        return temp
    elif number == 0:
        return 0
    else:
        print("Error: Value lesser than 0")
        return -1


print(factorial(13))
