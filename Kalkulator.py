def kalkulator():
    try:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        operation = (input("Enter the operation (+, -, *, /): "))
        operation_dict = {
            '+' : lambda a, b:a + b,
            '-' : lambda a, b:a - b,
            '*' : lambda a, b:a * b,
            '/' : lambda a, b:a / b if b != 0 else 'ERROR! CANT BE DIVIDED BY 0 or ZERO.'
        }  
        
        if operation in operation_dict:
            result = operation_dict[operation](x, y)
            print(f'Answer of {x} {operation} {y} = {result}')
        else:
            print('Operation is not valid.')
    except ValueError:
        print('Something went wrong.')
kalkulator()
    
