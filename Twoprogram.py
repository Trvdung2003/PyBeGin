# bai tap 1 nhap ten nguoi dung lay ra do dai
# user1=input("Moi ban nhap ten cua ban");
# dodai = len(user1)
# print(user1)
# print(dodai)

#bai tap 2 diem
# diemso = int(input("Moi ban nhap vao so diem"))

# if(diemso >=90):
#     print("Grade=A")
# elif(diemso<90 and diemso>=80):
#     print("Grade=B")       
# elif(diemso<80 and diemso>=70):
#     print("Grade=C")
# else:
#     print("Grade=D")

# print("Ket thuc xep hang")

# kiem tra so chan hay le, kiem tra boi so chia so do ==0
# userso = int(input("Moi ban nhap so de kiem tra chan hay le"))
# if(userso%2==0):
#     print("so chan ban oi")
# else:
#     print("solecmnr")    

#tim so lon nhat trong 4 so
so1=int(input("Moi ban nhap so1"))
so2=int(input("Moi ban nhap so2"))
so3=int(input("Moi ban nhap so3"))
so4=int(input("Moi ban nhap so4"))

if(so1>so2 and so1>so3 and so1>so4):
    print("so lon nhat la so1: ",so1)
elif(so2>so3 and so2>so4):
    print("so lon nhat la so2:  ",so2)    
elif(so3>so4):
    print("so lon nhat la so3:  ",so3)
else:
    print("so lon nhat la so 4",so4)        