#56)

# # 55) BASIC: Making Six Toast.
# def six_toast(num):
#     return abs(num - 6)
# print(six_toast(0))


# # 54) Collatz Conjecture (3n+1)
# def hotpo(n):
#     score = 0
#     if n == 1:
#         return score
#     while n != 1:
#         if n % 2 == 0:
#             n /= 2
#         else:
#             n *= 3
#             n += 1
#         score += 1
#     return score
#
# print(hotpo(6))


# #53)Jenny's secret message
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return f"Hello, {name}!".format(name=name)


# #52)Define a card suit
# def define_suit(card):
#     return {'C': 'clubs', 'D': 'diamonds', 'H': 'hearts', 'S': 'spades'}[card[-1]]

# print(define_suit('3C'))
# Good luck
# # 51)Is it a number?
# def isDigit(string):
#     try:
#         int(float(string))
#         return True
#     except:
#         return False

# # 50) Multiple of index
# def multiple_of_index(arr):
#     return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]
# print(multiple_of_index([22, -6, 32, 82, 9, 25]))

# # 49)The 'if' function
# def _if(bool, func1, func2):
#     return func1() if bool else func2()
#
# print(_if())
# # 48) Expressions Matter
# def expression_matter(a, b, c):
#     if (a == 1 and c == 1) or (a == 1 and b == 1 and c == 1):
#         return a + b + c
#     elif b == 1:
#         return  ((a + b) * c) if a < c else (a * (b + c))
#     elif a == 1:
#         return ((a + b) * c)
#     elif c == 1:
#         return (a * (b + c))
#     else: return a * b * c
# print(expression_matter(3, 2, 1))

# #47) Get Planet Name By ID
# def get_planet_name(id):
#     # This doesn't work; Fix it!
#     switcher = {
#     1: "Mercury",
#     2: "Venus",
#     3: "Earth",
#     4: "Mars",
#     5: "Jupiter",
#     6: "Saturn",
#     7: "Uranus",
#     8: "Neptune"
#     }
#     return switcher.get(id)
#
# print(get_planet_name(2))

#46) Capitalization and Mutability
# def capitalize_word(word):
#     return word.capitalize()
    # return "".join(char.upper() for char in word)


# # 44)Array plus array
# def array_plus_array(arr1,arr2):
#     return sum(arr1)+sum(arr2)
#
# print(array_plus_array([1, 2, 3], [4, 5, 6]))

# # 43) Check the exam
# def check_exam(arr1,arr2):
#     score = 0
#     for i in range(len(arr1)):
#         if arr1[i] == arr2[i]:
#             score += 4
#         if arr2[i] == '':
#             continue
#         if not arr1[i] == arr2[i]:
#             score -= 1
#     return 0 if score < 0 else score
#
# print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]))
# # 42) CSV representation of array
# def to_csv_text(array):
#     str1 = ''
#     array1 = []
#     for i in array:
#         array1.append([str(k) for k in i])
#     for a in array1:
#         for b in a:
#             str1 += b + ','
#         str1 = str1.rstrip(', ')
#         str1 += '\n'
#     return str1[:-1]
# #    return '\n'.join(f'{x}' for x in array1[len(array1)])
#
# print(to_csv_text([[0, 1, 2, 3, 45],
#                   [10, 11, 12, 13, 14],
#                   [20, 21, 22, 23, 24],
#                   [30, 31, 32, 33, 34]]))


#41)  L1: Bartender, drinks!
# def get_drink_by_profession(param):
#     names = {
#         "Jabroni": "Patron Tequila",
#         "School Counselor":	"Anything with Alcohol",
#         "Programmer":	"Hipster Craft Beer",
#         "Bike Gang Member":	"Moonshine",
#         "Politician":	"Your tax dollars",
#         "Rapper":	"Cristal"
#     }
#     return 'Beer' if not param.lower().title() in names else names[param.lower().title()]


# # 39)  Regular Ball Super Ball
# def boolean_to_string(b):
#     return  str(b)


#38) Find Maximum and Minimum Values of a List
# def minimum(arr):
#     return min(arr)
#
# def maximum(arr):
#     return max(arr)

# #37) Can we divide it?
# def is_divide_by(number, a, b):
#     return True if number % a == 0 and number % b == 0 else False


# 36) Filter out the geese
# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# def goose_filter(birds):
#     n_birds = []
#     for i in birds:
#         if not i in geese:
#             n_birds.append(i)
#         else:
#             continue
#     return n_birds



#35) Drink about
# def people_with_age_drink(age):
#     if age < 14:
#         return 'drink toddy'
#     if age >= 14 and age < 18:
#         return 'drink coke'
#     if age >= 18 and age < 21:
#         return 'drink beer'
#     if age >= 21:
#         return 'drink whisky'


# #34)  Grasshopper - Personalized Message
# def greet(name, owner):
#     if name == owner:
#         return 'Hello boss'
#     if not name == owner:
#         return 'Hello guest'


# #33)  Multiplication table for number
# def multi_table(number):
#     multstr = ''
#     for i in range(1, 11):
#         multstr += str(i) + ' * ' + str(number) + ' = ' + str(i * number) + '\n'
#     return multstr[:-1]


# #31) Double Char
# def double_char(s):
#     return ''.join(f'{i}' * 2 for i in s)
# print(double_char("Hello World"))
# # 30) Unfinished Loop - Bug Fixing #1
# def create_array(n):
#     res = []
#     i = 1
#     while i <= n:
#         res += [i]
#         i += 1
#     return res
# print(create_array(6))

# #29) Fix the loop!
# def list_animals(animals):
#     list1 = ''
#     for i in range(len(animals)):
#         list1 += str(i + 1) + '. ' + animals[i] + '\n'
#     return list1
#
# print(list_animals([ 'dog', 'cat', 'elephant' ]))

# #28) Sum of multiples
# def sum_mul(n, m):
#     if n <= 0 or m <= 0:
#         return 'INVALID'
#     if n == m:
#         return 0
#     lst = list(range(n, m+1))
#     lst2 = []
#     for i in lst:
#         if i % n == 0:
#             lst2.append(i)
#         else:
#             continue
#     return sum(lst2)
#
# print(sum_mul(0, 2))
# # 27) Sentence smash
# def smash(words):
#     return ' '.join(words)
# print(smash(["hello"]))

# # 26)If you can't sleep, just count sheep!!
# def count_sheep(n):
#     lst = list(range(1, n+1))
#     sep = ' sheep...'
#     newstr = sep.join(str(i) for i in lst)
#     return newstr + ' sheep...'
# print(count_sheep(3))

# 25) Sum Arrays
# def sum_array(a):
#     if a == []:
#         return 0
#     return float(sum(a))
# print(sum_array([]))
# # 24) Grasshopper - Summation
# def summation(num):
#     return sum(range(1, num+1))
# print(summation(3))

# # 23) A wolf in sheep's clothing
# def warn_the_sheep(queue):
#     if queue[-1] == 'wolf':
#         return 'Pls go away and stop eating my sheep'
#     for i in range(len(queue)):
#         if queue[i] == 'wolf':
#             return 'Oi! Sheep number ' + str((len(queue)-i)-1) + '! You are about to be eaten by a wolf!'
# print(warn_the_sheep(["sheep", "sheep", "sheep", "sheep", "wolf"]))


# # 22)Lario and Muigi Pipe Problem
# def pipe_fix(nums):
#     return [* range(nums[0], nums[-1] + 1)]
# print(pipe_fix([1, 2, 4]))

# #21) Remove First and Last Character
# def remove_char(s):
#     return s[1:-1]

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
