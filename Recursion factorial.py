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
