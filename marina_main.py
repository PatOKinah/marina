global PositionList

PositionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def main_menu():
    print("1. Lista stanowisk")
    print("2. Lista jachtów")
    print("3. Zamknij")

    Loop = True

    while Loop:
        wybor = input("Wybierz opcje[1-3]: ")
        if wybor == "1":
            print("Lista stanowisk")
            position_menu(PositionList)
        elif wybor == "2":
            print("Lista jachtów")
        elif wybor == "3":
            Loop = False
            exit()
        else:
            print("Brak takiej opcji")


def position_menu(PositionList):
    Loop = True
    # PositionList = []
    # for x in range(1, 21):
    #    PositionList.append(x)
    print(PositionList)
    print("1. Rezerwuj ")
    print("2. Zwolnij ")
    print("3. Menu główne ")
    while Loop:
        wybor = input("Wybierz opcje")
        if wybor == "1":
            print("Rezerwuję")
            reservation_option(PositionList)
        elif wybor == "2":
            print("Zwalniam")
            release_position(PositionList)
        elif wybor == "3":
            main_menu()
        else:
            print("Brak takiej opcji")
    return PositionList


def reservation_option(PositionList):
    x = int(input("Wybierz miejsce postojowe: "))
    PositionList[x - 1] = str(x) + ". Rezerwacja"
    print(PositionList)


def release_position(PositionList):
    x = int(input("Wybierz miejsce postojowe: "))
    PositionList[x - 1] = str(x)
    print(PositionList)


print("Marina")

main_menu()
