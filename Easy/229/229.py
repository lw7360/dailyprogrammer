# https://www.reddit.com/r/dailyprogrammer/comments/3i99w8/20150824_challenge_229_easy_the_dottie_number/

from math import cos

def main():
    dottie = 0
    while str(dottie) != str(cos(dottie)):
        print dottie
        dottie = cos(dottie)

    print dottie

if __name__ == "__main__":
    main()
