class Bank:
    def __init__(self,name,acc_no,bal,loan):
        self.name = name
        self.__account = acc_no
        self.__balance = bal
        self.loan = loan
    def get_account(self):
        return self.__account,self.__balance

    def customer(self):
        print(f"{self.name} he is the one of the important customer")
class Personal(Bank):
    def __init__(self,pwd,name,acc_no,bal,loan):
        super().__init__(name,acc_no,bal,loan)
        self.pwd = pwd

    def customer(self):
        return super().customer()

cn = Bank("suraj",5240000035,120000.11,1)
print(cn.name,cn.loan)

print(cn.get_account())

cn.customer()

p = Personal(2025,"srj",2522004466,1200254,2)
print(p.pwd,p.name)

p.customer()