# https://www.reddit.com/r/dailyprogrammer/comments/3ltee2/20150921_challenge_233_easy_the_house_that_ascii/

import random
import sys

def main():
    data = open(sys.argv[1]).read().splitlines()[1::]
    door = random.randrange(len(data[-1]))
    
    wideData = []
    for row in data:
        curStr = ''
        for ast in row:
            if ast == '*':
                curStr += '*****'
            else:
                curStr += '     '
        wideData.append(curStr)

    longData = []
    for row in wideData:
        longData.append(row[:])
        longData.append(row[:])
        longData.append(row[:])

    for row in longData:
        print row


if __name__ == "__main__":
    main()
