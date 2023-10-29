import sys
import re
from json import loads

if __name__ == "__main__":
    file = open("input_12.txt","r")
    line = file.read()
    file.close()

    def solve(j):
        if type(j) == int:
            return j
        if type(j) == list:
            return sum([solve(j) for j in j])
        if type(j) != dict:
            return 0
        if 'red' in j.values():
            return 0
        return solve(list(j.values()))

    print ("Sum :", solve(loads(line)))