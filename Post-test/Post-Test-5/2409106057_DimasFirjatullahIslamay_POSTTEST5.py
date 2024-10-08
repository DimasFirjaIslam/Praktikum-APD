users = [
    {"Username": "Dimas", "Password": "057", "Role": "Admin"},
    {"Username": "User", "Password": "000", "Role": "User"}
]

data_tanaman = [
    {"Nama": "Bunga Kamboja", "Jenis": "Bonsai Bunga", "Jadwal_siram": "3 Hari Sekali"},
    {"Nama": "Sirih Gading", "Jenis": "Tropis Merambat", "Jadwal_siram": "4 Hari Sekali"},
    {"Nama": "Lidah Buaya", "Jenis": "Sukulen", "Jadwal_siram": "Seminggu Sekali"}
]

print("=" * 10 + " Registrasi " + "=" * 10)
print("1. Registrasi")
print("2. Log in Sebagai Admin")
print("3. Log in Sebagai User")

pilihan = input("Masukkan Angka Menu Pilihan: ")

if pilihan == "1":
    print("=" * 10 + " Registrasi " + "=" * 10)
    user_baru = input("Masukkan Username Baru: ")
    password_baru = input("Masukkan Password Baru: ")
    user_exists = any(user["Username"] == user_baru for user in users)

    if user_exists:
        print("Username Sudah Terdaftar")
    else:
        users.append({"Username": user_baru, "Password": password_baru, "Role": "User"})
        print("Registrasi Berhasil")

    while True:
        user_baru = input("Masukkan Username: ")
        password_baru = input("Masukkan Password: ")
        login_sukses = False
        for user in users:
            if user["Username"] == user_baru and user["Password"] == password_baru:
                login_sukses = True
                break

        if login_sukses:
            print("Log in User Berhasil")
            break
        else:
            print("Username Atau Password Salah")

    while True:
        print("""
            Menu Tanaman Hias
            Lihat Data  >> 1
            Keluar      >> 2
        """)

        pilih = input("Masukan Pilihan Menu : ")

        if pilih == "1":
            print("=" * 9 + " Lihat Data " + "=" * 9)
            for i, tanaman in enumerate(data_tanaman):
                print(f"Data Ke-{i + 1}")
                print(f"Nama : {tanaman["Nama"]}")
                print(f"Jenis : {tanaman["Jenis"]}")
                print(f"Jadwal Siram : {tanaman["Jadwal_siram"]}")
                print("=" * 30)
            input("Tekan Enter Untuk Kembali Ke Menu")

        elif pilih == "2":
            print("Anda Telah Keluar")
            break

        else:
            print(f"Menu {pilih} Tidak Tersedia")
            input("Tekan Enter Untuk Kembali Ke Menu")

