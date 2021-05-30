def accum(s):
    accum_str = ""
    for i in range(len(s)):
        a = s[i]
        a = ((i+1)*a)+'-'
        a = a.capitalize()
        accum_str+=a
    return accum_str
print(accum('cwAt'))
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




