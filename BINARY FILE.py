#BINARY FILE 
import pickle

class teacherRecord :
    def __init__(self):
        self.name = ""
        self.subject = ""
        self.teacherid = ""
def write():
    myFile = open('teacher.DAT','w+b')
    myteacher = teacherRecord()
    myteacher.name = str(input('enter your name: '))
    myteacher.subject = str(input('enter your subject: '))
    myteacher.teacherid = str(input('enter your id: '))
    newRecord = myteacher.name + '' + myteacher.subject + '' + myteacher.teacherid
    pickle.dump(newRecord,myFile)
    myFile.close()
def read():
    myFile = open('teacher.DAT','rb')
    array = []
    for i in array:
        print(i)
    myFile.close()
def append():
    myFile = open('teacher.DAT', 'ab')
    myteacher = teacherRecord()
    myteacher.name = str(input('enter your name: '))
    myteacher.subject = str(input('enter your subject: '))
    myteacher.teacherid = str(input('enter your id: '))
    newRecord = myteacher.name + '' + myteacher.subject + '' + myteacher.teacherid
    pickle.dump(newRecord,myFile)
    myFile.close()
write()
read()
append()