elif pilihan == "2":
    print("=" * 6 + " Login Sebagai Admin " + "=" * 6)
    while True:
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        for user in users:
            if user["Username"] == username and user["Password"] == password and user["Role"] == "Admin":
                print("Login Admin Berhasil")
                break
        else:
            print("Username Atau Password Salah")
            continue
        break

    while True:
        print("""
            Menu Tanaman Hias
            Lihat Data  >> 1
            Tambah Data >> 2
            Update Data >> 3
            Hapus Data  >> 4
            Keluar      >> 5
        """)

        pilih = input("Masukkan Pilihan Menu : ")

        if pilih == "1":
            print("=" * 9 + " Lihat Data " + "=" * 9)
            for i, tanaman in enumerate(data_tanaman):
                print(f"Data Ke-{i + 1}")
                print(f"Nama : {tanaman["Nama"]}")
                print(f"Jenis : {tanaman["Jenis"]}")
                print(f"Jadwal Siram : {tanaman["Jadwal_siram"]}")
                print("=" * 30)
            input("Tekan Enter Untuk Kembali Ke Menu")

        elif pilih == "2":
            print("=" * 8 + " Tambah Data " + "=" * 8)
            for i, tanaman in enumerate(data_tanaman):
                print(f"Data Ke-{i + 1}")
                print(f"Nama : {tanaman["Nama"]}")
                print(f"Jenis : {tanaman["Jenis"]}")
                print(f"Jadwal Siram : {tanaman['Jadwal_siram']}")
                print("=" * 30)

            index = int(input("Masukkan Nomor Data Yang Mau Diubah: ")) - 1

            if 0 <= index < len(data_tanaman):
                nama = input("Nama Tanaman : ")
                jenis = input("Jenis Tanaman : ")
                jadwal_siram = input("Jadwal Siram : ")
                data_tanaman.append({"Nama": nama, "Jenis": jenis, "Jadwal_siram": jadwal_siram})
                print(f"Tanaman {nama} Telah Ditambahkan")
                input("Tekan Enter Untuk Kembali Ke Menu")

        elif pilih == "3":
            print("=" * 8 + " Update Data " + "=" * 8)
            for i, tanaman in enumerate(data_tanaman):
                print(f"Data Ke-{i + 1}")
                print(f"Nama : {tanaman["Nama"]}")
                print(f"Jenis : {tanaman["Jenis"]}")
                print(f"Jadwal Siram : {tanaman['Jadwal_siram']}")
                print("=" * 30)

            index = int(input("Masukkan Nomor Data Yang Mau Ditambah: ")) - 1

            if 0 <= index < len(data_tanaman):
                nama_baru = input("Nama Baru : ")
                jenis_baru = input("Jenis Baru : ")
                jadwal_siram_baru = input("Jadwal Siram Baru : ")
                data_tanaman[index] = {
                    "Nama": nama_baru,
                    "Jenis": jenis_baru,
                    "Jadwal_siram": jadwal_siram_baru
                }
                print("Data Berhasil Diubah")
            else:
                print("Pilihan Tidak Valid")
            input("Tekan Enter Untuk Kembali Ke Menu")

        elif pilih == "4":
            print("=" * 10 + " Hapus Data " + "=" * 10)
            for i, tanaman in enumerate(data_tanaman):
                print(f"Data Ke-{i + 1}")
                print(f"Nama : {tanaman["Nama"]}")
                print(f"Jenis : {tanaman["Jenis"]}")
                print(f"Jadwal Siram : {tanaman["Jadwal_siram"]}")
                print("=" * 30)

            index = int(input("Masukkan Nomor Data Yang Ingin Dihapus: ")) - 1

            if 0 <= index < len(data_tanaman):
                del_tanaman = data_tanaman.pop(index)
                print(f"Tanaman {del_tanaman["Nama"]} Telah Dihapus")
                print("Data Berhasil Dihapus")
            else:
                print("Pilihan Tidak Valid")
            input("Tekan Enter Untuk Kembali Ke Menu")

        elif pilih == "5":
            print("Anda Telah Keluar")
            break

        else:
            print(f"Menu {pilih} Tidak Tersedia")

elif pilihan == "3":
    print("=" * 10 + " Login Sebagai User " + "=" * 10)
    while True:
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        for user in users:
            if user["Username"] == username and user["Password"] == password and user["Role"] == "User":
                print("Login User Berhasil")
                break
        else:
            print("Username Atau Password Salah")
            continue
        break

    while True:
        print("""
            Menu Tanaman Hias
            Lihat Data  >> 1
            Keluar      >> 2
        """)

        pilih = input("Masukan Pilihan menu : ")

        if pilih == "1":
            print("=" * 9 + " Lihat Data " + "=" * 9)
            for i, tanaman in enumerate(data_tanaman):
                print(f"Data Ke-{i + 1}")
                print(f"Nama : {tanaman["Nama"]}")
                print(f"Jenis : {tanaman["Jenis"]}")
                print(f"Jadwal Siram : {tanaman["Jadwal_siram"]}")
                print("=" * 30)
            input("Tekan Enter Untuk Kembali Ke Menu")

        elif pilih == "2":
            print("Anda Telah Keluar")
            break

        else:
            print(f"Menu {pilih} Tidak Tersedia")
            input("Tekan Enter Untuk Kembali Ke Menu")
else:
    print("Pilihan Tidak Valid")
