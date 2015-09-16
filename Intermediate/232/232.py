# https://www.reddit.com/r/dailyprogrammer/comments/3l61vx/20150916_challenge_232_intermediate_where_should/

from ast import literal_eval
import sys
import math

def closestpoint(point, pointlist, mindist):
    closest = None

    for p in pointlist:
        dist = math.hypot(p[0] - point[0], p[1] - point[1])
        if dist < mindist:
            mindist = dist
            closest = p

    return ((point, closest), mindist)


def main():
    data = open(sys.argv[1]).read().splitlines()[1:] 
    pointlist = []
    for line in data:
        pointlist.append(literal_eval(line))

    closest = None
    mindist = sys.maxint
    for i, point in enumerate(pointlist):
        pointlistcopy = pointlist[:]
        del pointlistcopy[i]

        closestpair, mind = closestpoint(point, pointlistcopy, mindist)

        if mind < mindist:
            closest = closestpair
            mindist = mind

    print closest[1], closest[0]



if __name__ == "__main__":
    main()
