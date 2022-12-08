
####################################
# Document

from asyncio.windows_events import NULL


class Document:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def __str__(self):
        return self.name + "\n"
        

####################################
# Folder

class Folder:

    def __init__(self,name,parent):
        self.name = name
        self.parent = parent
        self.folders = []
        self.documents = []

    def __str__(self):
        string=self.name + "\n"
        for x in self.folders:
            string+=str(x)
        for y in self.documents:
            string+=str(y)
        return string

    def getSize(self):
        size = 0

        for doc in self.documents:
            size+=doc.size

        for fold in self.folders:
            size+=fold.getSize()

        return size

    def addFolder(self, name):
        self.folders.append(Folder(name,self))

    def addDocument(self, name, size):
        self.documents.append(Document(name,size))

    def getFolder(self,name):
        for x in self.folders:
            #print(x.name)
            if x.name == name:
                return x
    
    def folderSizes(self,resultArray):
        size = int(0)

        for fold in self.folders:
            size+=fold.getSize()
            fold.folderSizes(resultArray)

        for doc in self.documents:
            size+=doc.size

        resultArray.append(size)
        

####################################
# Reading data

file = open("input.txt","r")

lst = [line[:-(line[-1] == '\n') or None] for line in file]

#print(lst)

rootFolder = Folder("root",NULL)
currentFolder = rootFolder

for line in lst:
    command = line.split()
    #print(command)

    if(command[0]=="$"):
        #print("command")

        if(command[1]=="cd"):
            if(command[2]==".."):
                currentFolder=currentFolder.parent

            elif(command[2]=="/"):
                currentFolder=rootFolder

            else:
                currentFolder=currentFolder.getFolder(command[2])

        
    else:
        #print("content")
        if(command[0]=="dir"):
            currentFolder.addFolder(command[1])

        else:
            currentFolder.addDocument(command[1],command[0])

folderSizes = []
rootFolder.folderSizes(folderSizes)
folderSizes.sort()

#print(folderSizes)




sumSmallFolders=0
for fold in folderSizes:
    if fold<100000:
        sumSmallFolders+=fold
print("Sum small folders: {}".format(int(sumSmallFolders)))


capacity=70000000
print("Capacity: {}".format(capacity))
needed=30000000
print("Needed space: {}".format(needed))

usedSpace=rootFolder.getSize()
print("Used space: {}".format(usedSpace))

unusedSpace = capacity-usedSpace
print("Unused space: {}".format(unusedSpace))

toFree=needed-unusedSpace
print("Need to free: {}".format(toFree))


folderToDelete=0
for fold in folderSizes:
    if fold>toFree:
        folderToDelete=fold
        break
print("Size of folder to delete:  {}".format(folderToDelete))