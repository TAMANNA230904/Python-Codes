class Student:
    count=0
    def __init__(s):
        s.name=' '
        s.id=0
        s.cgpa=0.0
        Student.count+=1
    def studentcount(s):
        print('no.of students=',Student.count)
    def set(s):
        s.name=input('enter name')
        s.id=input('enter id')
        s.cgpa=float(input('enter cgpa'))    
    def display(s):
        print('Name:',s.name,'ID=',s.id,'CGPA=',s.cgpa)    

l=[]
while(True):
 ch=int(input('enter 1 to register 2 to display 3 to exit'))
 if(ch==1):
    s=Student()
    s.set()
    l.append(s)
 elif(ch==2):
    ch1=int(input('enter 3 to display all students 4 for particular student'))
    if(ch1==3):
        for x in l:
           x.display()
    else:
       l[int(input('enter position'))-1].display()
 else:
    break       
        

