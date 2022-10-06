# # многострочный string
# x = "Ярик\nЯрик\nЯрик"
# x1 = """Строчка 1
# Строчка 2
# Строчка 3"""
# print(x1)

# # списки (list)
# name_1 ="Ярик"
# name_2 ="Данил"
# name_3 ="Артём"
#
# bratva = [name_1, name_2, name_3]
# print(bratva)
# print(bratva[0]) # вывел Ярика
# print(bratva[-3]) # вывел Ярика

# alphabet = "АБВГДЕЁЖЗИКЛМН"
# print(alphabet[-1]) # Якубович захотел букву "Н"
# print(alphabet[0]) # Якубович захотел букву "A"
# print(alphabet[0] + alphabet[1] + alphabet[2]) # вывести 3 первых
# print(alphabet[:3]) # вывести 3 первых
# print(alphabet[-3:]) # вывести 3 последних
# print(alphabet[:6:2]) # вывести через одного до индекса 6
# print(alphabet[::-1]) # выести в обратном порядке
# print(alphabet[::-2]) # вывести в обратном порядке через 2

# = input("Введи слово: ")
# print("Первая буква:", x[0])
# print("Последняя буква", x[-1])е
# temp = x[-1]
# print(x.index(temp) + 1) # индекс последнего символа + 1
# print(len(x))path
#path = "C:/Python3/python.exe"
# решение, но не крутое
# print("Имя файла: ", path[-10:])
# print("Расширение: ", path[-3:])
# print("Имя каталога: ", path[3:10])
# print("Полный путь к каталогу: ", path[:10])
# решение, но крутое
# temp = path.split("/")
# print(temp)
# print("Имя файла: ", temp[-1])
# print("Расширение: ", temp[-1][-3:])
# print("Имя каталога: ", temp[1])
# print("Полный путь к каталогу: ", temp[0] + "/" + temp[1])

chapter_1 = input("Глава 1: ")
page_1 = input("Страница: ")

chapter_2 = input("Глава 2: ")
page_2 = input("Страница: ")

print(chapter_1.ljust(15), page_1.rjust(15))
print(chapter_2.ljust(15), page_2.rjust(15))