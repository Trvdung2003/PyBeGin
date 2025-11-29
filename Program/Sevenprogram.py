# bai 1 tao file moi va add noi dung
# f = open("practice.txt","a")
# f.write("""
# Hi everyone
# we are learning File I/O
# using Java
# i like programming in Java
#         """)
# print(f)

# chua bai 1
with open("practice1.txt","r") as f:
    # f.write("Hi everyone\n we are learning File I/O\n using Java\n I like programming in Java")
    data = f.read()
# newdata=data.replace("Java","Python")
    word="learning"
    if(data.find(word)):
        print(-1)
    else:
        print(0)
