my_list = [119,111,3,19]
for value in my_list:
    if value > 100:
        print(value)

####################################################################

my_list = [119, 111, 3, 19]
my_result = []
for value in my_list:
    if value > 100:
        my_result.append(value)
print(my_result)

####################################################################

my_list = [1, 11, 19]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)

####################################################################

my_string = "0123456789"
result = []

for symb_1 in my_string:
    for symb_2 in my_string:
        result.append(int(symb_1 + symb_2))
print(result)