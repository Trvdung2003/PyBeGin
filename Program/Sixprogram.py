# #bai 1 viet tinh do dai cua list ,lits la tham so
# def tinhdodailst(listt):
#     print(len(listt)) 
# def xuatraphantu(litss):
#     for item in litss:
#         print(item, end="")
# def timgiaithua(n):
#     sum=1
#     for i in range(1,n+1):
#         if(n==0):
#             print("giai thua cua 0 la: 1")
#         sum=sum*i
#     print("giai thua cua ",n,"la",sum)
       
# timgiaithua(0)
# tinhdodailst([1,2,3,4])
# xuatraphantu([1,2,3,4,5,6])

# bai tap ve nha viet ham kiem tra so le chan
# def checkk(number):
#     if(number%2==0):
#         print(number,"is even")
#     else:
#         print(number,"is odd")
# n = int(input("Moi ban nhap so vao kiem tra"))
# checkk(n)
# print("de quyyyyyyyyyy")

# de quyyyyyyyyyyyy
# def fact(m):
#     if(m==0 or m==1):
#         return 1
#     else:
#         return m*fact(m-1)
# print(fact(6))

#de quy tinh tong
def fact2(number):
    if(number==0):
        return 0
    return number+fact2(number-1)

print(fact2(2))

#de quy in danh sach list
def InraList(listt,index=0):
    if(index==len(listt)):
        return
    print(listt[index])
    InraList(listt,index+1)

fud =["banan","apple","orange"]
InraList(fud)