myList = ['Ala', 3.14, 1e20, [1, 2, 3]]

myList.append('Hello')
myList.insert(1, 'Hi')
myList.pop()
myList.pop(1)
myList.remove(3.14)

del myList[2]

myList.extend((1, 2, 3, 4, 5))

del myList[1:6]

myList[3:6] = [1, 2, 3]
myList.reverse()

print(myList)