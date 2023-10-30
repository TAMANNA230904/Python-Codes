class Person:
    def __init__(s,n,add,dob):
        s.n=n
        s.add=add
        s.dob=dob
    def p_display(s):
        print(s.n,s.add,s.dob)
class Employee(Person):
    def __init__(s,id,desg,n,add,dob):
        s.id=id
        s.desg=desg
        Person.__init__(s,n,add,dob)
    def e_display(s):
        print(s.id,s.desg,end=' ')
        Person.p_display(s)
class Admin:
    def __init__(s,privilege):
        s.privilege=privilege
    def a_display(s):
        print(s.privilege)


p=Person('Ram','Gwalior','1999-07-20')
e=Employee(23,'HR','Ram','Gwalior','1999-07-20')
a=Admin('r&w')
p.p_display()
e.e_display()
a.a_display()

