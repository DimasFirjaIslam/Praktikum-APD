users = [
    {"Username": "Dimas", "Password": "057", "Role": "Admin"},
    {"Username": "User", "Password": "000", "Role": "User"}
]

data_tanaman = [
    {"Nama": "Bunga Kamboja", "Jenis": "Bonsai Bunga", "Jadwal_siram": "3 Hari Sekali"},
    {"Nama": "Sirih Gading", "Jenis": "Tropis Merambat", "Jadwal_siram": "4 Hari Sekali"},
    {"Nama": "Lidah Buaya", "Jenis": "Sukulen", "Jadwal_siram": "Seminggu Sekali"}
]


def tampilkan_data():
    for i, tanaman in enumerate(data_tanaman):
        print(f"Data Ke-{i + 1}")
        print(f"Nama : {tanaman['Nama']}")
        print(f"Jenis : {tanaman['Jenis']}")
        print(f"Jadwal Siram : {tanaman['Jadwal_siram']}")
        print("=" * 30)


def tambah_data():
    tampilkan_data()
    try:
        print("Silahkan Tambah Data Yang Diinginkan ")
        nama = input("Nama Tanaman: ")
        jenis = input("Jenis Tanaman: ")
        jadwal_siram = input("Jadwal Siram: ")
        data_tanaman.append({"Nama": nama, "Jenis": jenis, "Jadwal_siram": jadwal_siram})
        print(f"Tanaman {nama} Telah Ditambahkan")
    except ValueError:
        print("Input Tidak Valid")


def update_data():
    tampilkan_data()
    try:
        index = int(input("Masukkan Nomor Data Yang Mau Diupdate : ")) - 1
        if not (0 <= index < len(data_tanaman)):
            print("Pilihan Tidak Valid")
            return
        nama_baru = input("Nama Baru: ")
        jenis_baru = input("Jenis Baru: ")
        jadwal_siram_baru = input("Jadwal Siram Baru: ")

        data_tanaman[index] = {
            "Nama": nama_baru,
            "Jenis": jenis_baru,
            "Jadwal_siram": jadwal_siram_baru
        }
        print("Data Berhasil Diubah")
    except ValueError:
        print("Input Tidak Valid")


def hapus_data():
    tampilkan_data()
    try:
        index = int(input("Masukkan Nomor Data Yang Ingin Dihapus : ")) - 1
        if not (0 <= index < len(data_tanaman)):
            print("Pilihan Tidak Valid")
            return

        del_tanaman = data_tanaman.pop(index)
        print(f"Tanaman {del_tanaman['Nama']} Telah Dihapus")
    except ValueError:
        print("Input Tidak Valid")


def login(role):
    while True:
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        for user in users:
            if user["Username"] == username and user["Password"] == password and user["Role"] == role:
                print(f"Login {role} Berhasil")
                return True
        print("Username Atau Password Salah. Coba Lagi")


def main_menu():
    while True:
        print("=" * 10 + " Menu Utama " + "=" * 10)
        print("1. Registrasi")
        print("2. Log in Sebagai Admin")
        print("3. Log in Sebagai User")
        print("4. Keluar Program")

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

        elif pilihan == "2":
            print("=" * 6 + " Login Sebagai Admin " + "=" * 6)
            if login("Admin"):
                menu_admin()

        elif pilihan == "3":
            print("=" * 6 + " Login Sebagai User " + "=" * 6)
            if login("User"):
                menu_user()

        elif pilihan == "4":
            print("Program Selesai, Terimakasih Telah Menggunakan Layanan Kami")
            break
        else:
            print("Pilihan Tidak Valid")
            input("Tekan Enter Untuk Kembali")


def menu_admin():
    while True:
        print(""" 
            Menu Admin
            Lihat Data  >> 1
            Tambah Data >> 2
            Update Data >> 3
            Hapus Data  >> 4
            Log out     >> 5
        """)
        pilih = input("Masukkan Pilihan Menu : ")

        if pilih == "1":
            print("=" * 9 + " Lihat Data " + "=" * 9)
            tampilkan_data()
            input("Tekan Enter Untuk Kembali Ke Menu")
        elif pilih == "2":
            print("=" * 8 + " Tambah Data " + "=" * 8)
            tambah_data()
            input("Tekan Enter Untuk Kembali Ke Menu")
        elif pilih == "3":
            print("=" * 8 + " Update Data " + "=" * 8)
            update_data()
            input("Tekan Enter Untuk Kembali Ke Menu")
        elif pilih == "4":
            print("=" * 8 + " Hapus Data " + "=" * 8)
            hapus_data()
            input("Tekan Enter Untuk Kembali Ke Menu")
        elif pilih == "5":
            print("Log out Berhasil")
            input("Tekan Enter Untuk Kembali Ke Menu")
            break
        else:
            print(f"Menu {pilih} Tidak Tersedia")
            input("Tekan Enter Untuk Kembali Ke Menu")


def menu_user():
    while True:
        print(""" 
            Menu User
            Lihat Data  >> 1
            Log Out     >> 2
        """)
        pilih = input("Masukkan Pilihan Menu : ")

        if pilih == "1":
            print("=" * 9 + " Lihat Data " + "=" * 9)
            tampilkan_data()
            input("Tekan Enter Untuk Kembali Ke Menu")
        elif pilih == "2":
            print("Log Out Berhasil")
            input("Tekan Enter Untuk Kembali Ke Menu")
            break
        else:
            print(f"Menu {pilih} Tidak Tersedia")
            input("Tekan Enter Untuk Kembali Ke Menu")


main_menu()
