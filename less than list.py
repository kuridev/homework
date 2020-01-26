# Take a list and write a program that prints out all the elements of the list that are less than 5.
my_list = [1,2,3,4,5]
print([x for x in my_list if x in range(0,5)])