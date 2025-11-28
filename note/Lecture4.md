Dictionary & set
1)dict giong kieu oject co key va value,thay doi gia tri dc
info ={
"key":"value",
}

2)truy cap value cua phan tu
info["key"]

3)mot so method
list() # chuyen doi hien sang list
.keys() #tra ve cac key cua dict
.values() # tra ve cac value
.items() # lay ra ca key va value
.get("key")
.update(newDict)

---

set la tap hop du lieu giong nhau ko thay doi dc, ko trung lap dc
nums ={1,2,3,4}
1)tao set rong
newset =set()

2)set method
.add(pt) #them 1 phan tu
.remove(pt) #xoa 1 phan tu
.clear() #xoa het phan tu
.pop() #xoa 1 phan tu ngau nhien
.union(setkhac) #lay cac phan tu ca 2 set neu co gia tri khac nhau
.intersection(setkhac) # chi lay phan tu chung
