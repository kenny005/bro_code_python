import math

"""
Modul ini menyediakan akses ke fungsi dan konstanta matematika umum, termasuk yang ditentukan oleh standar C.

Fungsi-fungsi ini tidak dapat digunakan dengan bilangan kompleks; gunakan fungsi nama yang sama dari modul jika Anda memerlukan dukungan untuk bilangan kompleks. Perbedaan antara fungsi yang mendukung bilangan kompleks dan yang tidak dibuat karena sebagian besar pengguna tidak ingin belajar banyak matematika seperti yang diperlukan untuk memahami bilangan kompleks. Menerima pengecualian alih-alih hasil yang kompleks memungkinkan deteksi lebih awal dari kompleks yang tidak terduga angka yang digunakan sebagai parameter, sehingga pemrogram dapat menentukan bagaimana dan mengapa itu dihasilkan sejak awal.


"""


print(math.pi)
print(math.e)

x = 9
y = 9.1
z = 9.9
# result = math.sqrt(x)
# result = math.ceil(y)
result = math.floor(z)
print(result)