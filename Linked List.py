#heapstartpointer always after startpointer
heapstartpointer = 5
#startpointer will increase and follow the index value not none
startpointer = 4
#index 11 which the last pointer
nullpointer = -1
myLinkedList = [27,19,36,42,16,None,None,None,None,None,None,None]
myLinkedListPointers = [-1,0,1,2,3,6,7,8,9,10,11,-1]

def find(itemsearch):
    found = False
    itempointer = startpointer
    while (itempointer != nullpointer) and found == False:
        if myLinkedList[itempointer] == itemsearch:
            found = True
        else:
            #keep looping until null pointer
            itempointer = myLinkedListPointers[itempointer]
    return itempointer

itemsearch = int(input('please enter a num '))
result = find(itemsearch)
if result == -1 :
    print("not found")
else:
    print("found")

#add at the beginning
#add at the end
#add between nodes
def linkedListAdd(itemadd):
    global heapstartpointer, startpointer
    if heapstartpointer == nullpointer:
        print('linked list full')
    else:
        tempPointer = startpointer
        startpointer = heapstartpointer
        heapstartpointer = myLinkedListPointers[heapstartpointer]
        myLinkedList[startpointer] = itemadd
        myLinkedListPointers[startpointer] = tempPointer
        print("new list after added", myLinkedList, myLinkedListPointers)

linkedListAdd(32)

def LinkedListdelete (itemdel):
    global heapstartpointer
    if startpointer == nullpointer:
        print('linked list empty')
    else:
        index = startpointer
        while myLinkedList[index] != itemdel and (index != nullpointer):
            oldindex = index
            index = myLinkedListPointers[index]
        if index == nullpointer:
            print('item not found')
        else:
            tempPointer = myLinkedListPointers[index]
            myLinkedListPointers[index]=heapstartpointer
            heapstartpointer = index
            myLinkedListPointers[oldindex]=tempPointer
            myLinkedList[index] = None
            print('new list after delete', myLinkedList,myLinkedListPointers)

LinkedListdelete(36)
