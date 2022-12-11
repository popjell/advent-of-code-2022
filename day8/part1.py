txt = open("input.txt", "r").read().split("\n")
for i in range(len(txt)):
    arr = [x for x in txt[i]]
    txt[i] = arr
total = 0
for i in range(len(txt)):
    for j in range(len(txt[i])):
        if i == 0 or j == 0 or j == len(txt[i]) - 1 or i == len(txt):
            total += 1
            continue
        height = int(txt[i][j])
        #check top
        botvisible = True
        topvisible = True
        Sidevisible = True
        Rightvisible = True
        for k in range(0, j):
            integer = int(txt[i][k])
            if integer >= height:
                botvisible = False
                break
        for k in range(j + 1, len(txt[i])):
            integer = int(txt[i][k])
            if integer >= height:
                topvisible = False
                break
        for k in range(0,i):
            integer = int(txt[k][j])
            if integer >= height:
                Sidevisible = False
                break
        for k in range(i + 1, len(txt[i])):
            integer = int(txt[k][j])
            if integer >= height:
                Rightvisible = False
                break
        if botvisible or Sidevisible or topvisible or Rightvisible:
            total+=1
print(total)
            
        
        
        