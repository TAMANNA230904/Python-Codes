try:
 f1=open('f1.txt','r')
 l1=[]
 while(True):
        x=f1.readline()
        if(x!=""):
            l1.append(x.split(','))
        else:
            break
except:
    print('exception occured')
else:
 print('hello')
 semlist=[]
 for x in l1:
        if(x[2] not in semlist):
            semlist.append(x[2]) 
 f2=open('result2.txt','w')
 for x in semlist:
        l2=[]
        for y in l1:
            if(x==y[2]):
                l2.append(str(float(y[3]))+','+y[0]+','+y[1]+','+y[2])
        l2.sort(reverse=True)
        f2.write('Semester'+str(x)+'\n')
        print('Semester',x)
        for z in l2:
            temp=z.split(',')
            f2.write('Name:'+str(temp[1])+' Enrollment:'+str(temp[2])+' Semester:'+str(temp[3])+'CGPA:'+str(float(z[0])))
            print('Name:',temp[1],' Enrollment:',temp[2],' Semester:',temp[3],'CGPA:',float(z[0]))  
        


