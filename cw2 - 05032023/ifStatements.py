x = int(input('Podaj liczbe'))

if x > 0:
    print('Podana liczba jest większa od 0')
elif x == 0:
    print('Podana liczba jest równa 0')
else:
    print('Podana liczba jest mniejsza od 0')

# zad4
number = int(input('Podaj liczbe: \n'))

if number < 0:
    number *= (-1)

print('Wartosc bezwzgledna podanej liczby to', number)

# zad5
a = int(input('Podaj pierwsza liczbe: \n'))
b = int(input('Podaj druga liczbe: \n'))
c = int(input('Podaj trzecia liczbe: \n'))

if 0 < a <= 10 and (a > b or b > c):
    print('Warunki zostały spełnione')
else:
    print('Warunki nie zostaly spelnione')
