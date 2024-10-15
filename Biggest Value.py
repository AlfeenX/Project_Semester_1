print("Nama  : Alfeen")
print("Prodi : Teknik Informatika")
print("NIM   :",12345678)

print("="*40)

x=100
y=500
z=300
a=40

if x>=y and x>=z and x>=a:
    terbesar = x
elif y>=x and y>=z and y>=a:
    terbesar = y
elif a>=x and a>=y and a>=z:
    terbesar = a
else:
    terbesar = z

print("bilangan terbesar saat ini =", terbesar)