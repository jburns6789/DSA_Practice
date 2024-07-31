# Array methods
# static
# lookup O(1)
# push O(1)
# insert 0(n)
# delete 0(n)
#
# dynamic
# lookup O(1)
# append O(1) O(n) if you have to expand
# insert 0(n)
# delete 0(n)

# if you see a string think arrays

# Pros fast lookups, fast push/pop, ordered
# Cons slow inserts slow deletes fixed size*(if using a static array)

# Reverse a String
string = "Python is fun"
reverse = string[::-1]
#print(reverse)

# List Slicing
my_list = [1, 2, 3, 4, 5, 6]
slice = my_list[2:4]
print(slice)

# Sort a List
my_list2 = [3, 5, 4, 2, 1]
my_list3 = [8, 6, 0, 3, 5]
new_list = my_list3 + my_list2

sorted_asc = sorted(new_list)
print(sorted_asc)