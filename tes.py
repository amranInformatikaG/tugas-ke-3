#string
nama="amran"
print(type(nama))
#integer
umur=18
print(type(umur))
#booleang(true and false)
mahasiswa=True
print(type(mahasiswa))
#float
ipk=3.4
print(type(ipk))

#operator aritmatika(+,-,/,%,*,**,//)
print("===============================")

gajipokok=10000000
gajilembur=1000000*2#jm
pajak=10/100
gajikotor=gajipokok+gajilembur
gkpajak=pajak*gajipokok
gajibersih=gajikotor-gkpajak
print("gaji pokok =",gajipokok)
print("gaji lembur =", gajilembur)
print("pajak =", pajak)
print("gaji kotor =", gajikotor)
print("jumlah tunjakan =",gkpajak)
print("gaji bersih =",gajibersih)

#perbandingan(>,<,>=,<=,==,!=)
print("===========================")
umur=13
if (umur >=1 and umur<=12):
    print("anak anak")
    
#percabangan if else
umur=34
if (umur >= 16 and umur <=18):
    print("remaja")
else:
    print("dewasa")
#elif    
print("==========================")
umur = 22
if (umur >=12 and umur <= 16):
    print("remaja")
elif (umur >= 17 and umur <=18):
    print("masa puber")
else:
    print("tidak ada yang memenuhi")
    
#logika(and or not)
# not
a = True
b = not a
print("variabel =",a)
print("not a =", b)
 # or
x=True
y=False
z=x or y
print(x,"or",y,"=",z)
x=False
y=False
z=x or y
print(x,"or",y,"=",z)
#and
print("======================")
a=True
b=False
c= a and b
print(a,'and',b,"=",c)

a=True
b=True
c= a and b
print(a,'and',b,"=",c)

