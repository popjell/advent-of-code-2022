filename = str(input())
commands = open(filename, "r").read().split('\n')

head = {"x":0, "y":0}
tail = {"x":0, "y":0}
pasthead = {"x":0, "y":0}

ydirections = {
    "U":1,
    "D":-1,
    "R":0,
    "L":0
}

xdirections = {
    "U":0,
    "D":0,
    "R":1,
    "L":-1
}


positions = []
count = 0


def followtail():
    global positions
    global count
    global head
    global tail
    x = head["x"]
    y = head["y"]
    if y > tail["y"] + 1:
        if x > tail["x"]:
            tail["x"] += 1
        elif x < tail["x"]:
            tail["x"] -= 1
        tail["y"] += 1
    elif y < tail["y"] - 1:
        if x > tail["x"]:
            tail["x"] += 1
        elif x < tail["x"]:
            tail["x"] -= 1
        tail["y"] -= 1
    if x > tail["x"] + 1:
        if y > tail["y"]:
            tail["y"] += 1
        elif y < tail["y"]:
            tail["y"] -= 1
        tail["x"] += 1
    elif x < tail["x"] - 1:
        if y > tail["y"]:
            tail["y"] += 1
        elif y < tail["y"]:
            tail["y"] -= 1
        tail["x"] -= 1
    if str(tail) not in positions:
        positions.append(str(tail))
        count += 1
    return

for i in range(len(commands)):
    direction = commands[i][0]
    amount = int(commands[i][2])
    if len(commands[i]) > 3:
        amount *= 10
        amount += int(commands[i][3])
    print(direction)
    print(amount)
    for j in range(amount):
        pasthead["x"] = head["x"]
        pasthead["y"] = head["y"]
        head["x"] += xdirections[direction]
        head["y"] += ydirections[direction]
        followtail()

    print("head", end = ":")
    print(head)
    print("tail", end = ":")
    print(tail)

                

positions.sort()
print(positions)
print(len(positions))
print(count)


