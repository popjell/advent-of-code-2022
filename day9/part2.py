filename = str(input())
commands = open(filename, "r").read().split('\n')

first = {"x":0, "y":0}
one = {"x":0, "y":0}
two = {"x":0, "y":0}
three = {"x":0, "y":0}
four = {"x":0, "y":0}
five = {"x":0, "y":0}
six = {"x":0, "y":0}
seven = {"x":0, "y":0}
eight = {"x":0, "y":0}
nine = {"x":0, "y":0}


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


def followtail(head, tail):
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
    return {"x":tail["x"],"y":tail["y"]}

for i in range(len(commands)):
    direction = commands[i][0]
    amount = int(commands[i][2])
    if len(commands[i]) > 3:
        amount *= 10
        amount += int(commands[i][3])
    for j in range(amount):
        first["x"] += xdirections[direction]
        first["y"] += ydirections[direction]
        one = followtail(first, one)
        two = followtail(one, two)
        three = followtail(two, three)
        four = followtail(three, four)
        five = followtail(four, five)
        six = followtail(five, six)
        seven = followtail(six, seven)
        eight = followtail(seven, eight)
        nine = followtail(eight, nine)
        string = str(nine)
        if string not in positions:
            positions.append(string)
            count+= 1

                

positions.sort()
print(count)


