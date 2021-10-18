#https://edabit.com/challenge/NLY7zGMYocsTbeS6n

def reverse(state):
    if type(state) == bool:
        return not state
    else:
        return ("boolean expected")


print(reverse(True))
