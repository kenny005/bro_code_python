# Latihan 2 pogram hitung belanja

item = input("Nama belanjaan: ")
price = float(input("Harga: "))
quantity = int(input("Banyak barang: "))
total = price * quantity

print(f"Kamu membeli {quantity} x {item}/s")
print(f"Total belanjaannya:  ${total}")