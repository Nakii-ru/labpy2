def total_harga_tiket(jenis_tiket, member):
    # Harga tiket berdasarkan jenis
    harga_tiket = 50000 if jenis_tiket == 'reguler' else 100000
    
    # Diskon 20% jika user adalah member
    harga_akhir = harga_tiket * 0.8 if member else harga_tiket
    
    return harga_akhir

# Input dari user
jenis_tiket = input("Masukkan jenis tiket (reguler/VIP): ")
member = input("Apakah Anda memiliki kartu member? (Y/T): ") == 'Y'

# Menghitung harga tiket
harga = total_harga_tiket(jenis_tiket, member)

print(f"Harga tiket yang harus dibayar: Rp {harga}")