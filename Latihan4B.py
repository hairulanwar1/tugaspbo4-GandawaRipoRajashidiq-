try:
    # Input angka dari user
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))

    # Proses penjumlahan
    hasil = angka1 + angka2

    # Menampilkan hasil
    print("Hasil penjumlahan:", hasil)

# Menangkap error jika input bukan angka
except ValueError:
    print("Input tidak valid! Harap masukkan angka.")


while True:  # Perulangan agar bisa terus mencoba
    try:
        # Input angka
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))

        # Penjumlahan
        hasil = angka1 + angka2
        print("Hasil:", hasil)

    # Jika terjadi error
    except ValueError:
        print("Input salah! Harus angka.")

    # Tanya user mau lanjut atau tidak
    lanjut = input("Mau coba lagi? (y/n): ")
    
    # Jika tidak 'y', keluar dari loop
    if lanjut.lower() != "y":
        break

    