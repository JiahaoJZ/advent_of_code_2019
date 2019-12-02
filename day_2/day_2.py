import FileParser

'''
Input -> data (string[] )
Output -> int with the value of the pos 0 of data
Additional info:
Each instruction requieres 4 positions in the array [x, y, z, d]
The first pos (x) indicates the operation:
    - 1 to add pos[y] and pos[z] and storage it on [d]
    - 2 to multiply pos[y] and pos[z] and storage it on [d]
    - 99 to halt the programm
    - else something went wrong (myb in my code? it is not specifyied)

'''
def RunIntCode(data, noun=12, verb=2):
    halt = False
    data = [int(x) for x in data] # parse str to int
    # In the description they tell us to switch [1] -> 12 and [2] -> 2
    data[1] = noun
    data[2] = verb
    pointer = 0

    while(data[pointer] != 99):
        param_1 = data[data[pointer+1]]
        param_2 = data[data[pointer+2]]
        if data[pointer] == 1:
            data[data[pointer+3]] = param_1 + param_2
        else:
            data[data[pointer+3]] = param_1 * param_2
        pointer = pointer + 4

    return data[0]

'''
Input -> number (int)
Output -> int with the combination of noun + verb that produces this number
          using this formula 100 * noun + verb
Additional info:
Noun and verb are a number between[0,99]

BRUTE FORCE
'''
def GuessNounAndVerb(content, number):
    for noun in range(0,100):
        for verb in range(0,100):
            if RunIntCode(content, noun,verb) == number:
                return 100 * noun + verb

def Main():
    content = FileParser.ReadWithCommaSeparator("day_2_data.txt")
    print("Part 1 answer: " + str(RunIntCode(content)))
    print("Part 2 answer: " + str(GuessNounAndVerb(content, 19690720)))

if __name__ == "__main__":
    Main()
