
#getting positive integers:

list1= [12,-7,5,64,-14]
list2 = [12,14,-95,3]

new_list = [str(num) for num in list1 if num >= 0]
string = ', '.join(new_list)
print(string)



modified_list = []

for num in list2:
    if num >= 0:
        modified_list.append(num)

print(modified_list)
    