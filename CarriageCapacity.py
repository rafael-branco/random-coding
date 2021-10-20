# https://edabit.com/challenge/XfSvKco6KZFRfgQyj

def find_a_seat(passengers, carriages):
    max_capacity = passengers / len(carriages)
    for i in range(0,len(carriages)):
        if carriages[i] <= 0.5*max_capacity:
            #print(i)
            return i
    #print(-1)
    return -1