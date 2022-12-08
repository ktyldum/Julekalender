####################################
# Reading file

# opening the file
from re import I


file_obj = open("input.txt", "r")
  
# splitting the file data into lines
chars = file_obj.readline()
#print(chars)
file_obj.close()

####################################
# Moving frame

for i in range(len(chars)-3):
    frame = chars[i:i+4]
    
    #print(i)
    #print(frame)

    if len(set(frame)) == 4:
        print("Oppgave 1: {}".format(i+4))
        break

for i in range(len(chars)-13):
    frame = chars[i:i+14]
    
    #print(i)
    #print(frame)

    if len(set(frame)) == 14:
        print("Oppgave 2: {}".format(i+14))
        break


