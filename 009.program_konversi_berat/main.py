

weight = float(input("Masukkan berat: "))
unit = input("Kg / Pounds? (K / L): ")

if unit == "K":
    weight *= 2.205
    unit = "Lbs"
    print(f"Berat kamu: {round(weight, 1)} {unit}")
elif unit == "L":
    weight /+ 2.205
    unit = "Kgs"
    print(f"Berat kamu: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")

