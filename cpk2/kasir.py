print("#=================================================#")
print("|                   Program Kasir                 |")
print("|                 Created By Anggie               |")
print("|                    (210601007)                  |")
print("#=================================================#")
print(" ")

jumlah = int(input("Masukan Jumlah : "))
setelah_diskon = jumlah

if jumlah>=15000000:
        diskon = jumlah * (10/100)
elif jumlah>=25000000:
        diskon = jumlah * (12.5/100)
elif jumlah>=35000000:
        diskon = jumlah * (15/100)
elif jumlah>=60000000:
        diskon = jumlah * (20/100)
setelah_diskon = jumlah - diskon
jmlTot = setelah_diskon
ubayar = int(input("Masukan uang yang akan dibayarkan : "))
kmbl = ubayar - jmlTot 
print(" ")

print("#=================================================#")
print("|                       Struk                     |")
print("#=================================================#")
print("|=================================================|")
print("| Jumlah                  :             ",jumlah,"|")
print("| Diskon                  :             ",diskon,"|")
print("| Total bayar             :             ",jmlTot,"|")
print("| Uang Yang Diberikan     :             ",ubayar,"|")
print("| Uang kembali            :             ",kmbl  ,"|")
print("#=================================================#")
print(" ")
uang = kmbl
uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 100]
jumlah_pecahan = {}
sisa = uang
print("#=================================================#")
print("Jumlah uang kembali {} : ".format(uang))
for pecahan in uang_pecahan:
        if sisa < pecahan:
                continue
        banyak_pecahan = int(sisa/pecahan)
        sisa = sisa - (pecahan * banyak_pecahan)
        print("Pecahan uang kemabali {} : {} ".format(pecahan, banyak_pecahan))
print("#=================================================#")        