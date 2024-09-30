#create a function
def factorial(number):
    if number == 0:
        return 1
    else:
        answer = number * factorial(number - 1)
        return answer

#main
num = int(input('enter a number: '))
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
else:
   print("The factorial of", num, "is", factorial(num))

#basic factorial (example 10) 
factorial = 1 
i = 1 
while i <=10: #(n =10)
    factorial = factorial * i 
    i = i + 1 
print("10! =", factorial) 

#first homework MAS 117
#3
x = 13
y = 21
x = y + 10
y = x + 10 
print("x = ", x, "and y = ", y)

x = 13 
y = 21
x, y = y +10, x+10 
print("x = ", x, "and y = ", y)

#4 triangular number program (recursion)
n = int(input("enter a number: "))
triangular = 0
i = 1

if n == 0: 
    print("maths error bruh")
else: 
    while i <= n: 
        formula = 1/(i**2)
        triangular = triangular + formula
        i = i + 1
    print(triangular) 
   
