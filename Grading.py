print("Nama  : Alfeen")
print("Prodi : Teknik Informatika")
print("NIM   :",12345678)

print("="*40)

nilai= 66
if nilai>100 or nilai<0:
    print("Nilai tidak valid!")
else:
    if 85<=nilai<=100:
        grade = "A"
        notes = "Baik Sekali"
    elif 75<=nilai<=84:
        grade = "B"
        notes = "Baik"
    elif 65<=nilai<=74:
        grade = " C"
        notes = "Cukup"
    elif 64<=nilai<=55:
        grade = "D"
        notes = "Buruk"
    else:
        grade = "E"
        notes = "Sangat Buruk"

    print("Nilai akhir anda adalah :",nilai)
    print("Grade                   :",grade)
    print("Keterangan              :",notes)