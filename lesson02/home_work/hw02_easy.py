# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["apple", "banana", "mango", "cherry"]
for num, frut in enumerate(fruits):
    print(str(num) + '. {:>30}'.format(frut))

# Задача-2:
# рисутствующие во втором списке.

fruits = ["apple", "banana", "tomato", "cherry"]
vegetables = ["tomato", 'cucumber', 'carrot', 'peterseile']
print('\n The basket labeled fruits contains following pieces:', fruits, '\nWe need to sort it out and if any vegetable inside, put it in a basket "Vegetables"')
for frut in fruits[:]:
    for jcs in vegetables[:]:
        if frut == jcs:
            fruits.remove(jcs)

print('Lets check our work. \nWe sorted the basket and now it contains only:', fruits)




# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numList = []
newList = []
thirdList = []
maxLength = int(input('How many numbers you want to check?',))
while len(numList) < maxLength:
    a = int(input('Please enter integer number:'))
    numList.append(a)

for a in numList:
    # count = numList.index(a) #позволяет получить порядковый номер
    if (a % 2) == 0:
        divtwo = a/4
        newList.append(a)
        thirdList.append(divtwo)
      #  print(count)

    else:
        a = a*2
        thirdList.append(a)
