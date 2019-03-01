print('How many numbers?')
x = 0

while x < 11:
   x = x + 1
   x+= 1

print("Would you like to continue? ")
user_input = input, ('y','n')
if user_input == 'y':
   print(range(0,11))
elif user_input == 'n':
   print('exit')