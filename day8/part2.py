txt = open("input.txt", "r").read().split("\n")
for i in range(len(txt)):
    arr = [x for x in txt[i]]
    txt[i] = arr
highest = 0

for i in range(len(txt)):
    for j in range(len(txt[i])):
        height = int(txt[i][j])
        t = 0
        b = 0
        l = 0
        r = 0
        for k in range(j - 1, -1,-1):
            integer = int(txt[i][k])
            b += 1
            if integer >= height:
                break
        for k in range(j + 1, len(txt[i])):
            integer = int(txt[i][k])
            t += 1
            if integer >= height:
                break
        for k in range(i - 1,-1,-1):
            integer = int(txt[k][j])
            l += 1
            if integer >= height:
                break
        for k in range(i + 1, len(txt[i])):
            integer = int(txt[k][j])
            r += 1
            if integer >= height:
                break
        viewscore = r*l*b*t
        if viewscore > highest:
            highest = viewscore
print(highest)
            
        
        
        