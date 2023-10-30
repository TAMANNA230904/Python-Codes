#tax
try:
    f1=open('employee.txt','r')
    l1=[]
    while(True):
        x=f1.readline()
        if(x!=""):
            l1.append(x.split(','))
        else:
            break
except:
    print('exception')
else:
    taxdict={}
    f2=open('taxresult2.txt','w')
    for x in l1:
        taxIncome=0
        tax=0
        if(float(x[3])>150000):
            pf=150000 
        else:
            pf=float(x[3])
        taxIncome=float(x[2])-pf
        taxIncome-=500000
        if(taxIncome>0):
            tax=0.05*taxIncome
            if(taxIncome<500000):
                taxIncome=0
            else:
                taxIncome-=500000
        elif(taxIncome>500000):
            tax=0.1*taxIncome
            if(taxIncome<75000):
                taxIncome=0
            else:
                taxIncome-=750000
        elif(taxIncome>750000):
            tax=0.15*taxIncome
            if(taxIncome<1000000):
                taxIncome=0
            else:
                taxIncome-=1000000
        else:
            tax=taxIncome*0.2  
        tax-=float(x[4])
        taxdict[int(x[1])]=tax 
        f2.write('Name:'+str(x[0])+'id:'+str(x[1])+'tax payable:'+str(tax)+'\n')                   

                               

