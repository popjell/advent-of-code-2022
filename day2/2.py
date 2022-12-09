import sys
from sys import argv

def main():
    if(len(sys.argv) != 2):
        print("nope")
        return
    with open(argv[1], "r") as file:
        lines = file.read().split("\n")
        score = 0
        for i in range(len(lines)):
            scenario = lines[i].split(" ")
            enemy = scenario[0]
            response = scenario[1]
            roundscore = 0
            #rock a paper b scissors c
            #lose x draw y win z
            #rock 1 paper 2 scissors 3
            #rock
            if enemy == 'A':
                if response == 'X':
                    score += 3
                elif response == 'Y':
                    score += 4
                elif response == 'Z':
                    score += 8            
            elif enemy == 'B':
                if response == 'X':
                    score += 1
                elif response == 'Y':
                    score += 5
                elif response == 'Z':
                    score += 9
            elif enemy == 'C':
                if response == 'X':
                    score += 2
                elif response == 'Y':
                    score += 6
                elif response == 'Z':
                    score += 7
        print(score)    
                    
            
                    
main()        