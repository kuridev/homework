# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

user_input = int(input('Please enter a number: '))
even = []
odd = []

for i  in range(1,user_input+1):
    if user_input %i == 0:
        even.append(i)

    elif user_input %i > 0:
        odd.append(i)
        
print('Divisiors: {}'.format(even))
print('Not Divisiors: {}'.format(odd))
        