# https://www.reddit.com/r/dailyprogrammer/comments/3efbfh/20150724_challenge_224_hard_langford_strings/

import string
alphabet = list(string.ascii_uppercase)
order = 8

def langford():
    for i, letter in enumerate(alphabet):
        if (i < order):
            unusedLetters = [2] * order
            unusedLetters[i] -= 1
            langfordHelper(letter, unusedLetters)

def checkLangford(curString):
    for i, letter in enumerate(curString, 1):
        if letter in curString[i:]:
            if curString[i:].index(letter) != alphabet.index(letter) + 1:
                return False
        elif letter not in curString[:i]:
            if alphabet.index(letter) + 1 + i > order * 2:
                return False
    return True

def langfordHelper(curString, unusedLetters):
    # print curString, unusedLetters
    if len(curString) == order * 2:
        print curString
    else:
        for i, j in enumerate(unusedLetters):
            if j:
                letter = alphabet[i]
                if checkLangford(curString + letter):
                    copyUnused = unusedLetters[:]
                    copyUnused[i] -= 1
                    langfordHelper(curString + letter, copyUnused)

def main():
    langford()

if __name__ == "__main__":
    main()
