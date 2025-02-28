class Bank:
    def __init__(self,acc_num,bal):
        self.acc_num=acc_num
        self.bal=bal
    def credit(self,camt):
        self.bal+=camt
        print("amount credited!!")
    def debit(self,damt):
        if self.bal<damt:
            print("no sufficient funds")
        else:
            self.bal-=damt
        print("amount debited")
    def get_bal(self):
        c=self.bal
        print(f"{c}")
acc_num=int(input("enter acc num "))
bal=float(input("enter account balance "))
b=Bank(acc_num,bal)
while True:
    print("enter 1 for credit")
    print("enter 2 for debit")
    print("enter 3 for balance display")
    print("enter 4 for exit")
    q=int(input())
    if q==1:
        camt=float(input("enter credit amount"))
        b.credit(camt)
    elif q==2:
        damt=float(input("enter debit amount"))
        b.debit(damt)
    elif q==3:
        b.get_bal()
    elif q==4:
        exit(0)
