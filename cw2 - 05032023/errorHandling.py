import math as m

# zadanie 14
try:
    x = int(input('Podaj liczbe: \n'))
    sqrt = m.sqrt(x)
    print('Pierwiastek podanej liczby to', sqrt)
except ValueError:
    print('Liczba nie może być ujemna')

# zadanie 15

try:
    y = int(input('Podaj liczbe: \n'))
except ValueError:
    print('Podana wartosc jest nieprawidlowa')