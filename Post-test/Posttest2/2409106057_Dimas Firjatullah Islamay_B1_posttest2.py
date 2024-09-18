Nama = input("Masukkan Nama = ")
NIM = int(input("Masukkan Nim = "))
Umur = int(input("Masukkan Umur = "))
BB = float(input("Masukkan Berat Badan (kg) = "))
TB = float(input("Masukkan Tinggi Badan (cm) = "))
Kerja = input("Apakah anda memiliki pekerjaan sampingan? (True/False)= ") == "True"

total = NIM + Umur + BB + TB

print("=====================================")
print("            BIO DATA ANDA            ")
print("=====================================")
print(f"Nama             : {Nama}")
print(f"Umur             : {Umur} tahun")
print(f"Berat Badan      : {BB} kg")
print(f"Tinggi Badan     : {TB} cm")
print(f"Pekerjaan        : {"Memiliki pekerjaan sampingan" if Kerja else ("Tidak ada")}")
print("=====================================")
print(f"Total (NIM + Umur + BB + TB) : {total}")
print("=====================================")
