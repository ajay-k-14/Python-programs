print("Calculator with basic operations")
print("Available operations: +, -, *, /")

print("Enter two numbers:")
x=int(input())
y=int(input())
print("Enter the operation you want to perform:")
operation=input()

if operation=='+':
    print("Answer is:", x+y)
elif operation=='-':
    print("Answer is:", x-y)
elif operation=='*':
    print("Answer is:", x*y)
elif operation=='/' and y!=0 or x!=0:
    print("Answer is:", x/y)
else:
    print("Invalid operation or division by zero!")