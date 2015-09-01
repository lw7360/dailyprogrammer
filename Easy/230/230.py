# https://www.reddit.com/r/dailyprogrammer/comments/3j3pvm/20150831_challenge_230_easy_json_treasure_hunt/

import sys

import json
data = json.load(open("input.txt"))

def recurse(element, stack):
    if element == "dailyprogrammer":
        print(" -> ".join(stack))
        return True
    elif type(element) in (dict, list):
        for k, v in element.items() if type(element) == dict else enumerate(element):
            if recurse(v, stack + [str(k)]):
                return True
    return False

stack = recurse(data, [])
