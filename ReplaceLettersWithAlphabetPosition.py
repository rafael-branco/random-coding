# https://edabit.com/challenge/Bm3JCT6rFrnAhHohy

def alphabet_index(temp_string):
    temp_string = temp_string.lower()
    result = ""
    for i in range(0, len(temp_string)):
        temp_char = ord(temp_string[i])
        if temp_char >= 97 and temp_char < 123:
            result += str(temp_char - 97 + 1) + " "
    
    return result



print(alphabet_index("abcdefghijkLm.nopqrstuvwxyZ"))