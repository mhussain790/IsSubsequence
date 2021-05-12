"""
Author: Masud Hussain
Course: CS162
Assignment: 6C
"""


# def is_subsequence(string_1, string_2):
#     list_1 = string_1
#     list_2 = string_2
#
#     list_length_1 = len(string_1)
#     list_length_2 = len(string_2)
#
#     if list_length_1 == 0 and list_length_2 == 0:
#         return False
#     # elif list_length_1 >= 0 and list_length_2 == 0:
#     #     print(True)
#     #     return True
#     # # if list_length_1 == 0 and list_length_2 >= 0:
#     # #     new_string_2 = string_2[1:list_length_2:]
#     # #     is_subsequence(list_1, new_string_2)
#     # # el
#
#     if string_1[:0] == string_2[:0]:
#         print(string_1)
#         print(string_2)
#
#         new_string_1 = string_1[1:list_length_1:]
#         new_string_2 = string_2[1:list_length_2:]
#
#         print(True)
#         return True
#     elif string_1[:0] != string_2[:0]:
#         list_length_1 = len(string_1)
#         list_length_2 = len(string_2)
#
#         new_string_1 = string_1[1:list_length_1:]
#
#         print(string_1)
#         print(string_2)
#
#         is_subsequence(new_string_1, string_2)
#
#
# is_subsequence("hen", "marj")

def is_subsequence(string_1, string_2, count=0):
    list_1 = []
    list_1[:0] = string_1
    print(list_1)

    list_2 = []
    list_2[:0] = string_2
    print(list_2)

    list_length_1 = len(string_1)
    list_length_2 = len(string_2)

    if list_length_1 == 0 or list_length_2 == 0:
        print(False)
        return False
    if count < list_length_2:
        if list_2[count] in list_1:
            print(list_2[count])
            print(True)
            return True
        else:
            return is_subsequence(string_1, string_2, count + 1)
    else:
        print(False)
        return False