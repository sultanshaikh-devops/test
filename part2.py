file_name = 'C:\Work\Exercises\calc\calc.txt'
total_sumvalue = 0


def add(x, y):
    return x + y

def subtract(x, y):
    return x -y

def multiply(x, y):    
    return x * y

def divde(x, y):
    return x / y

with open(file_name, 'r') as file:
    filedata = file.read().splitlines()

for data in filedata:
    process_data = data.split(" ")
    if process_data[1] == '+':
        result = add(float(process_data[2]),float(process_data[3]))
    elif process_data[1] == '-':
        result = subtract(float(process_data[2]),float(process_data[3])) 
    elif process_data[1] == '/':
        result = divde(float(process_data[2]),float(process_data[3]))
    elif process_data[1] == 'x':
        result = multiply(float(process_data[2]),float(process_data[3]))  
    else:
        result = 'Invalid operator found!'
    
    ans = float('{:.2f}'.format(result))
    total_sumvalue = total_sumvalue + ans  
    print('{:.2f}'.format(ans))
    print('{:.2f}'.format(total_sumvalue))