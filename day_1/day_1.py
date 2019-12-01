import FileParser

'''
Input -> mass (int), fuel_requiered_so_far (int)
Output -> an integer with the fuel requiered
'''
def FuelRequieredPerModule(mass, fuel_requiered_so_far):
    fuel = int(mass/3) - 2
    if(fuel <= 0):
        return sum
    else:
        return FuelRequieredPerModule(fuel, fuel_requiered_so_far+fuel)

def FuelRequiered(data):
    data = data.split('\n')
    return sum([int(int(x)/3)-2 for x in data])

def FuelRequieredPhase2(data):
    data = data.split('\n')
    return sum([FuelRequieredPerModule(int(x),0) for x in data])

def Main():
    content = FileParser.GetFileContents("day_1_data.txt")
    print("Part 1 answer: " + str(FuelRequiered(content)))
    print("Part 2 answer: " + str(FuelRequieredPhase2(content)))

if __name__ == "__main__":
    Main()
