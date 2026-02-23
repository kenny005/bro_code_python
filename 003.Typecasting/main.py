# Typecasting: Proses mengkonversi variabel dari satu tipe data ke tipe data lain: str(), int(), float(), bool()


name = "Kenny"
age = 23
gpa = 3.3
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))


gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = 25
age = str(age)
print(age)
print(type(age))
age += "1"
print(age)


name = bool(name)
print(name)
name = ""
name = bool(name)
print(name)