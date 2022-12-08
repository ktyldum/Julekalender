import re

Test = True
part = 2

####################################
# Reading data

file = "test.txt" if Test else "input.txt"

fp = open(file,"r")
lst = [line[:-(line[-1] == '\n') or None] for line in fp]

####################################
# Find empty dividing line
emptyline = lst.index("")

####################################
# Find number of Columns
numColumns=len(lst[emptyline-1].split())
 
####################################
# Initiate Columns
columns=[]
for a in range(numColumns):
    columns.append([])

####################################
# Parse and establish Columns
for a in reversed(range(0,emptyline-1)):
    layer = re.findall('....?',lst[a])
    for b in range(0,len(columns)):
        crate = re.sub("\ |[\[\]]", "", layer[b])
        if crate != "":
            columns[b].append(crate)

####################################
# Print Columns
   
print(columns)

####################################
# Juggle crates

##Parse commands
for c in range(emptyline+1,len(lst)):
    command = lst[c].split()
    print(command)

    if part==1:
        #for a number of crates
        for i in range(int(command[1])):
            #pick one crate from column a
            crate = columns[int(command[3])-1].pop()
            #put crate on column b
            columns[int(command[5])-1].append(crate)

        print(columns)
        
    else:
        crates=[]
        #for a number of crates
        #pick up all the crates from column a with crane
        for i in range(int(command[1])):
            crates.append(columns[int(command[3])-1].pop())

        #put all crates on column b
        for i in range(len(crates)):
            columns[int(command[5])-1].append(crates.pop())

        print(columns)

####################################
# Get top crates
topcrates = ""
for column in columns:
    topcrates+=column.pop()

print(topcrates)
