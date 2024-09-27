print("============================================================")
print("    Menu Program Menghitung Luas / Keliling Bangun Datar    ")
print("============================================================")
print("Menu Bangun Datar :")
print("1. Persegi :")
print("1.1 Luas")
print("1.2 Keliling")
print("2. Persegi Panjang")
print("2.1 Luas")
print("2.2 Keliling")
print("3. Segitiga")
print("3.1 Luas")
print("3.2 Keliling")
print("4. Jajar Genjang")
print("4.1 Luas")
print("4.2 Keliling")
print("5. Keluar")
print("============================================================")
menu = int(input("Pilih Nomor Menu Anda : "))
print("============================================================")
if menu == 1:
    kategori = float(input("Masukkan Nomor Kategori (Luas Atau Keliling) : "))
    if kategori == 1.1:
        print("Rumus Luas Persegi = sisi * sisi")
        sisi = float(input("Masukkan Sisi Persegi (cm) : "))
        luas = sisi * sisi
        print("Luas Persegi adalah :", float(luas), "cm")
        print("============================================================")

    elif kategori == 1.2:
        print("Rumus Keliling Persegi = 4 * sisi")
        sisi = float(input("Masukkan Sisi Persegi (cm) : "))
        keliling = 4 * sisi
        print("Keliling Persegi adalah :", float(keliling), "cm")
        print("============================================================")

    else:
        print("Error")

elif menu == 2:
    kategori = float(input("Masukkan Nomor Kategori (Luas Atau Keliling) : "))
    if kategori == 2.1:
        print("Rumus Luas Persegi Panjang = panjang * lebar")
        panjang = float(input("Masukkan Panjang Persegi Panjang (cm) : "))
        lebar = float(input("Masukkan Lebar Persegi Panjang (cm) : "))
        luas = panjang * lebar
        print("Luas Persegi Panjang Adalah :", float(luas), "cm")
        print("============================================================")

    elif kategori == 2.2:
        print("Rumus Keliling Persegi Panjang = 2 * (panjang + lebar)")
        panjang = float(input("Masukkan Panjang Persegi Panjang (cm) : "))
        lebar = float(input("Masukkan Lebar Persegi Panjang (cm) : "))
        keliling = 2 * (panjang + lebar)
        print("Keliling Persegi Panjang Adalah :", float(keliling), "cm")
        print("============================================================")

    else:
        print("Error")

elif menu == 3:
    kategori = float(input("Masukkan Nomor Kategori (Luas Atau Keliling) : "))
    if kategori == 3.1:
        print("Rumus Luas Segitiga = 1/2 * alas * tinggi")
        alas = float(input("Masukkan Alas Segitiga (cm) : "))
        tinggi = float(input("Masukkan Tinggi Segitiga (cm) : "))
        luas = 1/2 * alas * tinggi
        print("Luas Segitiga Adalah :", float(luas), "cm")
        print("============================================================")

    elif kategori == 3.2:
        print("Rumus Keliling Segitiga = Sisi a + Sisi b + Sisi c")
        a = float(input("Masukkan Sisi A Segitiga (cm) : "))
        b = float(input("Masukkan Sisi B Segitiga (cm) : "))
        c = float(input("Masukkan Sisi C Segitiga (cm) : "))
        keliling = a + b + c
        print("Keliling Segitiga Adalah :", float(keliling), "cm")
        print("============================================================")

    else:
        print("Error")

elif menu == 4:
    kategori = float(input("Masukkan Nomor Kategori (Luas Atau Keliling) : "))
    if kategori == 4.1:
        print("Rumus Luas Jajar Genjang = alas * tinggi")
        alas = float(input("Masukkan Alas Jajar Genjang (cm) : "))
        tinggi = float(input("Masukkan Tinggi Jajar Genjang (cm) : "))
        luas = alas * tinggi
        print("Luas Jajar Genjang Adalah :", float(luas), "cm")
        print("============================================================")

    elif kategori == 4.2:
        print("Rumus Keliling Jajar Genjang = 2 * (alas + sisi miring)")
        alas = float(input("Masukkan Alas Jajar Genjang (cm) : "))
        sisi_miring = float(input("Masukkan Sisi Miring Jajar Genjang (cm) : "))
        keliling = 2 * (alas + sisi_miring)
        print("Keliling Jajar Genjang Adalah :", float(keliling), "cm")
        print("============================================================")

    else:
        print("Error")

elif menu == 5:
    print("Anda Keluar Program")
    print("============================================================")

else:
    print("Error")
