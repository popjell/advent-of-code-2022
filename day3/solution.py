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
        for i in range(length):
            pack = [x for x in lines[i]]
            packsize = (len(pack))/2
            firsthalf = pack[0:int(packsize)]
            secondhalf = pack[int(packsize):int(len(pack))]
            itempriority = 0
            for j in range(int(packsize)):
                item = firsthalf[j]
                check = secondhalf.count(item)
                if check >= 1:
                    if ord(item) >= 97 and ord(item) <= 122:
                        itempriority = ord(item) - 96
                    else:
                        itempriority = ord(item) - 38
                    
                    break
                
            
            priorcount += itempriority
        print(priorcount)
 
                    
main()        