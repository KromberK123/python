# ZeroDivisionError
# x = 5/0

# TypeError
# = "а" + 15

# IndexError
# x = [0, -15, "Антон"]
# x[3]

# SyntaxError
# x = "Привет, я Ярик.

# NameError
# x = "Я строчка"
#
# print(x2)

# assert --> AssertionError
# def summa(numbers):
#     return sum(numbers)
#
# # print(summa([3,4]))
#
# assert summa([1, 2]) == 3
# assert summa([1, 2]) == 4


# try - попытаться
# expect - отлавление исключений
# else - иначе, когда нету ошибок (если всё хорошо)
# Finally - в любом случае
# try:
#     number = int(input())
#     x = 5 / number
# except ZeroDivisionError:
#     print("Слышь ты, овощь, низя на ноль делить")
# except ValueError:
#     print("Хочу цифирки")
# except Exception: # любая ошибка бдует обработана
#     print("Блин, ты ошибся, получается! ")
# else: # когда всё хорошо 🥰
#     print("Я поделив 👉👈")
# finally:
#     print("Меня написал Ярик. Все права защищены.")
#
# print("Я закончил работать.")


# PASS
# try:
#     number = int(input())
#     x = 5 / 0
# except Exception:
#     pass # затычка. ничего не произойдёт

# if 5 == 5:
#     pass #TODO: купить молока и дописать код
# try:
#     x = input("Введи имя: ")
#     if x == "Ярик":
#         raise Exception("Ярика в обиду не дам!")
#     # raise - вызвать исключение/ошибку
# except Exception as error_message:
#     # as -  сохранить ошибку в error_message
#     print("Это слово заперщено!", error_message)
#
# ints = []
# try:
#     f = open("df.txt")
# except FileNotFoundError:
#     print("Ну не получилось😔")
# else:
#     try:
#         for line in f:
#             ints.append(int(line))
#     except ValueError:
#         print("Тут не число, закрой за мной дверь , я ухожу.")
#     else: # если ошибок нет
#         print(ints)
#     finally: # всегда
#         f.close()
#         print("Я закрыл файл")