def dodawanie(x, y):
    return x + y


def odejmowanie(x, y):
    return x - y


def mnożenie(x, y):
    return x * y


def dzielenie(x, y):
    if y == 0:
        return 'nie można dzielić przez zero!'
    return x / y


def menu(działanie):
    x = float(input("podaj x:"))
    y = float(input("podaj y:"))

    if działanie == '1':
        print('wynik:', dodawanie(x, y))
    elif działanie == '2':
        print('wynik:', odejmowanie(x, y))
    elif działanie == '3':
        print('wynik:', mnożenie(x, y))
    elif działanie == '4':
        print('wynik:', dzielenie(x, y))


while True:
    print("""---Kalkulator naukowy--- 
                działania:
                1 dodawanie
                2 odejmowanie
                3 mnożenie
                4 dzielenie
                q koniec programu""")
    w = input("wybierz:")
    if w == 'q':
        print('koniec')
        break
    elif w == '1' or w == '2' or w == '3' or w == '4':
        menu(w)
