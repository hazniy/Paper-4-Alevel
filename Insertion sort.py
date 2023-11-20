#hodder
mylist = [53,21,69,18,42]
Highlist = len(mylist)
Lowlist = 0
for index in range (Lowlist+1, Highlist):
    current = mylist[index]
    left = index-1
    if mylist [left] > current:
        while left >= Lowlist and mylist[left] > current:
            temp = mylist[left+1]
            mylist[left+1] = mylist[left]
            mylist[left] = temp
            left = left -1
print('sorted array is', mylist)

#langfield
mylist2 = [53,21,69,18,42]
numitem = 5
for i in range(1,numitem):
    iteminsert = mylist2[i]
    x = i -1
    while (mylist2[x] > iteminsert) and (x>-1):
        mylist2 [x+1] = mylist2[x]
        x = x-1
    mylist2[x+1] = iteminsert
print(mylist2)
