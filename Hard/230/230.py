# https://www.reddit.com/r/dailyprogrammer/comments/3jn6te/20150903_challenge_230_hard_logo/

import os
import sys

fullwords = {}

X = None
Y = None
grid = None
res = None

def deletechar(ori, x, y):
    if ori == 0:
        if ((y > 0 and grid[y-1][x] != ' ') or
            (y < Y-1 and grid[y+1][x] != ' ')):
            pass # don't delete used letters
        else:
            grid[y] = grid[y][0:x] + ' ' + grid[y][x+1:]
    else:
        if ((x > 0 and grid[y][x-1] != ' ') or
            (x < X-1 and grid[y][x+1] != ' ')):
            pass # don't delete used letters
        else:
            grid[y] = grid[y][0:x] + ' ' + grid[y][x+1:]

def vertword(x, y, L):
    return "".join([ grid[_y][x] for _y in range(y, y+L) ])

def findword(x, y, orient):
    if orient == 0:
        for L in range(X - x, 0, -1):
            hword = grid[y][x:x+L]
            if hword[::-1] in fullwords:
                hword = hword[::-1]
            if hword in fullwords:
                res.append(hword)
                for _x in range(x, x + L):
                    deletechar(orient, _x, y)
                break
    else:
        for L in range(Y - y, 0, -1):
            vword = vertword(x, y, L)
            if vword[::-1] in fullwords:
                vword = vword[::-1]
            if vword in fullwords:
                res.append(vword)
                for _y in range(y, y + L):
                    deletechar(orient, x, _y)
                break

def main():
    global X, Y, grid, res

    wl = open("words", "rb")
    for w in wl:
        fullwords[w.strip().upper()] = True

    f = open(sys.argv[1], "rb")
    Y = int(f.next())

    lines = []

    for i in range(Y):
        ln = f.next()
        lines.append( ln.rstrip("\r\n") )
    X = len(lines[0])
    grid = lines

    res = []
    for y in range(Y):
        for x in range(X):
            for orient in range(2):
                findword(x, y, orient)

    res.sort()
    for r in res:
        print r.lower()

if __name__ == "__main__":
    main()