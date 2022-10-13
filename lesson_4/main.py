# familiya = input("Фамилия: ").capitalize()
# imya = input("Имя: ").capitalize()
# otchectvo = input("Отчество: ").capitalize()
# print(familiya, imya[0] + ".", otchectvo[0] + ".")
# print(f"{familiya} {imya[0]}. {otchectvo[0]}.
# word = input("Введи фразу: ")
# word.count("а")
# print(word.count("а"))
# print(word.count("аб"))
# phrase = input("Веди фразу, разделенную пробелами: ").strip()
# lst = phrase.split(" ")
# print(lst)
# lst.pop(0) # удалить по индексу
# lst.remove("Ярик") # удалить по значению
# print(lst)
# phrase = input("Введи фразу: ")
# find = input("Что меняем: ")
# replace = input("На что меняем: ")
#
# print(phrase.replace(find, replace))
# # .replace() - замена первого элемента на второй
# x = input()
# prin
alphabet = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "е",
    "ё": "yo",
    "ж": "zh",
}
phrase = input("Введи фразу: ")
translate = ""
for bukva in phrase:
    translate = translate + alphabet[bukva]
print(translate)