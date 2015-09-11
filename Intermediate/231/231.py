# https://www.reddit.com/r/dailyprogrammer/comments/3ke4l6/20150909_challenge_231_intermediate_set_game/

from itertools import combinations
import sys

def main():
    lines = open(sys.argv[1]).read().splitlines() # read in the data
    for cards in combinations(lines, 3):
      if any(len(set(card[i] for card in cards)) == 2 for i in range(4)):
        continue
      for card in cards:
        print(card, end=" ")
      print()

if __name__ == "__main__":
    main()
