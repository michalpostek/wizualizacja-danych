import sys

# zad6
for x in range(1, 21):
    print(x * 5)


# zad7
for i in range(1, 3):
    x = int(input('Podaj liczbe: \n'))
    print('Kwadrat podanej liczby to', x**2)


# zad8
myList = []

while len(myList) < 5:
    x = int(input('Podaj liczbe ktora chcesz dodac do listy: \n'))
    myList.append(x)


# zad9
num = input('Podaj liczbe wielocyfrowa: \n')
sum = 0

for i in list(num):
    sum += int(i)

print(sum)


# zad10
height = 11

while height > 10:
    height = int(input('Podaj wysokosc wiezy: \n'))

for i in range(1, height + 1):
    for j in range(1, i + 1):
        sys.stdout.write('A')
    sys.stdout.write('\n')


# zad11
def print_row(start, end, step):
    for i in range(start, end, step):
        for j in range(1, int(m.floor(width - i) / 2) + 1):
            sys.stdout.write(' ')
        for k in range(1, i + 1):
            sys.stdout.write('o')
        sys.stdout.write('\n')


width = 0

while width < 4 or width > 9:
    width = int(input('Podaj szerokosc diamentu z przedzialu (3, 9): \n'))

print_row(1, width + 1, 2)
print_row(width - 2, 0, -2)


# zad12
def addLeadingSpace(k):
    return (' ' + str(k))[-2:]


for x in range(0, 10):
    for y in range(0, 10):
        if x == 0 and y == 0:
            sys.stdout.write(' *')
        elif x == 0:
            sys.stdout.write(addLeadingSpace(y))
        elif y == 0:
            sys.stdout.write(addLeadingSpace(x))
        else:
            sys.stdout.write(addLeadingSpace(x * y))
        sys.stdout.write('  ')
    sys.stdout.write('\n')
