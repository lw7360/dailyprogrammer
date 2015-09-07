# https://www.reddit.com/r/dailyprogrammer/comments/3jz8tt/20150907_challenge_213_easy_cellular_automata/

import sys

def rule90(state):
    nextstate = ''
    for i in range(1, len(state) - 1):
        if state[i-1:i+2].count(state[i]) == 2:
            nextstate += '1'
        else:
            nextstate += '0'

    return '0' + nextstate + '0'

def printstate(state):
    print state[1:-1].replace('1', 'x').replace('0', ' ')

def main():
    state = '0' + open(sys.argv[1]).read() + '0' # read in the data

    printstate(state)

    for x in range(25):
        state = rule90(state)
        if state == len(state) * '0':
            break
        printstate(state)


if __name__ == "__main__":
    main()
