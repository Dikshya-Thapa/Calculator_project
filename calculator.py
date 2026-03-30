def add_numbers(num1, num2):
    result = num1 + num2
def subtract_numbers(num1, num2):
    result = num1 - num2
    return result

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Result:", add_numbers(a, b)) 
print("Result:", subtract_numbers(a, b))
