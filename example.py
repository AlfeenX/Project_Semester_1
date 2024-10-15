panjang=int(input("Masukkan panjang deret ="))
kelipatan=int(input("Masukkan jumlah kelipatan ="))
awalan=int(input("Masukan Angka awal ="))
pilih=int(input("pilih kelipatan (1.perkalian/2.penjumlahan) pilih menggunakan angka (1/2 ="))
i=1
data_deret=[]
data_deret.insert(0,awalan)
if pilih == 1:
    while i < panjang:
        deret=awalan*kelipatan
        awalan=deret
        data_deret.append(deret)
        i+=1
    print("=========Output========")
    print(data_deret)
elif pilih==2:
    while i < panjang:
        deret=awalan + kelipatan
        awalan=deret
        data_deret.append(deret)
        i+=1
    print("=========Output========")
    print(data_deret)
else:
    print("Maaf Pilihan Anda Tidak Ada")



