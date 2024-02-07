#set up a file
class TstudentRecord :
    def __init__(self):
        self.name = ""
        self.address = ""
        self.className = ""
studFile = open("Student.txt","w")
mystud = TstudentRecord()
mystud.name = 'Orkid Osman'
mystud.className = '2 Seroja'
mystud.address = 'My House'
print("name: ",mystud.name,"class: ",mystud.className,"address: ",mystud.address)
#write
studFile.write(mystud.name)
studFile.write("\n")
studFile.write(mystud.className)
studFile.write("\n")
studFile.write(mystud.address)
studFile.close()
#append
studFile = open("Student.txt", "a")
mystud.name = 'naqib'
mystud.className = 'al22.4'
mystud.address = 'here'
studFile.writelines(mystud.name)
studFile.writelines("\n")
studFile.writelines(mystud.className)
studFile.writelines("\n")
studFile.writelines(mystud.address)
studFile.close()
#read
studFile = open("Student.txt", "r")
data = studFile.readlines()
data.sort()
for i in range(len(data)):
    print(data[i])
#modify input from user
StudsFile = open("Students.txt", "w")
name = input('enter your name ')
mystud.name = name
classname = input('enter your class ')
mystud.className = classname
address = input('enter your address ')
mystud.address = address
StudsFile.write(mystud.name)
StudsFile.write("\n")
StudsFile.write(mystud.className)
StudsFile.write("\n")
StudsFile.write(mystud.address)
