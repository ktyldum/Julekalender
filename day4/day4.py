
from msilib.schema import File

counter=0
counter2=0

myFile = open("input.txt","r")

myLine = myFile.readline().strip()

while myLine:
    
    print("\n" + myLine)
    
    elfpair = myLine.split(",")
    
    elf1=elfpair[0].split("-")
    elf2 =elfpair[1].split("-")

    print(elfpair)
    print(elf1)
    print(elf2)

    if int(elf1[0])<=int(elf2[0]) and int(elf2[1])<=int(elf1[1]):
        counter+=1
        print("#")
        print(elf1[0] + "<=" + elf2[0] + "<=" + elf2[1] + "<=" + elf1[1])


    elif int(elf2[0])<=int(elf1[0]) and int(elf1[1])<=int(elf2[1]):
        counter+=1
        print("#")
        print(elf2[0] + "<=" + elf1[0] + "<=" + elf1[1] + "<=" + elf2[1])

##Overlapp

    elif int(elf1[0])<int(elf2[0]) and int(elf1[1])>=int(elf2[0]):
        counter2+=1
        print("##")
        print(elf1[0] + "<" + elf2[0] + elf1[1] + "=>" + elf1[0])


    elif int(elf1[0])<=int(elf2[1]) and int(elf1[1])>int(elf2[1]):
        counter2+=1
        print("##")
        print(elf1[0] + "<=" + elf2[1] + elf1[1] + ">" + elf2[1])

    myLine=myFile.readline().strip()

print(counter)
print(counter2)
print(counter+counter2)