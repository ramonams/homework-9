print("Pozdrav, ovdje možete preračunati km u milje")


while True:
    km = int(input("unesi kilometre:"))
    conv = km / 1.609344
    print("rezultat je:" + " " + str(conv) + " " + "mi")

    ask = input("želite li ponoviti pretvorbu (da/ne)?")

    if ask == "da":
        km = int(input("unesi kilometre:"))
        conv = km / 1.609344
        print("rezultat je:" + " " + str(conv))
    else:
        break



