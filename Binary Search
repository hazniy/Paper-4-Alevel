mylist = [16, 19, 21, 27, 36, 42, 55, 67, 76, 89]
item = int(input('please enter a number : '))
lowest = 0
highest = len(mylist)-1
Found = False
while lowest <= highest and Found == False :
        middle = lowest + (highest - lowest)//2
        if mylist[middle] == item:
            Found = True
        elif mylist[middle] < item:
            low = middle + 1
        else:
            high = middle - 1
if Found == True :
    print("Element is present at index ", middle)
else:
    print("Not found")
