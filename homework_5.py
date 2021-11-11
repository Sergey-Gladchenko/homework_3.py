my_int = 500300100200
result = str(my_int)
print(result.count('0'))

##########################################################

my_int = 500300
my_str = str(my_int)
result = len(my_str) - len(my_str.rstrip('0'))
print(result)

##########################################################

my_list_1 = ['1', '2', '3', '4', '5']
my_list_2 = ['0', '9', '8', '7', '6']

result = my_list_1[::2] + my_list_2[1::2]
print(result)

##########################################################

my_list = [1, 2, 3, 4, 5]
new_list = my_list[1:] + [my_list[0]]
print(f'{new_list=}')

##########################################################

my_list = [1, 2, 3, 4, 5]
list_value = my_list.pop(0)
my_list.append(list_value)
print(my_list)

##########################################################

my_str = "55 больше чем 11 но меньше чем 99"
my_str_list = my_str.split()
counter = 0

for item in my_str_list:
    if item.isdigit():
        counter += int(item)

print(counter)

##########################################################

my_str = "My long string"
l_limit, r_limit = 'o', 'g'
l_index = my_str.find(l_limit) + 1
r_index = my_str.rfind(r_limit)
sub_str = my_str[l_index: r_index]

print(sub_str)

##########################################################

example = 'abcde'
result_list = []
example_lenght = len(example)

for index in range(0, example_lenght, 2):
    if index < example_lenght - 1:
        result_list.append(example[index] + example[index + 1])
    else:
        result_list.append(example[index] + '_')

print(result_list)

##########################################################

my_list = [2, 4, 1, 5, 3, 9, 0, 7]
counter = 0

for index in range(1, len(my_list) - 1):
    if my_list[index] > sum([my_list[index - 1], my_list[index + 1]]):
        counter += 1

print(counter)