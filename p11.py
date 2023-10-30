def check(s):
    if(len(s)>9 and [if(i==i.lower()) for i in s] and j==j.upper() for j in s and i in ['!','@','#','$','%','^','&'
,'*'] for i in s and i in ['1','2','3','4','5','6','7','8','9','0'] for i in s):
        return True
    else:
        return False
def register(d):
    user=input('Enter a username')
    if(check(user) and user not in d.keys()):
        d[user]=input('Enter a password')
        print('Registered successfully')
    else:
        print('Enter valid username') 

def pass_change(d,user):
    if(user in d.keys()):
        d[user]=input('Enter new password')
def login(d,user,psw):
    if(user in d.keys() and d[user]==psw ):
        print('You are successfully logged in')
    else:
        print('invalid username or password')    
n=int(input('Enter 1 to login 2 to register and 3 to change password'))
d={'Tamanna@23':'Tamanna','Anushka!11':'Anushka','Khushi@189tt':'khushi','Ankita*941':'Ankita','Nobitadora15^':'Nobita','Kiara167@gmail':'Kiara','Ramgarh44#':'ram','Dehradun#22':'ddy','Kimtaehyung&1':'V','Park*6Jimin':'Mochi'}
if(n==1):
    login(d,input('Enter username'),input('Enter pass'))  
elif(n==2):
    register(d)          
else:
    pass_change(d,input('Enter username'))