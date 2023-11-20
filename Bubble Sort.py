mylist = [27, 19, 36, 42, 16, 89, 21, 16, 55]
print("Unsorted list is", mylist)
upperbound = 9
lowerbound = 0
top = upperbound
Swap = True
while Swap == True or top != 0 :
    for index in range(lowerbound,top-1):
        if mylist[index] > mylist[index+1]:
            temp = mylist[index]
            mylist[index] = mylist[index+1]
            mylist[index+1] = temp
            Swap = False
    top = top-1

print("Sorted Array is ", mylist)

