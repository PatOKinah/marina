import time
global PositionList
global Dict_of_yacht

PositionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Dict_of_yacht = {}

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
            list_of_yacht(Dict_of_yacht)
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

def list_of_yacht(Dict_of_yacht):
    x = int(input("Podaj miejsce postojowe: "))
    if PositionList[x-1] == x :
        owner = input("Podaj imię i nazwisko: ")
        saillicense = input("Podaj numer patentu żeglarskiego: ")
        degree = input("Podaj stopień żeglarski: ")
        contact_with_owner = input("Podaj numer telefonu: ")
        type_of_yacht = input("Typ/Klasa jachtu: ")
        plate = input("Numer rejestracyjny jachu")
        last_update = time.strftime("%Y.%m.%d//%H:%M:%S")
        Dict_of_yacht = {x:{"właściciel": owner, "patent": saillicense, "stopień": degree,
                            "telefon": contact_with_owner, "typ/klasa": type_of_yacht, "rejestracja": plate,
                            "modyfikacja": last_update}}
        print(Dict_of_yacht)
    else: print("Miejsce postojowe jest już zarezerwowane")
    return Dict_of_yacht



print("Marina")

main_menu()
