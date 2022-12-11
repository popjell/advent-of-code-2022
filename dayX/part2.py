
filename = str(input())

commands = open(filename, "r").read().split("\n")

cycle = 0

X = 1

nextcheck = 20

signalsum = 0

rows, cols = (6,40)

crt = [[' ' for i in range(cols)] for j in range(rows)]

row = 0
pixel = 0

def increcheck(increment, val):
    global crt
    global cycle
    global X
    global row
    global pixel
    cycle += 1
    row = int(cycle/40)
    if cycle % 40 == 0 and cycle >= 40:
        row -= 1
    pix = cycle - (row * 40) - 1
    if pix >= X - 1 and pix <= X + 1:
        crt[row][pix] = '#'
    if increment:
        X += val


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
        
        
for i in range(rows):
    for j in range(cols):
        print(crt[i][j], end = '')
    print('')

