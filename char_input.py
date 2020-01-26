import datetime
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# user information
user_name = input('What is your name? ')
user_age = int(input('What is your age? '))

# current year
current_year = datetime.datetime.now()
hundyear = 2120
final_year = hundyear - user_age


print('the current year is {}\n'.format(current_year.year))
print(str('The year you will be 100 is {} '.format(final_year)))
