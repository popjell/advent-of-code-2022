input = open("input.txt", "r").read().split("\n")

class Directory:
  def __init__(self, parent = None):
    self.directories = []
    self.parent = parent if parent is not None else "null"
    self.filesize = 0

root = {"name": "\\", "direc": Directory()}

root["direc"].parent = root

parentdirectory = root
currentdirectory = root
directorynames = ["\\"]
directories = [root]
listing = False

def parsecommand(cmd):

    print(commandheader)
    if commandheader == "$ls":
        print("list")
        global listing
        listing = True
        return  
    elif commandheader == "$cd":
        global parentdirectory
        global currentdirectory
        if cmd == "$cd ..":
            parent = currentdirectory["direc"].parent
            currentdirectory = parent
            parentdirectory = currentdirectory["direc"].parent
        else:
            parentdirectory = currentdirectory["direc"].parent
            name = cmd[4::]
            directory = next(item for item in currentdirectory["direc"].directories if item["name"] == name)
            currentdirectory = directory
    return
            
            
    
for i in range(len(input)):
    cmd = input[i]
    commandheader = cmd[0:cmd.index(" "):]
    print(cmd)
    print(listing)
    if cmd[0] == "$":
        listing = False
        parsecommand(cmd)
    elif listing:
        if cmd[0].isnumeric() == True:
            size = int(cmd[0:cmd.index(" ")])
            currentdirectory["direc"].filesize += size
        elif cmd[0] == 'd':
            name = cmd[4::]
            if name not in currentdirectory["direc"].directories:
                print("appende", end=" ")
                print(name)
                directorynames.append(name)
                newdir = {"name": name, "direc": Directory()}    
                newdir["direc"].parent = currentdirectory
                directories.append(newdir)
                currentdirectory["direc"].directories.append(newdir)
                print(currentdirectory["direc"].directories)
                print(newdir)
        elif cmd[0] == "$":
            listing = False
            parsecommand(cmd)

    
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
arr = []
def calc(direc):
    global arr
    files = direc["direc"].filesize
    print(direc["name"],end = "{\n")
    print(files)
    print("\n")
    name = direc["name"]
    dirlen = len(direc["direc"].directories)
    for i in range(dirlen):
        print("a\n")
        childsize = calc(direc["direc"].directories[i])
        files += childsize
    direc["direc"].filesize = files
    print(f"}}end {name}")
    print(files)
    print("\n\n")
    arr.append(files)
    return direc["direc"].filesize

used = calc(root)
total = 70000000
unused = total - used
necessary = 30000000 - unused
print("u" + str(unused))

arr.sort(reverse=True)
valid = []
for i in range(len(arr)):
    size = arr[i]
    if necessary - size <= 0:
        valid.append(size)
    else:
        break

valid.sort()    

print(valid[0])

    




    


        
        
        
    
    

