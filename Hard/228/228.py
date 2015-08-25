# https://www.reddit.com/r/dailyprogrammer/comments/3hsgr0/08212015_challenge_228_hard_golomb_rulers/

import sys
import itertools
import time

def search(order):
    def validate(marks):
        all_distances = set()
        for pair in itertools.combinations(marks, 2):
            dist = abs(pair[0] - pair[1])
            if dist in all_distances:
                return False
            all_distances.add(dist)
        return True

    for max_mark in itertools.count(start=order):
        possible_marks = range(0, max_mark + 1)
        for perm in itertools.permutations(possible_marks, order):
            if validate(perm):
                return order, max_mark, perm

def main():
    data = open(sys.argv[1]).read().splitlines() # read in the data
    for order in data:
        order = int(order)
        start = time.clock()
        o, l, m = search(order)
        elapsed = time.clock() - start
        print("{0} = {1} in {2:.2} secs: {3}".format(o, l, elapsed, m))

if __name__ == "__main__":
    main()
