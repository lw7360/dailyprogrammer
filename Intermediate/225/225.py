# https://www.reddit.com/r/dailyprogrammer/comments/3f9o7k/20150731_challenge_225_intermediate_diagonal_maze/

import sys

maze = open(sys.argv[1]).read().splitlines()[1:]
width, height = len(maze[0]), len(maze)

diagonalized = []

for h in range(height * 3):
    diagonalized.append([' '] * width * 3)

def diagonalIndex(row, col):
    y = 0 + row + col
    x = len(diagonalized[0])/2 - row + col
    return (y, x)

def delCol(col):
    for row in diagonalized:
        row[col] = ''

for j in range(len(maze)):
    for i in range(len(maze[j])):
        y, x = diagonalIndex(j, i)
        diagonalized[y][x] = maze[j][i]

for i in range(len(diagonalized)):
    diagonalized[i] = ['\\' if char=='-' else char for char in diagonalized[i]]
    diagonalized[i] = ['/' if char=='|' else char for char in diagonalized[i]]

for j in range(len(diagonalized)):
    for i in range(len(diagonalized[j])):
        if diagonalized[j][i] == '+':
            delCol(i)
    
crunched = []

for row in diagonalized:
    if '/' in row or '\\' in row:
        crunched.append(row)

for row in crunched:
    print ''.join(row)
