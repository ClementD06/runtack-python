#Job5

def calcule (num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    else:
        print("Opérateur invalide")

print(calcule(5, '+', 3)) 
print(calcule(10, '-', 4))  
print(calcule(2, '*', 6))  
print(calcule(15, '/', 3))  
print(calcule(17, '%', 5))   