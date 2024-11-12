print('='*10,'ADMIN','='*10)
dataLength= int(input('Masukkan banyak buku yang ingin di input :\n'))
datas=[]

n=1
while n <=dataLength:
    inputBook=input(f'Masukkan buku Ke-{n}:\n')
    datas.append(inputBook)
    n+=1

print('='*37)
print('berikut adalah daftar buku yang berhasil dimasukkan','\n',datas)
datas_lower=[data.lower() for data in datas]
print('='*37)

validateContinue=input('Apakah anda ingin lanjut mencari buku? (y/n)\n')
if validateContinue != "y":
    exit()

print("\n","="*10,'PENCARIAN MAPEL',"="*10)
cari=input('Masukkan buku yang ingin dicari :')
print("="*37)

for index,i in enumerate(datas):
    if cari.lower() in i.lower() in datas_lower:
        print(f'Hasil yang relevan dengan kata {cari} adalah : {i} ,ada pada rak {index}')





