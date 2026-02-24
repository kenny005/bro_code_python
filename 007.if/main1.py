# if melakukan sesuatu jika kondisi TRUE
# Else lakukan sesuatu jika kondisi bukan True

age = int(input("Umurmu: "))

if age >= 100:
    print("Kamu terlalu tua")
elif age >= 18:
    print("Kamu adalah dewasa")
elif age < 0:
    print("Kamu belum lahir")
else:
    print("Kamu belum dewasa")