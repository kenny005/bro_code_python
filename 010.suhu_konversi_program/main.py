unit = input("Is this them in celcius or fahren? (C/F): ")
temp = float(input("Masukkan temp: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32)
    print(f"Temp in fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"Temp in celcius is: {temp}°C")
else:
    print(f"{unit} is invalid")