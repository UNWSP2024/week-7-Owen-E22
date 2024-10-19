# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)
import math

def main():
    x1 = float(input('Enter value for x1: '))
    y1 = float(input('Enter value for y1: '))
    z1 = float(input('Enter value for z1: '))
    x2 = float(input('Enter value for x2: '))
    y2 = float(input('Enter value for y2: '))
    z2 = float(input('Enter value for z2: '))

    point1 = (x1, y1, z1)
    point2 = (x2, y2, z2)
    try:
        distance = calculate_distance(point1, point2)
    except:
        print('distance cannot be negative')

    print(f'The distance between the two points is {distance:.2f} units')


def calculate_distance(list1, list2):
    distance = math.sqrt((list2[0]-list1[0])**2 + (list2[1] - list1[1])**2 + (list1[2] - list2[2])**2)



    return distance

main()