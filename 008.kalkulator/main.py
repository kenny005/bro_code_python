operator = input("Masukkan operator (+, -, *, /): ")
num1 = float(input("Masukkan angka1: "))
num2 = float(input("Masukkan angka2: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is invalid operator")