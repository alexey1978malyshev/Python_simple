# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# list = [1, 1, 2, 0, -1, 3, 4, 4]
#
# set = set(list)
#
# print(set)
# print(len(set))

# # Дана последовательность из N целых чисел и число
# # K. Необходимо сдвинуть всю последовательность
# # (сдвиг - циклический) на K элементов вправо, K –
# # положительное число.
# # Input: [1, 2, 3, 4, 5] k = 3
# # Output: [4, 5, 1, 2, 3]
# # k = 3
# lst = [1, 2, 3, 4, 5]
# # lst_2 = []
# # for i in range(k-1):
# #     lst.insert(0, lst[-1])
# #     lst.pop(-1)
# #
# # print(lst)
#
# new_lst = lst[3:] + lst[:3]
# print(new_lst)

# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

list_of_dict = [{"V": "S001", "X":"D009"},
        {"V": "S002"},
        {"VI": "S001"},
        {"VI": "S005"},
        {"VII": " S005 "},
        {"V": "S009", "D": "S015"},
        {"VIII": "S007"}]

# result_set = set()
# for item in list_of_dict:
#     for i in item.values():
#             result_set.add(i.strip())
# print(result_set)

result = {i.strip() for item in list_of_dict for i in item.values()}
print(result)



