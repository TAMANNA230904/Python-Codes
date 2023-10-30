class Bill:
    item_cost={'hp-laptop':50000,'iphone':75000,'marker':25}
    item_stock={'hp-laptop':10,'iphone':2,'marker':20}
    tax=0.18
    billno=0
    def __init__(s,id,name,date,ass_cust_id,discount):
        s.id=Bill.billno+1
        s.name=name
        s.ass_cust_id=ass_cust_id
        s.discount=discount
        s.items=dict()
    def generate(s) :
        cost=0
        for x in s.items:
            if(s.items[x]<Bill.item_stock[x]):
                Bill.item_stock[x]-=s.items[x]
                cost+=s.items[x]*Bill.item_cost[x]
            else:
                return -1
            cost-=cost*s.discount
            cost+=cost*Bill.tax
        return cost        

class Customer:
    def __init__(s,n,id):
        s.n=n
        s.id=id
        s.cust_bill=Bill(n,1,'20-11-2020',s.id,0.25)
    def purchase(s):
        
        while(True):
            ch=int(input('Enter 1 to buy an item 2 to exit and generate bill'))
            if(ch==1):
                print('Write the product you want to buy') 
                for x in Bill.item_stock:
                    print(x,end=',')
                product=input('write product')
                quantity=int(input('Enter quantity'))
                s.cust_bill.items[product]=quantity
            else:
                if(s.cust_bill.generate()==-1):
                    print('BILL ERROR')
                    break
                else:
                    print('Please pay',s.cust_bill.generate())
                    break               
    def display(s):
        print('Bill id-',s.id,'Customer name-',s.n,'Item-list',s.cust_bill.items)   
c=Customer('Ram',23)
c.purchase()                     
