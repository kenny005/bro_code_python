# Variable adalah sebuah kontainer untuk sebuah nilai berupa string, integer, float, boolean


# strings
from operator import is_


first_name = "Kenny"
last_name = 'ken'
food = "Nasi goreng"
email = "kenny@fake.com"

print(first_name, last_name)
print(f"Hello my name is {first_name} {last_name}")
print(f"You like {food}")
print(f"My email {email}")

# integer
age = 22
quantity = 20
num_of_students = 34

print(f"You are{age} years")
print(f"You buy {quantity}")
print(f"You have studend {num_of_students}")

# float 
price = 10.99
gpa = 3.3
distance = 55.6

print(f"The price ${price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance}Km")


# Boolean
is_students = False
if is_students:
    print(f"Kalian adalah pelajar: {is_students}")
else:
    print(f"Kamu bukan pelajar: {is_students}")


for_sale = False
if for_sale:
    print("Untuk dijual")
else:
    print("Tidak dijual")

is_online = True
if is_online:
    print("Kamu online")
else:
    print("Kamu tidak online")


# try
user_name = "Kenny005"
year = 2033
pi = 3.14
is_admin = True

print(f"{user_name} adalah admin : {is_admin} sejak tahun {year} dan ia mengetahui nilai pi adalah {pi}")