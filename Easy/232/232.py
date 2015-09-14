# https://www.reddit.com/r/dailyprogrammer/comments/3kx6oh/20150914_challenge_232_easy_palindromes/

import sys

def main():
    data = filter(str.isalpha, ''.join(open(sys.argv[1]).read().splitlines()).replace(' ', '')).lower()
    if data == data[::-1]:
        print 'Palindrome'
    else:
        print 'Not a palindrome'

if __name__ == "__main__":
    main()
