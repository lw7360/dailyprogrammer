# https://www.reddit.com/r/dailyprogrammer/comments/3h9pde/20150817_challenge_228_easy_letters_in/

import sys

def main():
    data = open(sys.argv[1]).read().splitlines()
    for line in data:
        sortedline = ''.join(sorted(line))
        reversedline = line[::-1]
        sortedreverse = ''.join(sorted(reversedline))
        if sortedline == line:
            print line + ' IN ORDER'
        elif sortedreverse == reversedline:
            print line + ' REVERSE ORDER'
        else:
            print line + ' NOT IN ORDER'

if __name__ == "__main__":
    main()
