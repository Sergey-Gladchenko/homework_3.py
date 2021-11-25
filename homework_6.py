persons = [{"name": "John", "age": 15}, {"name": "Jack", "age": 45}]


sort_age = sorted(persons, key=lambda item: item["age"], reverse=False)
for index in sort_age:
    if index.get("age") == sort_age[0].get("age"):
        print(index.get("name"))

#-------------------------------------------------------------------------------------------------#

sort_ages = sorted(persons, key=lambda item: len(item["name"]), reverse=True)
for index1 in sort_ages:
    if len(index1.get("name")) == len(sort_ages[0].get("name")):
        print(index1.get("name"))

#-------------------------------------------------------------------------------------------------#

sum_age = 0
for index2 in persons:
    sum_age += index2.get("age")
if len(persons) > 0:
    result = sum_age/len(persons)
else:
    result = "No dictionary"
print(result)


####################################################################################################

my_dict = {i: i**2 for i in range(1, 10, 2)}
my_dict1 = {i: i**2 for i in range(2, 10, 3)}
print(my_dict)
print(my_dict1)

#-------------------------------------------------------------------------------------------------#

my_list = list(set(list(my_dict)).intersection(list(my_dict1)))
print(my_list)

#-------------------------------------------------------------------------------------------------#

my_list1 = list(set(list(my_dict)).difference(list(my_dict1)))
print(my_list1)

#-------------------------------------------------------------------------------------------------#

my_dict2 = {}
for item2 in my_list1:
    my_dict2[item2] = my_dict.get(item2)
print(my_dict2)

#-------------------------------------------------------------------------------------------------#
my_dict3 = my_dict
my_dict3.update(my_dict1)
for item3 in my_list:
    my_dict3.pop(item3)
print(my_dict3)

#-------------------------------------------------------------------------------------------------#

my_dict4 = my_dict
my_dict4.update(my_dict1)
for item4 in my_list:
    my_dict4[item4] = [my_dict[item4], my_dict1[item4]]
print(my_dict4)
