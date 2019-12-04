'''
Input -> number (String)
Output -> True if the digits are sorted
'''
def DigitNeverDecreases(number):
    return sorted(number) == [x for x in number]

'''
Input -> number (String)
Output -> True if there are 2 digits adjacent with the same value, False ioc
'''
def PairAdjacent(number):
    pivot = -1
    for elem in number:
        if int(elem) == pivot:
            return True
        else:
            pivot = int(elem)
    return False

'''
Input -> number (String)
Output -> True if there is a number repeated twice
'''
def PairAdjacent_2(number):
    number_counter = dict()
    for elem in number:
        if elem not in number_counter:
            number_counter[elem] = 1
        else:
            number_counter[elem] += 1
    return 2 in number_counter.values()

def Main():
    #input
    A = 307237
    B = 769058
    #Given the problem we know A must be greater than 333333 and B must be
    #smaller than 700000 so..
    A = 333333
    B = 700000

    digit_list = [int(x) for x in range(A,B) if DigitNeverDecreases(str(x))]
    print("Part 1 answer: " + str(len([x for x in digit_list if PairAdjacent(str(x))])))
    print("Part 2 answer: " + str(len([x for x in digit_list if PairAdjacent_2(str(x))])))

if __name__ == "__main__":
    Main()
