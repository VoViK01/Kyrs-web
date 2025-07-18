# a = input("Vedit ima: ")
# print(f"Hello, {a}")
# n = int (input("namber"))
# if n > 0:
#     print("+")
# elif n == 0:
#     print("0")
# else:
#     print("-")
#1.Створи змінні name, age, is_student та виведи їх значення за допомогою print().
# name = "Vova"
# age = "19"
# is_student = True
# print(f"{name},{age},{is_student}") 
# Створи три змінні: ціле число, десяткове число і рядок. Виведи їх типи за допомогою type().
# a= 11
# b= 10.2
# c="ppp"
# print (type(a), type(b),type(c))
# 4.Запитай число як рядок. Перетвори його у int, додай 10 і виведи результат.
# a = input("Chuslo")
# print(int(a)+10)
# Перетвори float у str, а потім знову у int. Виведи кожен тип після перетворення.
# a= float(input("chuslo ne cile"))
# a1 = str(a)
# a2= int(a)
# print(a,a1,a2)
# 5.Створи:
# список з трьох улюблених ігор,
# кортеж з трьох місяців,
# множину з унікальних букв у слові,
# словник з ключами: name, age, city.
# a = ["GTA","GTA SA","Mafia"]
# b = ("Січень","Лютий","Липень")
# c = set("GaaaaaT") 

# Виведи по одному значенню з кожної структури (list, tuple, dict). У множині просто виведи її.
# a = ["GTA", "GTA SA", "Mafia"]
# b = ('Січень','Лютий','Липень')
# c = 'GaaaaaT'
# print(a[0],b[2],c[0])
# 6.Створи список чисел [5, 3, 9, 1]. Виведи:
# другий елемент,
# заміни перший на 10,
# видали останній,
# відсортуй список.
# a = [5, 3, 9, 1]
# a[0] = 10            # заміна першого
# a.pop()              # видалення останнього
# a.sort()             # сортування списку
# print(a)             # друк результату


# Зі строки "Hello":
# виведи першу букву,
# останню,
# зроби всі літери великими (upper()),
# виведи довжину рядка.
# a = "Hello"
# print(a[0])
# print(a[4])
# print(a.upper())
# print(len(a))
numbers = [8, 2, 7, 4, 6]
# Виведи третій елемент списку
print(numbers[2])
# Замінити останній елемент на 10
numbers[-1] = 10
# Видали другий елемент
numbers.pop(1)
# Відсортуй список у зворотному порядку (від більшого до меншого)
numbers.sort(reverse=True)

print(numbers)

fruits = ["apple", "banana", "cherry", "mango"]
# Виведи перший та останній фрукт
fruits[0], fruits[3]
# Замінити "banana" на "orange"
fruits[1]= "orange"
# Видали "cherry"
fruits.remove("cherry")
# Додай "peach" в кінець
fruits.append("peach")
# Відсортуй список по алфавіту
fruits.sort()
print(fruits)