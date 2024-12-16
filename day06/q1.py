# Advant of Code 2024 Day 6

# Question 1

import numpy as np

enemyMovement = []
directions = "<>^v" #left right up down
count = 0

with open("input.txt", "r") as file:
    enemyMovement = [list(line.strip()) for line in file]

def findStartingDirection(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] in directions:
                return map[i][j]

def findStartingPosition(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] in directions:
                return (i,j)
            

def directionMove(direction):
    if direction == "^":
        return (-1,0)
    elif direction == "v":
        return (1,0)
    elif direction == "<":
        return (0, -1)
    elif direction == ">":
        return (0, 1)
    
def updateDirection(direction):
    if direction == "^":
        return ">"
    elif direction == ">":
        return "v"
    elif direction == "v":
        return "<"
    elif direction == "<":
        return "^"

def tracking(map, position, direction):
    left = False
    while not left:
        movement = directionMove(direction)
        newPosition = tuple(np.add(position, movement))
        if not 0 <= newPosition[0] < len(map) or not 0 <= newPosition[1] < len(map[0]):
            map[position[0]][position[1]] = 'X'
            left = True
        elif map[newPosition[0]][newPosition[1]] == '#':
            direction = updateDirection(direction)
        else:
            map[position[0]][position[1]] = 'X'
            map[newPosition[0]][newPosition[1]] = direction
            position = newPosition

direction = findStartingDirection(enemyMovement)
position = findStartingPosition(enemyMovement)
tracking(enemyMovement, position, direction)
for i in range(len(enemyMovement)):
    for j in range(len(enemyMovement[0])):
        if enemyMovement[i][j] == 'X':
            count += 1

print(count)


