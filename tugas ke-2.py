#list
r=["kamu",1,2.1,"roti"]
#DICTIONARY
g={"nama":"amran","umur":"18"}
#set
h={"meja","kursi",1}
#tuple
b=("bola","sepatu",5,5,5,5,1.2)
for s in (r,g,h,b):
    print(s)
print("===========peng update value===========")
print("===========list============")
r[0]="saya"
print(r)
print("===============dic=============")
g["nama"]="doraemon"
print(g)
print("=========list=========")
r.append("gajah")
print(r)
print("======dic======")
g["jk"]="laki2"
print(g)
print("==========set============")
h.add("hp")
print(h)
print("=====remove=======")
print("list")
r.pop(0)
print(r)
print("====dic=======")
g.pop("jk")
print(g)
print("====set======")
h.remove("meja")
print(h)
print("pencaian fungsi tuple")
print(b.index(1.2))