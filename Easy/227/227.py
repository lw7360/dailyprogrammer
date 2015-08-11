# https://www.reddit.com/r/dailyprogrammer/comments/3ggli3/20150810_challenge_227_easy_square_spirals/

import sys
from math import sqrt

def getlocation(spiralsize, point):
    start = spiralsize / 2 + 1

    layer, i = 0, 1

    while point > i * i:
        layer += 1
        i += 2
        
    location = [start + layer, start + layer]
    tail = i * i
    mod = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for a in range(4):
        if tail == point:
            break
        curmod = mod[a]
        for b in range(i - 1):
            if tail == point:
                break
            tail -= 1
            location[0] += curmod[0]
            location[1] += curmod[1]

    return location

def getpoint(spiralsize, x, y):
    center = spiralsize /2 + 1
    layer = max(abs(x - center), abs(y - center))

    layerlen = layer * 2 + 1
    tail = layerlen * layerlen
    taillocation = [center + layer, center + layer]
    mod = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for a in range(4):
        if taillocation[0] == x and taillocation[1] == y:
            break
        curmod = mod[a]
        count = 0
        while count < layerlen - 1:
            if taillocation[0] == x and taillocation[1] == y:
                break
            tail -= 1
            taillocation[0] += curmod[0]
            taillocation[1] += curmod[1]
            count += 1


    return tail


def main():
    data = open(sys.argv[1]).read().splitlines()

    spiralsize = int(data[0])
    splitdata = data[1].split(' ')
    if len(splitdata) == 1:
        print tuple(getlocation(spiralsize, int(splitdata[0])))
    else:
        print getpoint(spiralsize, int(splitdata[0]), int(splitdata[1]))

if __name__ == "__main__":
    main()
