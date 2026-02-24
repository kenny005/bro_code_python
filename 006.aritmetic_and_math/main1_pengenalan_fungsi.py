from unittest import result




"""
🔹 round()
Digunakan untuk membulatkan angka.
Tanpa desimal → dibulatkan ke bilangan bulat terdekat
Bisa juga menentukan jumlah angka di belakang koma

round(3.6)      # 4
round(3.14159, 2)  # 3.14

🔹 abs()
Digunakan untuk mengambil nilai mutlak (jarak dari nol).
Hasilnya selalu positif
Contoh: abs(-5) → 5

🔹 pow()
Digunakan untuk perpangkatan.
Artinya: angka pangkat angka lain
Bisa juga dipakai untuk pangkat + sisa bagi (modulus)
pow(2, 3)  # 8

🔹 max()
Digunakan untuk mencari nilai paling besar.
Bisa dari beberapa angka atau dari satu kumpulan data
max(3, 7, 1)  # 7

🔹 min()
Digunakan untuk mencari nilai paling kecil.
Bisa dari beberapa angka atau dari satu kumpulan data
min(3, 7, 1)  # 1

"""
x = 3.14
y = -4
z = 5
# result = round(x)
result = abs(y)
# result = pow(3, 3 ) #3*3*3=27
# result = max(x, y, z)
# result = min(x, y, z)
print(result)


