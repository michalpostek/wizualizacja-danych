import sys

text = input('Podaj zdanie: \n')
spaceCounter = text.count(' ')
print("Twoje zdanie to '" + text + "', a liczba spacji w nim to", spaceCounter)

x = int(input('Podaj pierwszą liczbę: \n'))
print('Podaj drugą liczbę:')
y = int(sys.stdin.readline())
print('Iloczyn liczb', x, 'oraz', y, 'to', x*y)
