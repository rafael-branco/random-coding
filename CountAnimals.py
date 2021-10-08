# https://edabit.com/challenge/u7ykayCJjyQXAk7gw

def count_animals(str):
    animals = ["dog", "cat", "bat", "cock", "cow", "pig",
                "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
                "frog", "hen", "mole", "duck", "goat"]
    count = 0
    tempStr = list(str)
    for animal in animals:
        tempName = ""
        animal = list(animal)
        for j in range(0, len(animal)):
            letter = animal[j]
            for i in range(0, len(tempStr)):
                if letter == tempStr[i] and letter != '':
                    animal[j] = ''
                    tempName += letter
                    tempStr[i] = ''
        
        if "".join(animal) == '':
            count += 1

    return count

            
                    




print(count_animals("goatcode"))
print(count_animals("cockdogwdufrbir"))
print(count_animals("dogdogdogdogdog"))