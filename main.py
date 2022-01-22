import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
difficulty = int(input("What should be the difficulty of your password? type '0' for easy and '1' for hard\n"))
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

lis = []
easy_password = ""
for i in range(nr_letters):
    l = random.choice(letters)
    easy_password += l
    lis.append(l)
for i in range(nr_symbols):
    s = random.choice(symbols)
    easy_password += s
    lis.append(s)
for i in range(nr_numbers):
    n = random.choice(numbers)
    easy_password += n
    lis.append(n)

random.shuffle(lis)
hard_password = ""
for i in lis:
    hard_password += i

if difficulty ==0:
    print(easy_password)
else:
    print(hard_password)