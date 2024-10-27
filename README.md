## PRAKTIKUM - 2
# STRUKTUR KONDISI

# Kasus 1
Buat program yang menghitung harga tiket bioskop. Tiket reguler berharga Rp50.000,
sedangkan tiket VIP berharga Rp100.000. Jika user memiliki kartu member, mereka
mendapatkan diskon 20% dari harga tiket. Program ini harus meminta tipe tiket dan status
member dari user, lalu menghitung total harga yang harus dibayar.
# Kode Program - 1
``` python
def total_harga_tiket(jenis_tiket, member):
    
    harga_tiket = 50000 if jenis_tiket == 'reguler' else 100000
    
    harga_akhir = harga_tiket * 0.8 if member else harga_tiket
    
    return harga_akhir

jenis_tiket = input("Masukkan jenis tiket (reguler/VIP): ")
member = input("Apakah Anda memiliki kartu member? (Y/T): ") == 'Y'

harga = total_harga_tiket(jenis_tiket, member)

print(f"Harga tiket yang harus dibayar: Rp {harga}")
```
# Penjelasan Kode - 1
``` python
def total_harga_tiket(jenis_tiket, member):
```
``` python
harga_tiket = 50000 if jenis_tiket == 'reguler' else = 100000
```
``` python
harga_akhir = harga_tiket * 0.8 if member else harga_tiket
```
``` python
return harga_akhir
```
``` python
jenis_tiket = input("Masukkan jenis tiket (reguler/VIP): ")
member = input(Apakah Anda Memiliki kartu member?(Y/T)") == "Y"
```
``` python
harga = total_harga_tiket(jenis_tiket, member)
```
``` python
print(f"Harga tiket yang harus dibayar adalah: Rp.{harga}")
```

# Flowchart Kode - 1
![foto](https://github.com/Nakii-ru/foto/blob/main/Untitled%20Diagram.drawio(2).png?raw=true)
# Hasil Eksekusi Program - 1
![foto](https://github.com/Nakii-ru/foto/blob/main/Screenshot%202024-10-27%20180053.png?raw=true)
