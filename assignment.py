#This is an empty list
my_list = []

#Appending to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

#Insert the value 15 at the second position
my_list.insert(1, 15)

#Another list
another_list = [50, 60, 70]

#Extending my_list
my_list.extend(another_list)


#Removing the last element from my list
del my_list[-1]
print(my_list)


#Sorting my_list
my_list.sort()
print(my_list)


#find and print the index of value 30 in my_list
print(my_list.index(30))