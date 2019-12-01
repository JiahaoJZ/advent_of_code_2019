import FileParser

'''
Input -> fuel_mass (int), fuel_requiered_so_far (int)
Output -> an integer with the fuel requiered
'''
def FuelRequieredPerModule(mass, fuel_requiered_so_far=0):
    fuel = int(mass/3) - 2
    if(fuel <= 0):
        return fuel_requiered_so_far
    else:
        return FuelRequieredPerModule(fuel, fuel+fuel_requiered_so_far)

def FuelRequiered(data):
    return sum([int(int(x)/3)-2 for x in data])

def FuelRequieredPhase2(data):
    return sum([FuelRequieredPerModule(int(x)) for x in data])

def Main():
    content = FileParser.ReadLines("day_1_data.txt")
    print("Part 1 answer: " + str(FuelRequiered(content)))
    print("Part 2 answer: " + str(FuelRequieredPhase2(content)))

if __name__ == "__main__":
    Main()
