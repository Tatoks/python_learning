# [2,2,3,5,5]. Remove duplicate elements and print

my_list = [2, 2, 3, 3, 4, 5, 6, 7, 7]

new_list: list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
