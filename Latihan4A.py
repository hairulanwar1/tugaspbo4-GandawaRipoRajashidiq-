# Meminta input nama dari user
nama = input("Masukkan nama Anda: ")

# Membuka file guest.txt dengan mode write (w)
# Jika file belum ada, akan dibuat
with open("guest.txt", "w") as file:
    file.write(nama)  # Menyimpan nama ke file

# Menampilkan pesan sukses
print("Nama berhasil disimpan ke guest.txt")



print("Masukkan nama (ketik 'stop' untuk berhenti)")

# Membuka file dalam mode write
with open("guest_book.txt", "w") as file:
    while True:  # Perulangan terus menerus
        nama = input("Nama: ")  # Input nama
        
        # Jika user mengetik 'stop', perulangan berhenti
        if nama.lower() == "stop":
            break
        
        # Menyimpan nama ke file + pindah baris
        file.write(nama + "\n")

print("Semua nama berhasil disimpan.")