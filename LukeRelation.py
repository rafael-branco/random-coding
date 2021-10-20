#https://edabit.com/challenge/8pDH2SRutPoaQghgc

class Person:
  def __init__(self, name, relation):
    self.name = name
    self.relation = relation

def relation_to_luke(name):
    lst = [Person("Darth Vader", "father"), 
        Person("Leia", "sister"),
        Person("Han", "brother in law"),
        Person("R2D2", "droid")]

    for person in lst:
        if person.name == name:
            return "Luke, I am your " + person.relation + "."
    
    return "I dont know you."

print(relation_to_luke("Darth Vader"))
print(relation_to_luke("John Wick"))
    