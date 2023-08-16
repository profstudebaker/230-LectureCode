# # my_list = [7,8,10]
# # my_list.append(12)
# # print(my_list)
# # # remove by value, not position
# # my_list.remove(7)
# # print(my_list)
# # # pop is remove by position
# # my_list.pop(0)
# # print(my_list)

# # items_in_list = len(my_list)
# # print(items_in_list)



# my_int = 8
# another_int = my_int
# another_int += 1
# print(my_int, another_int)
# my_str = "Hello!"
# my_list = [0,1,2]
# another_list = my_list
# another_list.append(12)
# print(my_list, another_list)
# a_copied_list = my_list.copy()
# a_copied_list.append(32)
# print(my_list, a_copied_list)

# # list comprehension
data = [8, 12, 34, 20, 17, 60]
# # VALUE_IF_TRUE for ITEM in LIST if CONDITION
# not_minors = [number for number in data if number >= 18]
# # VALUE_IF_TRUE if CONDITION else VALUE_IF_FALSE for ITEM in LIST 
not_minors_with_default = [number if number >= 18 else 18 for number in data]
print(not_minors_with_default)

# list_of_defaults = [0.0] * 10
# print(list_of_defaults)

# words = ("do","not","change","me!")
# # words.append("or else!")
# print(words[-1])






