gaji = int(input("Masukkan Gaji: "))
berkeluarga = (False, True)[input("Sudah Berkeluarga?(Y/T) ") == "Y"]
punya_rumah = (False, True)[input("Punya Rumah?(Y/T) ") == "Y"]

if gaji > 3000000:
    print ("Gaji Sudah Diatas UMR")
    
    if berkeluarga:
        print("Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print("Tidak perlu ikutan asuransi")

    if punya_rumah:
            print("wajib bayar pajak rumah")
    else:
            print("tidak wajib bayar pajak rumah")
else:
 print("Gaji Belum UMR")