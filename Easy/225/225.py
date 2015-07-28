# https://www.reddit.com/r/dailyprogrammer/comments/3esrkm/20150727_challenge_225_easyintermediate/

def checkFor(match, realLine):
    for i, char in enumerate(realLine):
        if char in '+|':
            if char == match:
                realLine = realLine[i + 2:].strip()
                return realLine
            else:
                return checkFor('+|'.replace(match, ''), realLine[i + 1:]) 

def main():
    data = open("input3.txt").read().splitlines()
    lines = int(data[0])
    data = data[1:]
    decolumned = ''

    for line in data:
        if not line:
            decolumned += '\n'
            continue

        leftFeature = line[0] in '+|'
        rightFeature = line[-1] in '+|'

        realLine = line

        if leftFeature:
            realLine = checkFor(line[0], realLine[1:])

        if rightFeature and realLine:
            realLine = checkFor(line[-1], realLine[::-1][1:])[::-1]

        realLine = realLine.strip()

        if realLine:
            if realLine[-1] == '-':
                decolumned += realLine[:-1]
            else:
                decolumned += realLine + ' '
        else:
            decolumned += '\n'

    decolumned = decolumned[:-1]
    print decolumned

if __name__ == "__main__":
    main()
