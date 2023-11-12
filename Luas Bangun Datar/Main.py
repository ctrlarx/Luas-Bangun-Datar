#Pilihan
print("1. Luas Lingkaran")
print("2. Luas Persegi")
pilihan = input("Operasi apa yang ingin dilakukan?")


#Luas Lingkaran
def luas_lingkaran():
    #menentukan satuan
    global satuan
    satuan = input("Masukkan satuan awal yang digunakan (mm/cm/m/km): ")
    
    #menentukan radius lingkaran
    radius = float(input("Masukkan radius: "))
    
    #eksekusi dengan rumus jika radius habis dibagi 7
    if radius % 7 == 0:
        global hasil_luas_lingkaran
        hasil_luas_lingkaran = 22 / 7 * radius * radius 
        print(f"{hasil_luas_lingkaran} {satuan}")
    
    #eksekusi dengan rumus jika radius tidak habis dibagi 7    
    elif radius % 7 != 0:
        global hasil_luas_lingkaran2
        hasil_luas_lingkaran2 = 3.14 * radius * radius 
        print(f"{hasil_luas_lingkaran2} {satuan_awal}")

#Luas Persegi
def luas_persegi():
    #menentukan satuan
    global satuan 
    satuan = input("Masukkan satuan yang digunakan (mm/cm/m/km): ")
    
    #menentukan panjang sisi persegi
    panjang_sisi = float(input("Masukkan panjang sisi: "))
    
    #eksekusi dengan rumus
    global hasil 
    hasil = panjang_sisi * panjang_sisi
    print(hasil)

#Luas Persegi Panjang
def luas_persegi_panjang():
    #menentukan satuan
    global satuan 
    satuan = input("Masukkan satuan yang digunakan (mm/cm/m/km): ")
    
    #menentukan panjang sisi persegi panjang
    panjang = float(input("Masukkan panjang: "))
    
    #menentukan lebar sisi persegi panjang
    lebar = float(input("Masukkan lebar: "))

    #eksekusi dengan rumus
    global hasil 
    hasil = panjang * lebar
    print(hasil)

#Eksekusi
while True:
    if pilihan == "1":
        luas_lingkaran()
    elif pilihan == "2":
        luas_persegi()
    else:
        print("Maaf, pilihan belum tersedia.")
    
#memilih untuk mengonversi satuan atau tidak
konversi_satuan = input("Ketik '1' jika ingin mengonversi satuan, ketik '2' jika tidak ingin mengonversi satuan: ")
if konversi_satuan == "1":
    satuan_akhir = input("Ingin mengonversi satuan kemana (mm/cm/m/km): ")
    if satuan == "cm" and satuan_akhir == "mm":
        hasil_akhir = hasil * 10
    else: 
        print("Maaf, konversi belum tersedia.")