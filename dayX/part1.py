
filename = str(input())

commands = open(filename, "r").read().split("\n")

cycle = 0

X = 1

nextcheck = 20

signalsum = 0

def increcheck(increment, value):
    global cycle
    global nextcheck
    global X
    global signalsum
    cycle += 1
    if cycle == nextcheck:
        nextcheck += 40
        signalstrength = X * cycle
        signalsum += signalstrength
    if increment:
        X += value


for i in range(len(commands)):
    cmd = commands[i]
    header = cmd[0:4:]
    ender = ""
    if header == "noop":
        increcheck(False, 0)
    else:
        ender = int(cmd[5:])
        increcheck(False, 0)
        increcheck(True, ender)
        
print(f"Strength: {signalsum}")

