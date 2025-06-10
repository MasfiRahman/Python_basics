#file = open("student.txt","r")#reading file 
#file = open("student.txt","w")#writing file
#print(file.readable())#read check
file = open("student.txt","r+")#read and write
#print(file.writable())#write check
#text=file.read()
#print(text)
#size = len(text)
#print(size)
#text=file.readlines()
#text=file.readlines()[1]
#print(text)
for line in file:
    print(line)
file.close()