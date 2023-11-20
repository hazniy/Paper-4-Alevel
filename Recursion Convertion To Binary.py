def decitobin(number):
    if number == 1 or number == 0:
        print(number, end='')
    else:
        decitobin(number//2)
        print(number%2, end='' )

#main
num = int(input('enter a number: '))
print('the binary of the number is', decitobin(num))
