# 20) Do you speak "English"?
# def sp_eng(sentence):
#     if not sentence.lower().find('english') == -1:
#         return True
#     else:
#         return False
# print(sp_eng('eNgliSh'))


# # 18) Return Two Highest Values in List
# def two_highest(arg1):
#     if arg1 == []:
#         return []
#     lst = []
#     arg1.sort(reverse=True)
#     lst.append(arg1[0])
#     for i in arg1:
#         if i == arg1[0]:
#             continue
#         else:
#             lst.append(i)
#             break
#     return lst
# print(two_highest([]))

# 17) Add Length
# def add_length(str_):
#     lst = str_.split()
#     return [i + " " + str(len(i)) for i in lst]
# print(add_length('hello world'))

# # 16) Reverse List Order
# def reverse_list(l):
#     return l[::-1]
# print(reverse_list([1, 2, 3]))

# #15)Exes and Ohs
# def xo(s):
#     if s.lower().count('x') == s.lower().count('o'):
#         return True
#     else:
#         return False
# print(xo('zbOxx'))


# #14) Count the Monkeys!
# def monkey_count(n):
#     return [*range(1, n+1, 1)]
# print(monkey_count(10))

# #13) Removing Elements
# def remove_every_other(my_list):
#     newlst = []
#     for i in range(len(my_list)):
#         if i % 2 == 0:
#             newlst.append(my_list[i])
#     return newlst
# print(remove_every_other([1, 11, 111, 1111]))


# #12) Square(n) Sum
# def square_sum(numbers):
#     num2 = []
#     for i in numbers:
#         i **= 2
#         num2.append(i)
#     return sum(num2)
# print(square_sum([2, 2, 3]))


# 11) Sort the odd
# def sort_array(source_array):
#     odd_lst = []
#     for i in source_array:
#         if i % 2 == 0:
#             continue
#         else:
#             odd_lst.append(i)
#     odd_lst.sort()
#     k = 0
#     for i in range(len(source_array)):
#         if source_array[i] % 2 != 0:
#             source_array[i] = odd_lst[k]
#         else:
#             continue
#         k += 1
#     return source_array
# print(sort_array([7, 2, 3, 6, 23]))

# # 10) Count of positives / sum of negatives
# def count_positives_sum_negatives(arr):
#     arr2 = []
#     pos = 0
#     neg = 0
#     if len(arr) == 0:
#         arr2.append(pos)
#         arr2.append(neg)
#         return arr2
#     if max(arr) == 0 and min(arr) == 0:
#         return arr2
#     for i in arr:
#         if i > 0:
#             pos += 1
#         else:
#             neg += i
#     return [pos, neg]
# print(count_positives_sum_negatives([5, -5]))

# #9) Kata Sum of two lowest positive integers
# def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     return numbers[0] + numbers[1]
# print(sum_two_smallest_numbers([1, 22, 31, 5]))


# 8) Kata Invert values
# def invert(lst):
#     lst_n = []
#     for i in lst:
#         i *= -1
#         lst_n.append(i)
#     return lst_n
# print(invert([1, -1, 22, -5]))

# 7) Kata8 Regexp Basics - is it a digit?
# def is_digit(n):
#     if len(n) >= 2:
#         return False
#     else:
#         x = n.isdigit()
#     return x
# print(is_digit("5"))

# 6) Kata8 My head is at the wrong end!
# def fix_the_meerkat(arr):
#     arr = arr[::-1]
#     return arr
# print(fix_the_meerkat(['tail', 'body', 'head']))


# 5) Kata Stop gninnipS My sdroW!
# def spin_words(sentence):
#     words = sentence.split()
#     word = ''
#     new_sentence = ''
#
#     for i in range(len(words)):
#         if len(words[i]) >= 5:
#             word = words[i]
#             new_sentence += word[::-1]
#         elif len(words[i]) < 5:
#             word = words[i]
#             new_sentence += word
#
#         if not i == len(words)-1:
#             new_sentence += ' '
#         else:
#             break
#     return new_sentence


# 4) Kata "count sheeps"
# 4.1  solution with for
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
# 2) def make_negative( number ):
#     if number >= 0:
#         return number*(-1)
#     else:
#         return number
#
# print(make_negative(0))

# 1) string1 = " "
# def is_isogram(string):
#     string = str.lower(string)
#     set_str = set(string)
#     if len(string) == len(set_str):
#         return True
#     else:
#         return False
# print(is_isogram(string1))
