# https://www.reddit.com/r/dailyprogrammer/comments/3dl9wr/20150717_challenge_223_hard_the_heighway_dragon/

import random

def randNum(minr, maxr):
    return int(minr + random.random() * (maxr - minr))

def shuffle(words):
    n = len(words)
    for i in range(0, n - 2):
        j = randNum(i, n)
        words[i], words[j] = words[j], words[i]
    return words

print shuffle([1, 2, 3, 4, 5])
print shuffle(['a', 'b', 'c', 'd', 'e'])
