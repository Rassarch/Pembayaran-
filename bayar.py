import json
from datetime import datetime

print("=== Program Pembayaran Siswa SMK Negeri 3 Metro ===")

# Fungsi untuk menyimpan data ke file JSON
def simpan_ke_json(data, file="data_pembayaran.json"):
    try:
        # Cek apakah file JSON sudah ada
        with open(file, "r") as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        # Jika file belum ada, buat daftar kosong
        existing_data = []
    
    # Tambahkan data baru ke daftar
    existing_data.append(data)
    
    # Simpan kembali ke file JSON
    with open(file, "w") as f:
        json.dump(existing_data, f, indent=4)
    print("Data berhasil disimpan ke JSON.")

# Fungsi untuk membaca data dari file JSON
def lihat_data_json(file="data_pembayaran.json"):
    try:
        with open(file, "r") as f:
            data = json.load(f)
        print("\n=== Data Pembayaran yang Tersimpan ===")
        for idx, pembayaran in enumerate(data, 1):
            print(f"\nData {idx}:")
            for key, value in pembayaran.items():
                print(f"{key}: {value}")
    except FileNotFoundError:
        print("Belum ada data yang tersimpan.")
    except json.JSONDecodeError:
        print("File JSON kosong atau rusak.")

# Main program
while True:

    bayar = input("Apakah Anda ingin melakukan pembayaran? (Y/N): ").upper()

    if bayar == "Y":
        # Menginput identitas siswa
        nis = input("Masukkan NIS: ")
        nama = input("Masukkan Nama: ")
        kelas = input("Masukkan Kelas (X/XI/XII): ").upper()
        jurusan = input("Masukkan Jurusan: ")

        # Menghitung total pembayaran sesuai kelas
        total_bayar = 0
        rincian_pembayaran = ""
        tanggal_sekarang = datetime.now()

        if kelas == "X":
            total_bayar += 3200000
            rincian_pembayaran += "Komite: Rp 3.200.000\n"

        elif kelas == "XI":
            print("Anda bisa membayar Komite dan KI.")
            
            # Pembayaran Komite
            bayar_komite = input("Apakah Anda ingin membayar Komite? (Y/N): ").upper()
            if bayar_komite == "Y":
                total_bayar += 2900000
                rincian_pembayaran += "Komite: Rp 2.900.000\n"
            
            # Periode pembayaran KI
            awal_pembayaran_ki = datetime(tanggal_sekarang.year, 11, 8)
            akhir_pembayaran_ki = datetime(tanggal_sekarang.year, 11, 11)

            # Pembayaran KI
            if awal_pembayaran_ki <= tanggal_sekarang <= akhir_pembayaran_ki:
                bayar_ki = input("Apakah Anda ingin membayar KI? (Y/N): ").upper()
                if bayar_ki == "Y":
                    print("Pilih tipe KI:")
                    print("1. Luar Provinsi (Rp 1.900.000)")
                    print("2. Dalam Provinsi (Rp 300.000)")
                    print("3. Mandiri (Gratis)")
                    pilihan_ki = input("Masukkan pilihan KI (1/2/3): ")

                    if pilihan_ki == "1":
                        total_bayar += 1900000
                        rincian_pembayaran += "KI Luar Provinsi: Rp 1.900.000\n"
                    elif pilihan_ki == "2":
                        total_bayar += 300000
                        rincian_pembayaran += "KI Dalam Provinsi: Rp 300.000\n"
                    elif pilihan_ki == "3":
                        rincian_pembayaran += "KI Mandiri: Gratis\n"
            else:
                print("Pembayaran KI sudah ditutup.")

        elif kelas == "XII":
            print("Anda bisa membayar Komite dan PKL.")
            
            # Pembayaran Komite
            bayar_komite = input("Apakah Anda ingin membayar Komite? (Y/N): ").upper()
            if bayar_komite == "Y":
                total_bayar += 2800000
                rincian_pembayaran += "Komite: Rp 2.800.000\n"
            
            # Pembayaran PKL
            bayar_pkl = input("Apakah Anda ingin membayar PKL? (Y/N): ").upper()
            if bayar_pkl == "Y":
                print("Pilih lokasi PKL:")
                print("1. Dalam Kota (Rp 250.000)")
                print("2. Luar Kota (Rp 500.000)")
                pilihan_pkl = input("Masukkan pilihan PKL (1/2): ")

                if pilihan_pkl == "1":
                    total_bayar += 250000
                    rincian_pembayaran += "PKL Dalam Kota: Rp 250.000\n"
                elif pilihan_pkl == "2":
                    total_bayar += 500000
                    rincian_pembayaran += "PKL Luar Kota: Rp 500.000\n"

        # Pilihan metode pembayaran
        print("Pilih metode pembayaran:")
        print("1. Lunas")
        print("2. Cicil")
        pilihan_metode = input("Masukkan pilihan (1/2): ")

        status_pembayaran = "Belum Lunas"
        jumlah_cicilan = 0

        if pilihan_metode == "1":
            status_pembayaran = "Lunas"
            jumlah_cicilan = total_bayar
        elif pilihan_metode == "2":
            jumlah_cicilan = int(input("Masukkan jumlah cicilan yang ingin dibayar: Rp "))
            if jumlah_cicilan >= total_bayar:
                status_pembayaran = "Lunas"
                jumlah_cicilan = total_bayar
            else:
                status_pembayaran = "Cicil"
                total_bayar -= jumlah_cicilan

        # Simpan data ke JSON
        data_pembayaran = {
            "Nama Siswa": nama,
            "NIS": nis,
            "Kelas": kelas,
            "Jurusan": jurusan,
            "Tanggal Bayar": datetime.now().strftime('%d-%m-%Y'),
            "Rincian Pembayaran": rincian_pembayaran.strip(),
            "Total Bayar": jumlah_cicilan,
            "Kekurangan": total_bayar,
            "Status": status_pembayaran
        }
        simpan_ke_json(data_pembayaran)

        # Cetak struk pembayaran
        print("\n===== STRUK PEMBAYARAN =====")
        print(f"Nama Siswa   : {nama}")
        print(f"NIS          : {nis}")
        print(f"Kelas        : {kelas}")
        print(f"Jurusan      : {jurusan}")
        print(f"Tanggal Bayar: {datetime.now().strftime('%d-%m-%Y')}")
        print("\nRincian Pembayaran:")
        print(rincian_pembayaran)
        if status_pembayaran == "Cicil":   
            print(f"Total Bayar             : Rp {jumlah_cicilan:,}")
        print(f"Kekurangan              : Rp {total_bayar:,}")
        print(f"Status                  : {status_pembayaran}")
        print("=============================")

    elif bayar == "N":
        lihat = input("Apakah Anda ingin melihat data yang tersimpan? (Y/N): ").upper()
        if lihat == "Y":
            lihat_data_json()
        print("Terima kasih telah menggunakan program pembayaran.")
        break
    else:
        print("Input tidak valid. Harap masukkan 'Y' atau 'N'.")
