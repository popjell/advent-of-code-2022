import sys
from sys import argv

def main():
    if(len(sys.argv) != 2):
        print("nope")
        return
    with open(argv[1], "r") as file:
        lines = file.read().split("\n")
        length = len(lines)
        overlap = 0
        for i in range(len(lines)):
            pair = lines[i].split(',')
            pair1 = pair[0].split('-')
            pair2 = pair[1].split('-')
            a = pair1[0]
            b = pair1[1]
            c = pair2[0]
            d = pair2[1]
            check1 = int(a) >= int(c) and int(a) <= int(d)
            check2 = int(b) >= int(c) and int(b) <= int(d)
            check3 = int(c) >= int(a) and int(c) <= int(b)
            check4 = int(d) >= int(a) and int(d) <= int(b)
            if check1 or check2 or check3 or check4:
                overlap += 1
                
        print("\n\n")
        print(overlap)
            
 
                    
main()        