print('='*10,'DATA MATA PELAJARAN','='*10)
panjangdata= int(input('Masukkan banyak mapel :'))
datas=[]
i=1
while i <=panjangdata:
    matapelajaran=input(f'Masukkan Mata Pelajaran Ke-{i}:')
    datas.append(matapelajaran)
    i+=1
print('='*37)
print('berikut adalah mapel yang berhasil dimasukkan','\n',datas)
print('='*37)

lanjut=input('Apakah anda ingin lanjut mencari mapel? (y/n)')
if lanjut != "y":
    exit()

print("\n","="*10,'PENCARIAN MAPEL',"="*10)
cari=input('Masukkan kata kunci mapel yang ingin dicari :')
print("="*37)
hasil=[]

for data in datas:
    if cari in data:
        hasil.append(data)
if datas:
    print(f'Data yang mengandung kata "{cari}" ada pada mapel :')
    print('No | Mapel \t\t| index')
    for index,i in enumerate(hasil):
        print(f' {index + 1} | {i} \t| {index}')
else:
    print(f'Tidak ada data')






