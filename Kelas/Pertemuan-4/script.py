#Modul 6 Perulangan

print("Perulangan ke 0")
print("Perulangan ke 1")
print("Perulangan ke 2")
print("Perulangan ke 3")
print("Perulangan ke 4")
print("Perulangan ke 5")
print("Perulangan ke 6")
print("Perulangan ke 7")
print("Perulangan ke 8")
print("Perulangan ke 9")
print("Perulangan ke 10")

batas = 20
for i in range(1, batas, 2):
    print(f"Perulangan ke{i}")

buah_banyak = ("Apel", "Mangga", "Anggur", "Semangka")
for buah in buah_banyak:
    print(buah)

for baris in range (1,4):
    print("Baris ke", baris)
    for kolom in range (1,4):
        print(kolom, "kolom", end=" ")
    print()
    print()

#Infinity Loop

# while True:
   # print("Hello World")

# while "Hello":
   # print("Hello")

lagi = "yes"
ulang = 0
while lagi == "yes":
    ulang += 1
    print("Mabar")
    lagi = input ("Mabar lagi gak? ")
print("Selesai Mabar!")
print(f"Perulangan Terjadi sebanyak {ulang} kali")

for i in range(1,10):
    if i == 4:
        break
    else:
        print(f"Perulangan ke {i}")

for i in range (1,4):
    print("Baris ke", i)
    for kolom in range (1,4):
        print(kolom, "kolom", end=" ")
    print()

buah_banyak = ("Apel", "Mangga", "Anggur", "Semangka")
for buah in buah_banyak:
    if buah == "Anggur":
        print("Buah Anggur Ketemu")
        break
    else:
        print("Belum Ketemu")

while True:
    ulang = input("Mabar lagi: ")
    if ulang.lower() == "gak":
        break
    print("Mabar lagi")

for i in range (1,10):
    if i % 2 == 1:
        continue
    print(f"Perulangan ke {i}")

#Modul
print("Matrix")
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

print("Segitiga Siku Siku")
for i in range(1, 5):
    print("*" * i)

print("Segitiga Siku Siku")
for i in range(batas):
    print(" " * (batas - i)+ "i ")


kesempatan = 3
while kesempatan > 0:
    username = input("Masukkan username: ")
    password = input("Masukkan password : ")
    if username == "admin" and password == "admin1234":
        print("Berhasil login")
    break
else:
    print("Username atau password salah")
    kesempatan -= 1
    print(f"Kesempatan login tersisa {kesempatan} kali")
print("Program utama")