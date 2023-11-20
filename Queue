size = 5
numelements = 0
headpointer = 0
tailpointer = -1
queue = ["" for i in range (size)]

#add
#first move tail pointer, then add the element
def Enqueue(NewData):
    global headpointer, tailpointer, numelements
    if numelements >= size:
        print("queue is full")
    else:
        tailpointer = tailpointer + 1
#circular happen here, start to 0 back to add
        if tailpointer > size - 1:
            tailpointer = 0
        queue[tailpointer] = NewData
        numelements = numelements + 1
        print(queue)

#delete
def Dequeu():
    global headpointer, tailpointer, numelements
    if numelements <= 0:
        print("queue is empty")
    else:
        remove = queue[headpointer]
        headpointer = headpointer + 1
        numelements = numelements - 1
#circular happen, which when headpointer point at last array it go back to 0 if element in 0 present
        if headpointer > size-1:
            headpointer = 0
        print(queue)

Enqueue(15)
Enqueue(45)
Dequeu()
Dequeu()
Enqueue(1)
Enqueue(2)
Enqueue(3)
Enqueue(4)
Enqueue(5)
Enqueue(7)

