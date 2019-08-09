# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

import math

position = [0,0]
magnitude1 = []
direction = []
for i in range(4):
    userDirection = input("Enter Direction: ")
    direction.append(userDirection)
    magnitude = int(input("Enter a magnitude: "))
    magnitude1.append(magnitude)

i = 0


while i < len(direction):
    if direction[i] == '+Y': 
        position[0] += magnitude1[i]
    elif direction[i] == '-Y': 
        position[0] -= magnitude1[i]
    elif direction[i] == '-X': 
        position[1] -= magnitude1[i]
    elif direction[i] == '+X':
        position[1] += magnitude1[i]
    else: pass
    i += 1

print (int(math.sqrt(position[1]**2+position[0]**2)))