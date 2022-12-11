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

    if commandheader == "$ls":
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
                directorynames.append(name)
                newdir = {"name": name, "direc": Directory()}    
                newdir["direc"].parent = currentdirectory
                directories.append(newdir)
                currentdirectory["direc"].directories.append(newdir)
        elif cmd[0] == "$":
            listing = False
            parsecommand(cmd)

    
arr = []
def calc(direc):
    global arr
    files = direc["direc"].filesize
    name = direc["name"]
    dirlen = len(direc["direc"].directories)
    for i in range(dirlen):
        childsize = calc(direc["direc"].directories[i])
        files += childsize
    direc["direc"].filesize = files
    arr.append(files)
    return direc["direc"].filesize

total = calc(root)
def check(num):
    if num <= 100000:
        return True
    else:
        return False
    
lessthan_enumerator = filter(check, arr)
valid = list(lessthan_enumerator)
print(sum(valid))




    


        
        
        
    
    

