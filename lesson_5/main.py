# x = int(input("Введи число: "))
#
# if 5 < x < 10: # двойное неравенство
#     pass # pass - затычка
#
# if x < 10 and x > 5:
#     print("Ура")
#
# if x < 10 or x > 5: # одно из условий
#     print("Ура")

#СПИСКИ
# name_1 = "Тоха"
# name_2 = "Антонуан"
# name_3 = "Ярик"
# mega_yarick = [name_1, name_2, name_3] # СПИСОК
# # ОПЕРАЦИИ СО СПИСКАМИ:
# mega_yarick.append("Тоша") # добавить элемент в список
# print(mega_yarick)
# mega_yarick.pop(2) # удалить по идексу
# mega_yarick.remove("Тоха") # удалить по значению
#
# print(mega_yarick)
# Индексация несколько раз
# man = [["Ярик", "Гриша"], ["Компутеры", "Настолки"], "Мама"]
# print(man[0] [1]) # Выводим Гришу
# x = 7
# if x == 7 or x > 10:
#     print("ура")
#
# number = float(input("Введи число: "))
# if number < 0: # если
#         print("Отрицательное")
# elif number > 0: # иначе если if + else
#         print("Положительное")
# else: # иначе
#     print("Число, на которое енльзя делить")
# year = int(input("Введи год: "))
# if year % 4 == 0 and (year % 400 ==0 or year % 100 !=0):
#     print("Весокосненько 😎")
# else:
#     print("Не високосненько 😣")

# number_1 = int(input("Введи первое число: "))
# operation = input("Введи операцию (+, -, /, *, **):").strip()
# number_2 = int(input("Введи второе число: "))
# lst = ["+", "-", "/", "*", "**"]
# if operation in lst:
#     if operation == "+":
#         print(number_1 + number_2)
#     elif operation == "-":
#         print(number_1 - number_2)
#     elif operation == "/":
#         print(number_1 / number_2)
#     elif operation == "*":
#         print(number_1 * number_2)
#     elif operation == "**":
#         print(number_1 ** number_2)
# number_1 = int(input("Первое число: "))
# number_2 = int(input("Второе число: "))
# number_3 = int(input("Третье число: "))
#
# spisok = [number_1, number_2, number_3]
# print("Максимальное число:", max(spisok))
# print("Мнимальное число:", min(spi
# ticket = input("Введи номер билета: ")
# if len(ticket) == 6 and ticket.isdigit():
#     first_half = ticket[:3]
#     last_half = ticket[-3:]
#     first_sum = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
#     last_sum = int(last_half[-3]) + int(last_half[-2]) + int(last_half[-1])
#     if first_sum == last_sum:
#         print("Счастливый❤")
#     else:
#         print("Не счастливый💔")
# else:
#     print("У тебя фигня")