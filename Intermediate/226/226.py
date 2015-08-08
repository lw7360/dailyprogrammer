# https://www.reddit.com/r/dailyprogrammer/comments/3fva66/20150805_challenge_226_intermediate_connect_four/

import sys, string

xmoves = open(sys.argv[1]).read().translate(None, string.ascii_lowercase + ' \n')
omoves = open(sys.argv[1]).read().translate(None, string.ascii_uppercase + ' \n')

board = [[' ' for x in range(6)] for x in range(7)]

def insert(colchar, player):
    colnumber = ord(colchar.lower()) - ord('a')
    col = board[colnumber]
    for i in range(len(col)):
        if col[i] == ' ':
            col[i] = player
            break

def checkwinner(player):
    for x in range(6):
        for y in range(6):
            if board[x][y] == player:
                top = board[x][y+1:y+4]
                if len(top) == 3 and not ''.join(top).strip(player):
                    return True
                try:
                    right = [board[x+1][y], board[x+2][y], board[x+3][y]]
                    if not ''.join(right).strip(player):
                        return True
                except:
                    pass
                try:
                    topright = [board[x+1][y+1], board[x+2][y+2], board[x+3][y+3]]
                    if not ''.join(topright).strip(player):
                        return True
                except:
                    pass

for i in range(len(xmoves)):
    insert(xmoves[i], 'X')
    if checkwinner('X'):
        print 'X won at move ' + str(i+1)
        break
    insert(omoves[i], 'O')
    if checkwinner('O'):
        print 'O won at move ' + str(i+1)
        break
