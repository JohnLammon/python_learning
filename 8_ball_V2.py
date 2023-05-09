import random

print('------------------------------------')
print('Welcome to the magic 8-Ball program!')
print('------------------------------------')
print()
print()

min_val = 0
max_val = 5

#Using a list rather than the if elif statements from the first iteration

input("What is your question? \n")
get_answer = ["Yes", "No", "It is possible", "All signs point to yes", "All signs point to no", "Ask again later"]
get_val = random.randint(min_val, max_val)

print(get_answer[get_val])

input("Press Enter to exit...")