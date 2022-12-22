# ПЕРВЫЙ ЗАДАЧА
# phrase = "РОССИЯ, РОССИЯ, РОССИЯ И БОГДАН! ".title().strip() # тут жесткое опускание
# symbolse = list("!@#$%^&*()1234567890'\",.?") # \" - экранирование
# phrase_clear = "" # щас помоем фразу
# for ovoshi in phrase: # итерироваться по фразе
#     if ovoshi not in symbolse: # если это не спец символ
#         phrase_clear += ovoshi
#
# phrase_list = phrase_clear.split(" ")
# print(phrase_list)
#
# d = {}
# for dom in phrase_list:
#     if dom not in d: # если ключа нет
#         d[dom] = 1 # обозначение нового элемента
#     else: # если ключ есть
#         d[dom] += 1 # плюс один элемент
# print(d)


# ВТОРОЙ ЗАДАЧА
# slojenie = 0
# d = {"Молоко": 100,
#      "Доширак": 21,
#      "Чипсы": 0.5,
#      "Богдан": 999}
# for i in d.values(): # перебор по значениям
#     slojenie += i
# print(slojenie)



# ТРЕТИЙ ЗАДАЧА
# DIE_SIDES = 6
# DIE_COUNT = 2
# d = {}
#
#
# for first in range(1, DIE_SIDES + 1): # от 1 до 6 включительно
#     for second in range(1, DIE_SIDES + 1):
#         if first + second not in d:
#             d[first + second] = [(first, second)]
#         else:
#             d[first+second].append((first, second))
#
# # ВЫВОД
# for tadjikistan in d:
#     print(f"{tadjikistan}: {d[tadjikistan]}")


