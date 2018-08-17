class Cust:
    """ cust app """
    cbname="sbi"
    def __init__(self,cname,cadd,cacno,cbal):
            self.cname=cname
            self.cadd=cadd
            self.cacno=cacno
            self.cadd=cadd
            self.cbal=cbal
    def deposit(self,damt):
            self.cbal=self.cbal+damt
    def withdraw(self,wamt):
            self.cbal=self.cbal-wamt
    def display(self):
            print(self.cname)
            print(self.cadd)
            print(self.cacno)
            print(self.cbal)
            print(Cust.cbname)
c1=Cust("vijaya lakshmi","solasa",1234,500000)
print(c1)
c1.deposit(40000)
c1.withdraw(50000)
c1.display()
c2=Cust("priyanka","guntur",5678,250000)
print(c2)
c2.deposit(20000)
c2.withdraw(30000)
c2.display()


