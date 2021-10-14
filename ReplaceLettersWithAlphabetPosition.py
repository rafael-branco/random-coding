# https://edabit.com/challenge/Bm3JCT6rFrnAhHohy
import re

def alphabet_index(temp_string):
    temp_string = temp_string.lower()
    regex = re.compile('[^a-zA-Z]')
    temp_string = regex.sub("", temp_string)

    result = ""
    for i in range(0, len(temp_string)):
        temp_char = ord(temp_string[i])
        if temp_char >= 97 and temp_char < 123:
            result += str(temp_char - 97 + 1)
            if i != (len(temp_string) - 1):
                result += " "

    return result

print(alphabet_index("Wednesday is hump day, but has anyone asked the camel if he's happy about it?"))