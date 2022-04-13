

number = int(input("unesi broj (1-100):"))

for number in range (1, number+1):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)

#treći zadatak zadaće 9

pozdrav = input("unesi pozdrav:")
print(pozdrav.lower())
print(f"{pozdrav}".upper())

ime = "ramona"
prezime = "sendo"

print(f"moje ime je {ime}, a moje prezime je {prezime} ")



