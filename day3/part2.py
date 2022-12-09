import sys
from sys import argv

def main():
    if(len(sys.argv) != 2):
        print("nope")
        return
    with open(argv[1], "r") as file:
        lines = file.read().split("\n")
        length = len(lines)
        priorcount = 0
        c = 0
        currentgroup = []
        for i in range(int(length)):
            c += 1
            group = lines[i]
            currentgroup.append(group)
            if c >= 3:
                c = 0
                number1 = [x for x in currentgroup[0]]
                number2 = [x for x in currentgroup[1]]
                number3 = [x for x in currentgroup[2]]
                itempriority = 0
                for i in range(len(number1)):
                    item = number1[i]
                    twocount = number2.count(item)
                    threecount = number3.count(item)
                    if twocount >= 1 and threecount >= 1:
                        if ord(item) >= 97 and ord(item) <= 122:
                            itempriority = ord(item) - 96
                        else:
                            itempriority = ord(item) - 38
                        break
                currentgroup.clear()
                priorcount += itempriority
        print(priorcount)
 
                    
main()        