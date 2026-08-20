# input = "a1bc234d"
# # output = "a1b2c3d4"
# output = ""
# alpha_list = [item for item in input if item.isalpha()]
# digit_list = [item for item in input if item.isdigit()]
#
# for alpha, digit in zip(alpha_list, digit_list):
#     output = output + alpha + digit
# print(output)
#####################################################################################################
# input = "aaabbccccddd"
# # output = "d3c4b2a3"
# output = ""
# dup_dict = {}
#
# for item in set(input):
#     item_count = input.count(item)
#     if item not in dup_dict:
#         dup_dict[item] = item_count
#
# dup_dict_sort = sorted(dup_dict.items(), key = lambda x:x[0], reverse=True)
# print(dup_dict)
# print(dup_dict_sort)
# for i,j in dict(dup_dict_sort).items():
#     output = output + i + str(j)
# print(output)
###################################################################################################
# input = [1, 3, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, 3, 1, 3, 5, 5, 4, 4, 1, 3, 2, 2, 2, 2]
# k = 3
# output = []
# # output = [2, 3, 1]
# dup_dict = {}
# for digit in set(input):
#     digit_count = input.count(digit)
#     if digit not in dup_dict:
#         dup_dict[digit] = digit_count
# dup_dict_sort = sorted(dup_dict.items(), key=lambda x:x[1], reverse=True)
# for i, key in enumerate(dict(dup_dict_sort).keys()):
#     output.append(key)
#     if i == k-1:
#         break
# print(output)
#####################################################################################################
# def fact(num):
#     if num<=1:
#         return 1
#     else:
#         return num * fact(num-1)
# print(fact(5))
#####################################################################################################
# fib_series = [0, 1]
# for i in range(20-2):
#     fib_series.append(fib_series[-2]+fib_series[-1])
# print(fib_series)
#####################################################################################################
#PRIME SERIES
import math
def is_prime(num):
    if num<=1:
        return False
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num%i == 0:
                return False
        return True

for n in range(50):
    if is_prime(n):
        print(n, end=",")
