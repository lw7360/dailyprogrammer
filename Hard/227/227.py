# https://www.reddit.com/r/dailyprogrammer/comments/3h0uki/20150814_challenge_227_hard_adjacency_matrix/

import sys
import string

def parsediagram(diagram, adjmatrix):
    alph = string.ascii_lowercase[:len(adjmatrix)]

    for a in alph:
        for i, row in enumerate(diagram):
            if a in row:
                findadjacent(diagram, adjmatrix, diagram[i][row.index(a)], i, row.index(a))

    for row in adjmatrix:
        print ''.join(row)

def findadjacent(diagram, adjmatrix, char, y, x, prev=''):
    alph = string.ascii_lowercase
    check = [-1, 0, 1]

    for b in check:
        for a in check:
            try:
                if y + b >= 0 and x + a >= 0:
                    edge = diagram[y + b][x + a]
                    validedges = ''
                    if b == 0:
                        validedges = '-'
                    elif a == 0:
                        validedges = '|'
                    elif a == b:
                        validedges = '\\'
                    else:
                        validedges = '/'
                    if edge in validedges and edge not in prev:
                        n, m = y + b + b, x + a + a
                        while True:
                            if n >= 0 and m >= 0:
                                try:
                                    curchar = diagram[n][m]
                                    if curchar == edge:
                                        n += b
                                        m += a
                                        continue
                                    elif curchar == '#':
                                        findadjacent(diagram, adjmatrix, char, n, m, edge)
                                        break
                                    elif curchar in alph:
                                        row, col = alph.index(char), alph.index(curchar)
                                        if char != curchar:
                                            adjmatrix[row][col] = '1'
                                        break
                                    else:
                                        n += b
                                        m += a
                                except:
                                    break
                            else:
                                break

            except:
                continue
    


def main():
    diagram = open(sys.argv[1]).read().splitlines()[1:]
    
    alph = string.ascii_lowercase
    for i, char in enumerate(alph):
        if char not in ''.join(diagram):
            adjmatrix = [['0' for y in range(i)] for x in range(i)]
            parsediagram(diagram, adjmatrix)
            break

if __name__ == "__main__":
    main()
