import FileParser, math

# This will be used to move on X,Y during the loop
X_Y_coords = {'L':(-1,0), 'R':(1,0), 'U':(0,1) ,'D':(0,-1)}

'''
Input -> Pair_A (int,int), Pair_B (int,int)
Output -> pair(int,int) with their sum
'''
def AddPair(Pair_A, Pair_B):
    return (Pair_A[0]+Pair_B[0], Pair_A[1]+Pair_B[1])

'''
Input -> Wire (string[] )
Output -> pair(int,int)[] with the points each wires encounters during its path
Additional info:
If the wire encounters a point more than once, we do not store it twice, that is
why I am using a set()
'''
def PointsSet(Wire):
    current_pos = (0,0)
    wire_points = set()
    wire_points.add(current_pos)
    for elem in Wire:
        direction = elem[0]
        cable_length = elem[1:]
        for _ in range(0,int(cable_length)):
            current_pos = AddPair(current_pos, X_Y_coords.get(direction))
            wire_points.add(current_pos)
    return wire_points

'''
Input -> Wire (string[] )
Output -> dict(pair(int,int) -> int) being the pair each point and the int
the number of steps requiered to get into the point
Additional info:
If more we encounter the point more than once, we only store the steps taken
for the first encounter
'''
def PointsSetWithCounter(Wire):
    current_pos = (0,0)
    wire_points = dict()
    wire_points[0,0] = 0
    counter = 1
    for elem in Wire:
        direction = elem[0]
        cable_length = elem[1:]
        for _ in range(0,int(cable_length)):
            current_pos = AddPair(current_pos, X_Y_coords.get(direction))
            if(current_pos not in wire_points.keys()):
                wire_points[current_pos] = counter
            counter += 1
    return wire_points

'''
Input -> Pair_A (int,int), Pair_B (int,int)
Output -> int with their Manhattan distance
'''
def ManhattanDistance(A,B):
    return math.fabs(A[0] - B[0]) + math.fabs(A[1] - B[1])

def Main():
    Wires = FileParser.ReadLines('day_3_data.txt')
    Wire_1 = Wires[0].split(',')
    Wire_2 = Wires[1].split(',')
    collision_points = PointsSet(Wire_1)&PointsSet(Wire_2)
    collision_points.remove((0,0)) # The central port it is not counted
    part_1_answer = min([int(ManhattanDistance((0,0),x)) for x in collision_points])
    print("Part 1 answer: " + str(part_1_answer))

    Wire_1_points = PointsSetWithCounter(Wire_1)
    Wire_2_points = PointsSetWithCounter(Wire_2)
    part_2_answer = min([Wire_1_points[x] + Wire_2_points[x] for x in collision_points])
    print("Part 2 answer: " + str(part_2_answer))

if __name__ == "__main__":
    Main()
