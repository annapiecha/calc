def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielic przez zero!"

x = float(input("Podaj x: "))
y = float(input("Podaj y: "))

print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnozenie")
print("4. Dzielenie")

wybor = input("Podaj operacje: ")

if wybor == '1':
    wynik = dodawanie(x, y)
elif wybor == '2':
    wynik = odejmowanie(x, y)
elif wybor == '3':
    wynik = mnozenie(x, y)
elif wybor == '4':
    wynik = dzielenie(x, y)

print(wynik)
