import sys
from sys import argv


def main():
    if len(sys.argv) != 2:
        print("nope")
        return
    with open(argv[1], "r") as file:
        lines = file.read().split("\n")
        cals = []
        current = 0
        for i in range(len(lines)):
            inp = lines[i]
            if inp == '':
                cals.append(current)
                current = 0
            else:
                current += int(inp)
        cals.sort(key = int, reverse = True)
        returnval = cals[0] + cals[1] + cals[2]
        print(returnval)
        
main()
            
            
