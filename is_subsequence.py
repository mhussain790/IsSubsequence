"""
Author: Masud Hussain
Course: CS162
Assignment: 6C
"""


def is_subsequence(string_1, string_2, count=0):
    """
    Method that takes two strings and a count variable, and returns a boolean value indicating if string_2 is a subsequence of string_1
    :param string_1:
    :param string_2:
    :param count:
    :return: True or False
    """

    # split up each character from the strings into respective lists
    list_1 = []
    list_1[:0] = string_1
    # print(list_1)

    list_2 = []
    list_2[:0] = string_2
    # print(list_2)

    # Store the length of each list
    list_length_1 = len(string_1)
    list_length_2 = len(string_2)

    # Base case
    if list_length_1 == 0 or list_length_2 == 0:
        # print(False)
        return False
    if count < list_length_2:
        if list_2[count] in list_1:
            # print(list_2[count])
            # print(True)
            return True
        else:
            return is_subsequence(string_1, string_2, count + 1)
    else:
        # print(False)
        return False
