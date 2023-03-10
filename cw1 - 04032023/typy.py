import math as m

num = 3.55
num2 = 4.8
sum = num + num2
sin = m.sin(8)**2
log = m.log(5 + sin)

print('Wynikiem działania', num, '+', num2, '=', sum)
print('Wynikiem działania %(num)f + %(num2)f = %(sum)f' % {'num':num, 'num2': num2, 'sum': sum})
print(m.e**10)
print(log**(1/6))
print(m.floor(num))
print(m.ceil(num2))

first_name = 'MICHAŁ'
last_name = 'POSTEK'

print(first_name.capitalize(), last_name.capitalize())

sentence = 'Ala ma kota'
print(sentence.split(' '))
