print("Menampilkan bilangan dari n buah data yang di input")

max = 0
while True:
    a = int(input("Masukkan Bilangan : "))
    if max < a:
        max = a
    if a ==0:
        break    
print("bilangan Terbesar Adalah: ", max)    