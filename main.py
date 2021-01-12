
def add(x, y):
    return x + y

def subtract(x, y):
    return x -y

def multiply(x, y):    
    return x * y

def divde(x, y):
    return x / y

choice = input('''
    please select type of operation you want to perform:
    + for addition
    - for substraction
    * for multiplication
    / for division
''')

num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))

if choice == '+':
    print(add(num_1,num_2))
elif choice == '-':
    print(subtract(num_1, num_2))
elif choice == '*':
    print(multiply(num_1, num_2))
elif choice == '/':
    print(divde(num_1, num_2))
else:
    print('Enter a valid operator, please run the program again')