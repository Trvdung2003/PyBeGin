lam viec voi file
1)cach mo file
f = open("namefie","kieudochayviet")
vd f = open("ga.txt",r) r la read , w la chua co thi tao file moi,a neu chua co file tao file moi va viet luon
.read() # doc file, neu truyen tham so vao nhu so thi chi doc bao nhieu do ky tu
.readline() #doc 1 dong
.write(noidung can viet dong moi vao file)
.close() # dong file

<!--  -->

with open("file.txt","a") as f:
data=f.read()
print(data)

<!--  -->

import os
os.remove(filename)
