## PRAKTIKUM - STRUKTUR DAN KONDISI

RIDHO FHADLY HAMZAH

312410386

TI.24.A5

# Kasus 1
Buat program yang menghitung harga tiket bioskop. Tiket reguler berharga Rp50.000,
sedangkan tiket VIP berharga Rp100.000. Jika user memiliki kartu member, mereka
mendapatkan diskon 20% dari harga tiket. Program ini harus meminta tipe tiket dan status
member dari user, lalu menghitung total harga yang harus dibayar.
# Kode Kasus - 1
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
# Penjelasan Kasus - 1
``` python
def total_harga_tiket(jenis_tiket, member):
```
fungsi pertama pada program ini ialah definisi dari fungsi `harga total` yang menerima 2 parameter, yaitu `jenis tiket` dan `member`.
``` python
harga_tiket = 50000 if jenis_tiket == 'reguler' else = 100000
```
Di sini, variabel harga_tiket diisi dengan harga sesuai jenis_tiket,
jika pengguna memasukan input dengan "`reguler`" maka harga tiket akan menjadi 50000.
Ketika pengguna memasukan input selain "`reguler`" atau hanya mengisi "`VIP`" maka program akan otomatis memberi variabel harga tiket nya menjadi 100000.
``` python
harga_akhir = harga_tiket * 0.8 if member else harga_tiket
```
Dalam baris ini, jika pengguna memasukkan input "`Y`" maka harga tiket "`reguler`" maupun "`VIP`" akan dikali kan dengan 0.8 untuk memberikan diskon. Tetapi, ketika pengguna menginputkan "`T`" maka harga tiket akan sama dengan nilai asli nya.
``` python
return harga_akhir
```
Fungsi ini mengembalikan `harga_akhir` ke bagian program yang memanggil fungsi ini.
``` python
jenis_tiket = input("Masukkan jenis tiket (reguler/VIP): ")
```
Mengambil input dari pengguna untuk menentukan jenis tiket (reguler atau VIP).
``` python
member = input(Apakah Anda Memiliki kartu member?(Y/T)") == "Y"
```
Mengambil input dari pengguna untuk menentukan apakah mereka memiliki kartu member (Y untuk ya, T untuk tidak). Operator == 'Y' mengubah input menjadi True atau False
``` python
harga = total_harga_tiket(jenis_tiket, member)
```
Setelah input diambil, fungsi total_harga_tiket dipanggil dengan argumen jenis_tiket dan member.
Variabel harga menyimpan hasil dari fungsi tersebut, yaitu harga tiket yang harus dibayar setelah memperhitungkan status member dan jenis tiket.
``` python
print(f"Harga tiket yang harus dibayar adalah: Rp.{harga}")
```
Hasil tersebut dicetak dengan pesan berikut.

# Flowchart Kasus - 1
![foto](https://github.com/Nakii-ru/foto/blob/main/Untitled%20Diagram.drawio(2).png?raw=true)
# Hasil Eksekusi Program - 1
![foto](https://github.com/Nakii-ru/foto/blob/main/Screenshot%202024-10-27%20180053.png?raw=true)

# Kasus - 2
Buat program kalkulator yang menerima dua angka dan satu operator aritmatika dari
pengguna (penjumlahan, pengurangan, perkalian, atau pembagian). Program akan
menghitung hasil sesuai dengan operator yang dipilih.

# Kode Kasus - 2
```python
def hitung(angka1, operator, angka2):
    if operator == '+':
        hasil = angka1 + angka2

    elif operator == '-':
        hasil = angka1 - angka2
 
    elif operator == '*':
        hasil = angka1 * angka2

    else:
    operator == '/'
        hasil = angka1 / angka2
 
return hasil
```
# Penjelasan Kasus - 2
``` python
def hitung(angka1, operator, angka2):
```
Baris pertama ialah deklarasi fungsi hitung yang menerima tiga parameter: `angka1`, `operator`, dan `angka2`. `angka1` dan `angka2` adalah angka yang akan dioperasikan, sedangkan operator adalah simbol operasi `(+, -, *, atau /)` yang akan digunakan pada angka tersebut.
```python
    if operator == '+':
```
if operator == `'+'`: Kondisi ini mengecek apakah operator adalah `+`. Jika benar, maka `angka1` dan `angka2` akan dijumlahkan.
```python
        hasil = angka1 + angka2
```
hasil = angka1 + angka2: Jika kondisi di atas terpenuhi, variabel hasil akan menyimpan hasil dari penjumlahan angka1 dan angka2.
``` python
    elif operator == '-':
```
elif operator == `'-'`: Kondisi ini akan memeriksa apakah operator adalah `-`. Jika benar, maka `angka1` dan `angka2` akan dikurangkan.
```python
        hasil = angka1 - angka2
```
hasil = angka1 - angka2: Variabel hasil menyimpan hasil pengurangan angka1 dan angka2.
``` python
    elif operator == '*':
```
hasil = angka1 * angka2: Variabel hasil menyimpan hasil perkalian angka1 dan angka2.
elif operator == `'*'`: Kondisi ini memeriksa apakah operator adalah `*`. Jika benar, maka `angka1` dan `angka2` akan dikalikan.
```python
        hasil = angka1 * angka2
```
hasil = angka1 + angka2: Jika kondisi di atas terpenuhi, variabel hasil akan menyimpan hasil dari penjumlahan angka1 dan angka2.
``` python
    else:
        operator == '/'
```
`else:` Kondisi ini digunakan untuk operasi pembagian sebagai pilihan terakhir jika operator bukan +, -, atau *. yaitu membagi `'/'` bilangan `angka1` dan `angka2`.
```python
        hasil = angka1 / angka2
```
hasil = angka1 / angka2: hasil menyimpan hasil pembagian angka1 dan angka2.
``` python
return hasil
```
Mengembalikan nilai hasil sebagai output dari fungsi hitung. nilai hasil dikembalikan setelah semua operasi selesai.
# Flowchart Kasus - 2
![foto](https://github.com/Nakii-ru/foto/blob/main/Untitled%20Diagram(2).drawio(1).png?raw=true)
# Hasil Eksekusi Kasus - 2
![foto](https://github.com/Nakii-ru/foto/blob/main/Screenshot%202024-10-28%20075642.png?raw=true)
