try:
    f1=open('Meritlist.txt','r')
    l1=[]
    while(True):
        x=f1.readline()
        if(x!=''):
            l1.append(x.split(','))
        else:
            break
except:
    print('exception')  
else:
    phy=[]
    chem=[]
    math=[]
    for x in l1:
        if(x[2] not in phy):
            phy.append(float(x[2])) 
        if(x[3] not in phy):
            chem.append(float(x[3])) 
        if(x[4] not in phy):
            math.append(float(x[4]))
    f2=open('newfile3.txt','w')
    f2.write('Physics Meritlist\n')
    phy.sort(reverse=True)
    for y in phy:
      for x in l1:
          if(y==float(x[2])):
              f2.write('Name:'+x[0]+' Roll no.:'+x[1]+'Marks:'+str(x[2])+'\n')
    f2.write('Chemistry Meritlist\n')
    chem.sort(reverse=True)
    for y in chem:
      for x in l1:
          if(y==float(x[3])):
              f2.write('Name:'+x[0]+' Roll no.:'+x[1]+'Marks:'+str(x[3])+'\n')
    f2.write('Maths Meritlist\n')
    math.sort(reverse=True)
    for y in math:
      for x in l1:
          if(y==float(x[4])):
              f2.write('Name:'+x[0]+' Roll no.:'+x[1]+'Marks:'+str(x[4])+'\n')                    

                                      