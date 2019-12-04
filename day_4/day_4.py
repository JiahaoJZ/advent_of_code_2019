'''
Input -> number (String)
Output -> True if the digits are sorted
'''
def DigitNeverDecreases(number):
    pivot = -1
    for elem in number:
        if int(elem) < pivot:
            return False
        else:
            pivot = int(elem)
    return True

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
Output -> True if there are any pair (and only pair) of digits adjacent
with the same value, False ioc
'''
def PairAdjacent_2(number):
    pivot = -1
    # without the second variable on two_adjacent my code was accepting any
    # even number of repetitions of a number
    two_adjacent = [False, pivot]
    for elem in number:
        if int(elem) == pivot:
            # If dont have a pair yet
            if not two_adjacent[0]:
                # If we have encountered the number more than once (case 124444)
                if int(elem) != two_adjacent[1]:
                    two_adjacent[0] = True
            # If the occurrence of a number is higher than 2
            else:
                two_adjacent[0] = False
                two_adjacent[1] = pivot
        else:
            pivot = int(elem)
            two_adjacent[1] = -1
            if two_adjacent[0]:
                return True
    # If the pair is located at the end
    if two_adjacent[0]:
        return True
    return False

def Main():
    #input
    A = 307237
    B = 769058
    #Given the problem we know A must be greater than 333333 and B must be
    #smaller 700000 than so..
    A = 333333
    B = 700000

    digit_list = [int(x) for x in range(A,B) if DigitNeverDecreases(str(x))]
    print("Part 1 answer: " + str(len([x for x in digit_list if PairAdjacent(str(x))])))
    print("Part 2 answer: " + str(len([x for x in digit_list if PairAdjacent_2(str(x))])))

if __name__ == "__main__":
    Main()
