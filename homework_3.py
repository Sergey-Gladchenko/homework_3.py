value = 211
my_value = int(value / 2) if value < 100 else int(value / (-1))
print(my_value)

#####################################################

value = 19
my_value = int(value / value) if value < 100 else int(value * 0)
print(my_value)

#####################################################

value = 11
my_value = print(True) if value < 100 else print(False)

#####################################################

my_str = "123456789"
my_value = my_str[::2]
print(my_value)

#####################################################

my_str = '123456789'
my_value = my_str[1::2]
print(my_value)

#####################################################

my_str = "karser"
len_my_str = len(my_str)
my_value = str(my_str * 2) if len_my_str < 5 else str(my_str)
print(my_value)

#####################################################

my_str = "kar"
len_my_str = len(my_str)
my_value = str(my_str + my_str[::-1]) if len_my_str <5 else str(my_str)
print(my_value)
