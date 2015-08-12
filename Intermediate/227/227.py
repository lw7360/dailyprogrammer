# https://www.reddit.com/r/dailyprogrammer/comments/3gpjn3/20150812_challenge_227_intermediate_contiguous/

import sys

def countchains(chains):
    count = 0
    for i, row in enumerate(chains):
        for j, char in enumerate(row):
            if char == 'x':
                markchain(chains, i, j)
                count += 1
    print count

def markchain(chains, i, j):
    maxheight = len(chains)
    maxwidth = len(chains[0])

    if i >= 0 and i < maxheight and j >= 0 and j < maxwidth and chains[i][j] == 'x':
        chains[i][j] = ' '
        markchain(chains, i, j + 1)
        markchain(chains, i + 1, j)
        markchain(chains, i, j - 1)
        markchain(chains, i - 1, j)

def main():
    data = [list(x) for x in open(sys.argv[1]).read().splitlines()[1:]]
    countchains(data)

if __name__ == "__main__":
    main()
