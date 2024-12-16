# Advant of Code 2024 Day 6

# Question 2

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

def tracking(map, curPosition, curDirection):
    seen = set()
    left = False
    while not left:
        movement = directionMove(curDirection)
        newPosition = tuple(np.add(curPosition, movement))
        if not 0 <= newPosition[0] < len(map) or not 0 <= newPosition[1] < len(map[0]):
            return False
        elif map[newPosition[0]][newPosition[1]] == '#':
           curDirection = updateDirection(curDirection)
        else:
            curPosition = newPosition
            if(curPosition, curDirection) in seen:
                return True
            else:
                seen.add((curPosition, curDirection))


direction = findStartingDirection(enemyMovement)
position = findStartingPosition(enemyMovement)
for i in range(len(enemyMovement)):
    for j in range(len(enemyMovement[0])):
        if enemyMovement[i][j] != ".": continue
        enemyMovement[i][j] = "#"
        if tracking(enemyMovement, position, direction):
            count += 1
        enemyMovement[i][j] = "."

print(count)


