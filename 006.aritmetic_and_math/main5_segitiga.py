import math

# c = akar(a2 + b2)

a = float(input("Masukkan angka a: "))
b = float(input("Masukkan angka b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C : {c}")