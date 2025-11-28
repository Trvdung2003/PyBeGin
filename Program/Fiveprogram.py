#bai 1 in so tu 1 den 100
# i=1
# while i<=100:
#     print(i)
#     i+=1
# print("end")

# --------

#bai 2 in so tu 100 den 1 
# i=100
# while i>=1 :
#     print(i)
#     i-=1
    
#bai 3 bang cuu chuong 1 so nao day
# i2=1
# while i2<=10:
#     print(i2*2)
#     i2+=1;    
  
#luythua bai 4
# i=1
# while i<=10:
#     print(i*i)
#     i+=1
   
#tim gia tri trong list
# listtne=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i < len(listtne):
#     print(listtne[i])
#     i+=1


#dung vong for tim phan tu list
# list1=[1,2,3,4,5,6,7,8]
# for i in list1:
#     print(i)

#dung vong for tim x
# list2=[1,2,3,4,5,6,7,8]
# for i2 in list2:
#     if(i2==7):
#         print("da tim thay so 7 tai: ",i2)
#         break
#     print(i2)

#tim x ma ko dung vong for
# listnew=[1,2,3,4,5]
# x=5
# indexx=0
# while indexx <= len(listnew):  
#     if(listnew[indexx] ==5):
#         print("da tim thay 5 tai vi tri",indexx)
#         break
#     indexx+=1

# ----------- bai tap dung range
# bai 1 in so tu 1-100
# for i in range(1,101):
#     print(i) 

# bai 2 in so tu 100-1
# for i in range(100,0,-1):
#     print(i)

#bai 3 bang cuu chuong so nao day
# n = int(input("moi nhap so de hien bang cuu chuong"))
# for i in range(1,101):
#     if(i<=10):
#         print(i*n)

# ----------------------
#bai tap sau cau lenh pass
#tinh tong n so
n=int(input("Moi ban nhap n so de tinh tong: "))
sum=0
i=1
while i<=n:
    print("Cac so lan luot la: ",i)
    sum+=i
    i+=1
print("Tong cua cac so la: ",sum)

#tinh tong giai thua n so
m=int(input("Moi ban nhap m so de tinh giai thua "))
sum1=1
i1=1
while i1<=m:
    if(m==0):
        print("Giai thua cua 0 la: ",1)
    sum1*=i1
    i1+=1
print("Giai thua cua ",m,"la",sum1)    