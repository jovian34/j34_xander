a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

operator = input('Do you want to Add(a), subtract(s), multiply(m) or divide(d)?: ')

if (operator[0] == 'a'):
    c = a + b
elif (operator[0] == 's'):
    c = a - b
elif (operator[0] == 'm'):
    c = a * b
elif (operator[0] == 'd'):
    c = a / b
    
print('Your result is', c)
