# Create an empty list called my_list.
mylist = []
print(mylist)

# Append the following elements to my_list: 10, 20, 30, 40.
mylist.append(10,)
mylist.append(20,)
mylist.append(30,)
mylist.append(40)
print(mylist)
# Insert the value 15 at the second position in the list.
mylist.insert(1,15)
# Extend my_list with another list: [50, 60, 70].
mylist.extend([50,60,70])
print(mylist)
# Remove the last element from my_list.
mylist.pop()
print(mylist)
# Sort my_list in ascending order.
mylist.sort()   
print(mylist)
# Reverse my_list.
mylist.reverse()
print(mylist)   
# Find and print the index of the value 30 in my_list.
print(mylist.index(30))