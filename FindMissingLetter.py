def find_missing_letter(chars):
    c0_original = chars[0]
    chars = [x.lower() for x in chars]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    c0 = chars[0]
    for i in range(len(alphabet)):
        if alphabet[i] == c0:
            for j in range(len(chars)):
                if alphabet[i + j] != chars[j]:
                    if c0_original.islower():
                        return alphabet[i + j]
                    else:
                        return alphabet[i + j].upper()
                    
    return None
    
print(find_missing_letter(['a','b','c','d','f']))