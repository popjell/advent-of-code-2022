import sys
from sys import argv

def main():
    if(len(sys.argv) != 2):
        print("nope")
        return
    with open(argv[1], "r") as file:
        signal = file.read()
        length = len(signal)
        for i in range(length):
            if(i < 13):
                continue
            marker = [signal[i-13],signal[i-12],signal[i-11],signal[i-10],signal[i-9],signal[i-8],signal[i-7],signal[i-6],signal[i-5],signal[i-4],signal[i-3],signal[i-2],signal[i-1],signal[i]]
            validsignal = True
            for j in range(len(marker)):                
                if marker.count(marker[j]) > 1:
                    validsignal = False
            if validsignal:
                print(marker)
                print(i + 1)
                break
                             
main()        