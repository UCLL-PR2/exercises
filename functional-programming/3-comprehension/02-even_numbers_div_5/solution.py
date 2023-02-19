
def even_nums_divisible_by_5():
    l = [x for x in range(1,101) if x % 2 == 0 and x % 5 == 0]
    return l


# Solution without list comprehension 

# even_nums_divisible_by_5 = []
# for x in range(1,101):
#     if x % 2 == 0 and x % 5 == 0:
#         even_nums_divisible_by_5.append(x)

# print(even_nums_divisible_by_5)