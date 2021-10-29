value = 21
my_value = value / 2 if value < 100 else value * (-1)
print(my_value)

#####################################################

value = 19
my_value = 1 if value < 100 else 0
print(my_value)

#####################################################

value = 110
my_value = True if value < 100 else False
print(my_value)

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
my_value = my_str * 2 if len_my_str < 5 else my_str
print(my_value)

#####################################################

my_str = "kar"
len_my_str = len(my_str)
my_value = my_str + my_str[::-1] if len_my_str <5 else my_str
print(my_value)
