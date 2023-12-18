#task 1

# print ('введите два числа')
# a = int(input())
# b = int(input())

# if a < b:
#     print (a)
#     print ('это число меньше')
# else:
#     print (b)
#     print ('это число меньше')


#task 2

# print ('введите имя')
# name = str(input())
# print ('введите возраст')
# age = int(input())

# if age <= 18:
#     print ('Привет' + ' ' + name + ' ' +  'Приносим извинения, но вы не можете гулять после 22:00.')
# else:
#     print ('Добрый вечер,' + ' ' + name + ' ' + 'Вы совершеннолетний, поздравляем!')

#task 3

# print ('введите первую строку')
# str1 = input()
# print ('введите вторую строку')
# str2 = input()
# print ('введите третью строку')
# str3 = input()

# if str1 == 'python':
#     print (1)
# elif str2 == 'python':
#     print (2)
# elif str3 == 'python':
#     print (3)
# else:
#     print ('Такой строки нет')

#task 4

# print ('введите первое число')
# int1 = int(input())
# print ('введите второе число')
# int2 = int(input())
# print ('введите третье число')
# int3 = int(input())

# if int1 == int2:
#     print (int3)
# elif int1 == int3:
#     print(int2)
# elif int2 == int3:
#     print (int1)
# else:
#     print ("ошибка")

#task 5
# print ('введите число')
# int1 = str(input())
# if len(int1) == 4:
#     print ('успешно')
# else:
#     print ('ошибка')

#task 6
# print ('введите время в часах')
# time = int(input())

# if time >= 7 and time <= 10:
#     print ('Пора вставать')
# elif time < 7 and time >= 0 or time > 10 and time <= 23:
#     print ('Ты проспал')
# else:
#     print ('Ошибка')

#task 7

# print ('введите время в часах')
# time = int(input())
# if time >= 0 and time < 7:
#     print ('Ночь')
# elif time >= 7 and time <= 11:
#     print ('Утро')
# elif time >= 12 and time < 17:
#         print ('День')
# elif time >= 17 and time <= 23:
#         print ('Вечер')
# else:
#     print ('Ошибка')

#task 8

# strPre = str(input())
# str1 = strPre.lower()
# print ('Введите время года')
# if str1 == 'лето':
#     print ('Тополинный пух, жара, июль')
# elif str1 == 'зима':
#     print ('Снеговик, снежки и горка')
# elif str1 == 'осень':
#     print ('Пора на учебу!')
# elif str1 == 'весна':
#     print ('Весенняя капель')
# else:
#     print ('Ошибка')

#task 9



#task 10
# print ('Введите ваш год рождения')
# year = int(input())
# if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
#     print ('Вы случайно родились не 29 февраля?')
# else:
#     print ('Ничего необычного')    

#task 11
# print ('введите целое число')
# num = int(input())

# if num == 0:
#     print('нулевое число')
# elif num % 2 == 0 and str(num)[0] != '-':
#     print ('положительное четное число')
# elif num % 2 == 0 and str(num)[0] == '-':
#     print ('Отрицательное четное число')
# elif num % 2 != 0 and str(num)[0] != '-':
#     print ('положительное нечетное число')
# elif num % 2 != 0 and str(num)[0] == '-':
#     print ('отрицательное нечетное число')    


#task 12
# print ('введите целое число')
# num = int(input())
# numList = list(map(int,str(num)))

# if len(numList) == 1:
#     print ('Цифра')
# elif len(numList) == 2:
#     print ('Двузначное')
# elif len(numList) == 3:
#     print ('Трехзначное')
# else:
#     print ('Ошибка')

#task 13
print ('введите положение короля по оси x (от 1 до 8)')
kingPosX = int(input())
print ('введите положение короля по оси y (от 1 до 8)')
kingPosY = int(input())

print ('введите пункт назначения короля по оси x (от 1 до 8)')
kingGoX = int(input())
print ('введите пункт назначения короля по оси y (от 1 до 8)')
kingGoY = int(input())

if kingPosX >= 1 and kingPosX <= 8 and kingPosY >= 1 and kingPosY <= 8 and kingGoX >= 1 and kingGoX <= 8 and kingGoY >= 1 and kingGoY <= 8:
    print ('Координаты введены верно')
else:
    print ('Координаты введены неверно')    


if (kingGoX == kingPosX or kingGoX - kingPosX == 0) and (kingGoY == kingPosY or kingGoY - kingPosY == 0):
 print ('YES')
else:
   print ('NO')
 


