class student:
    l1=[]
    l2=[]
    l3=[]
    d1={}
    d2={}
    d3={}
    def __init__(s,n,id,sem,cgpa):
        s.detail=[cgpa,n,id,sem]
        if(s==1):
            student.l1.append(s.detail)
        elif(s==2):
            student.l2.append(s.detail)
        else:
            student.l3.append(s.detail)
    @staticmethod
    def displayMeritlist():
        student.l1.sort(reverse=True)
        for i,x in enumerate(student.l1):
            student.d1[i+1]=x
        student.l2.sort(reverse=True)
        for i,x in enumerate(student.l2):
            student.d2[i+1]=x
        student.l3.sort(reverse=True)
        for i,x in enumerate(student.l3):
            student.d3[i+1]=x  
        print('Sem 1-\n',student.d1)
        print('Sem 2-\n',student.d2)
        print('Sem 3-\n',student.d3)
while(True):
    ch=input('Enter 1 to register and 2 to display')
    if(ch=='1'):
        stu=student(input('Enter name:'),input('Enter id:'),int(input('Enter sem:')),float(input('Enter cgpa:')))
    else:
        student.displayMeritlist()
        break    
