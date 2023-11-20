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
