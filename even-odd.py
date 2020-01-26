# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

user_input = int(input('Enter a number please: '))
even_message = 'your number is a even number'
odd_message = 'your number is a odd number'

if user_input % 2 == 0:
    print(even_message)

elif user_input %2 != 0:
    print(odd_message)
    