# Magic 8-Ball
import random

print('------------------------------------')
print('Welcome to the magic 8-Ball program!')
print('------------------------------------')
print()
print()

min_val = 1 
max_val = 6
input("What is your question? \n")
answer = random.randint(min_val, max_val)

# I know there is a better way to do this but I haven't learned it yet. So, here we are.

if (answer == 1):
    print('Yes')
elif (answer == 2):
    print('No')
elif (answer == 3):
    print('It is possible')
elif (answer == 4):
    print('All signs point to yes')
elif (answer == 5):
    print('All signs point to no')
elif (answer == 6):
    print('Ask again later')

input('Press enter to exit...')