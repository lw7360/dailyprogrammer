# https://www.reddit.com/r/dailyprogrammer/comments/3kj1v9/20150911_challenge_231_hard_eight_husbands_for/

import sys

def stableMatching(preferences):
    available_men = [p for p in preferences if p==p.upper()]
    available_women = [p for p in preferences if p==p.lower()]
    pairs = {}
    while available_men:
        man = available_men[0]
        woman = preferences[man].pop(0)
        if woman in available_women:
            pairs[woman] = man
            available_women.remove(woman)
            available_men.remove(man)
        else:
            rival = pairs[woman]
            if preferences[woman].index(man) < preferences[woman].index(rival):
                available_men.append(rival)
                available_men.remove(man)
                pairs[woman] = man
    return pairs

def main():
    data = open(sys.argv[1]).read().splitlines() # read in the data
    prefs = {}

    for line in data:
        pref = line.split(', ')
        prefs[pref[0]] = pref[1:]

    matching = sorted(stableMatching(prefs).items(), key=lambda x: x[1])

    for k, v in matching:
        print('{}; {}'.format(v, k))

if __name__ == "__main__":
    main()
