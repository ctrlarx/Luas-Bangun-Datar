#Luas Lingkaran
def luas_lingkaran():
    #menentukan radius lingkaran
    radius = float(input("Masukkan radius: "))
    
    #eksekusi dengan rumus jika radius habis dibagi 7
    if radius % 7 == 0:
        global hasil_luas_lingkaran
        hasil_luas_lingkaran = 22 / 7 * radius * radius 
        print(f"Luas lingkaran = {hasil_luas_lingkaran}")
    
    #eksekusi dengan rumus jika radius tidak habis dibagi 7    
    elif radius % 7 != 0:
        global hasil_luas_lingkaran2
        hasil_luas_lingkaran2 = 3.14 * radius * radius 
        print(f"Luas lingkaran = {hasil_luas_lingkaran2}")

#Luas Persegi
def luas_persegi():
    #menentukan panjang sisi persegi
    panjang_sisi = float(input("Masukkan panjang sisi: "))
    
    #eksekusi dengan rumus
    hasil = panjang_sisi * panjang_sisi
    print(f"Luas persegi = {hasil}")

#Luas Persegi Panjang
def luas_persegi_panjang():
    #menentukan panjang sisi persegi panjang
    panjang = float(input("Masukkan panjang: "))
    
    #menentukan lebar sisi persegi panjang
    lebar = float(input("Masukkan lebar: "))

    #eksekusi dengan rumus
    hasil = panjang * lebar
    print(hasil)

def luas_segitiga():
    #menentukan alas segitiga
    alas = float(input("Masukkan alas : "))

    #menentukan tinggi segitiga
    tinggi = float(input("Masukkan tinggi: "))

    #eksekusi dengan rumus
    hasil = 1 / 2 * alas * tinggi
    print(hasil)

def luas_trapesium():
    #menentukan panjang sisi sejajar pendek
    #a = panjang sisi sejajar pendek
    a = float(input("Masukkan panjang sisi sejajar pendek: "))

    #menentukan panjang sisi sejajar panjang
    #b = panjang sisi sejajar panjang
    b = float(input("Masukkan panjang sisi sejajar panjang: "))

    #menentukan tinggi
    #t = tinggi
    t = float(input("Masukkan tinggi: "))
        
    #eksekusi dengan rumus
    hasil = 1 / 2 * (a + b) * t
    print(hasil)


#Eksekusi
while True:
    print("1. Luas Lingkaran")
    print("2. Luas Persegi")
    print("3. Luas Persegi Panjang")
    print("4. Luas Segitiga")
    print("5. Luas Trapesium")
    pilihan = input("Operasi apa yang ingin dilakukan? ")
    
    if pilihan == "1":
        luas_lingkaran()
        break
    elif pilihan == "2":
        luas_persegi()
        break
    elif pilihan == "3":
        luas_persegi_panjang()
        break
    elif pilihan == "4":
        luas_segitiga()
        break
    elif pilihan == "5":
        luas_trapesium()
        break
    else:
        coba_lagi = input("Maaf, pilihan belum tersedia.Ingin coba lagi? Tekan '1' untuk ya, tekan '2' untuk tidak: ")
        if coba_lagi == "2":
            break
        else:
            continue
