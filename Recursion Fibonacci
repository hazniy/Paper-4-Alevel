# Fn = 0,1,1,2,3,5,8,13,21,34,55
# F0 = 0
# F1 = 1
# Fn = Fn-2 + Fn-1
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        ans = fibonacci(n-2) + fibonacci(n-1)
        return ans

#main
num = int(input('enter a number: '))
if num < 0:
   print("Sorry, fibonacci number is positive number")
else:
   print("The fibonacci number of", num, "term is", fibonacci(num))

#for all
for n in range (0,16):
    print(fibonacci(n))
    
