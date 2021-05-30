# Kata "count sheeps"
#4.1  solution with for
# def count_sheeps(sheep):
#     # TODO May the force be with you
#     counter = 0
#     for i in sheep:
#         if i == True:
#             counter += 1
#     return counter
#     pass
# print(count_sheeps([True, True, None, "Djafl", False]))

# 4.2 solution with count
# def count_sheeps(sheep):
#     # TODO May the force be with you
#     return sheep.count(True)
#     pass
# print(count_sheeps([True, True, None, "Djafl", False]))

# 3) Kata "Mumbling"
# def accum(s):
#     accum_str = ""
#     for i in range(len(s)):
#         a = s[i]
#         a = ((i+1)*a) + '-'
#         a = a.capitalize()
#         accum_str += a
#     return accum_str[:-1]
# print(accum('Azamat'))
#2) def make_negative( number ):
#     if number >= 0:
#         return number*(-1)
#     else:
#         return number
#
# print(make_negative(0))

#1) string1 = " "
# def is_isogram(string):
#     string = str.lower(string)
#     set_str = set(string)
#     if len(string) == len(set_str):
#         return True
#     else:
#         return False
# print(is_isogram(string1))




