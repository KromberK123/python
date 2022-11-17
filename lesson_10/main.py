# lst = [0, 1, 2, 3, 4, 5]
#
# for mega_yarick in lst:
#     print(mega_yarick)
#
# for super_yarick in range(0, 11): # от 0 до 10 включительно
#     print(super_yarick)

# x1 = int(input("Число: "))
# x2 = int(input("Число: "))
#
# # while x1 <= x2:
# #     print(x1)
# #     x1 += 1
#
# for yarick in range(x1, x2):
#     print(yarick)
#
# while True:
#     try:
#         level = int(input("Ярусов: "))
#     except ValueError:
#         print("Хочу число")
#         continue
#     else:
#         break
#
# while True:
#     char = input("Символ: ").strip()
#     if len(char) == 1:
#         break
#
# for i in range(0, level+1):
#     # левая половина
#     print(" " * (level-i), end="")
#     print(char * i, end="||")
#
#     # правая половина
#     print(char * i)