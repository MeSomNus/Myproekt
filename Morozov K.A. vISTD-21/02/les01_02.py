# coding: utf-8

# Python. Быстрый старт.
# Занятие 2.

# Домашнее задание: в случае, если пользователь ввел Y, то придумать и вывести список действий,
#                    спросить, какое он хочет выполнить;
#                   ознакомиться с PEP8
import os
print("Great Python Program!")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = input("Давайте поработаем? (Y/N)")
    
# PEP-8 рекомендует делать отступ, равный 4 пробелам   
if answer == 'Y' or 'y' :
    print ("Отлично, хозяин!")
    print ("Я умею:")
    print (" [1] - сложить 2 числа")
    print(" [2] - выведу информацию о системе")
    print(" [3] - выведу список процессов")
    do = int(input("Укажите номер действия"))

    if do == 1:
        a = int(input('Введите число "а": '))
        b = int(input('Введите число "b": '))
        print("a + b = ", a + b )
if do == 2:
    x = str(input())
    x = int(x)
    h1 = x // 100000 + (x // 10000) % 10 + (x // 1000) % 10
    h2 = x % 10 + (x % 100) // 10 + (x % 1000) // 100
    if h1 == h2:
        print ('Счастливый')
    else:
        print ('Обычный')
if do == 3:
    files = [f for f in os.listdir() if f.endwith(' .jpg')]
    print (files)

# Оператор == (двойное равно) - это логический оператор сравнения
elif answer == 'N':    
    print("До свидания!")
else:
    print("Неизвестный ответ")    