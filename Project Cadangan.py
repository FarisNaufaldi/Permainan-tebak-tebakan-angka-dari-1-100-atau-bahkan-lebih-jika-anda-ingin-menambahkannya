import random 
def tebak_angka():
    Nama = input("Sebagai Pemain Anda harus memiliki nama = ")
    y = random.randint(1,100)
    while True:
        try:
            x = int(input(f"{Nama}, Masukkan tebakan anda dari 1 sampai 100 = "))
            if x == y:
                print(f"Selamat {Nama}, anda berhasil menebak angka yang benar yaitu {y}")
                break
            elif x > y:
                print(f"{Nama}, seharusnya anda menebak angka yang lebih kecil") 
            else:
                print(f"{Nama}, seharusnya anda menebak angka yang lebih besar")
        except ValueError:
            print(f"Hmmm sepertinya input yang {Nama} masukkan, salah")
tebak_angka()    

