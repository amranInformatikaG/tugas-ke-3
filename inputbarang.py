#add,remov,updat,m.index,mencri keberadaanvalue#
data_indeks = []
jumlah_barang = int(input("masukkan jumlah value :"))
for s in range (jumlah_barang):
    barang =(input("masukkan nama barang :"))
    data_indeks.append(barang)
print(data_indeks)
print("""pengeditan !\n
      1.tampilkan value
      2.menambah barang
      3.mengubah barang
      4.pencarian index barang
      5.menentukan apakah barang terdapat di dalam variabel list
      6.menghapus barang""")
print("masukkan slah satu angka\n di atas untuk mengedit")
edit = int(input("masukkan salah satu angka di atas untuk mengedit :"))
if edit == 1:
    print(data_indeks)
elif edit == 2:
    data_indeks.append(input("masukkan barang :"))
    print(data_indeks)
elif edit == 3:
    data_indeks[int(input("masukkan index yang ingin di edit :"))]=input("masukkan barang :")
    print(data_indeks)
elif edit == 4:
    print(data_indeks.index(input("masukkan value untuk mencari psisi indeks :")))
elif edit == 5:
    barang1= input("masukkan barang yang ingin di cari :")
    if barang1 in data_indeks:
        print("barang ada di dalam variabel")
    elif barang1 not in data_indeks:
        print("barang tidak di temukan di dalam indeks")
elif edit == 6:
    data_indeks.remove(input("masukan value yang ingin di hapus :"))
    print(data_indeks)
else:
    print("perintah salah")