#bai 1 tao ra 1 lop co name va 3 doi tuong mon hoc trong ham tao
#sau do tao method tinh trung binh cong
class Monhoc:
    def __init__(self,name,toan,van,anh):
        self.name=name
        self.toan=toan 
        self.van=van 
        self.anh=anh
    
    def Avergen(self):
        trungbinh=(self.toan+self.van+self.anh)/3
        return trungbinh

s1=Monhoc("Dung",9,8,10)
print(s1.Avergen())     

#tao lop tai khoan ngan hang co so du va tai khoan ghi no neu co
class Bank():
    def __init__(self,money,numberb):
        self.money=money
        self.numberb=numberb
    def Checkno(self,ghino):
        self.money-=ghino
        print("So no cua ban",ghino)
        print("tong so du",self.Get_banlance())
    def Checksodu(self,ghino):
        self.money+=ghino
        print("So co cua ban",ghino)
        print("tong so du",self.Get_banlance())
    def Get_banlance(self):
        return self.money


acc1=Bank(100000,"1234")
acc1.Checkno(2000)
acc1.Checksodu(2000)
