toppointer = -1
size = 10
stack = ["" for i in range(size)]

#move toppointer up, then add element
#LIFO (last in first out)
def push (newdata):
#global ni kalau kita tukar the value in subroutine
    global toppointer
    if toppointer + 1 >= size:
        print("stack is full")
    else:
        toppointer = toppointer + 1
        stack[toppointer] = newdata
        print(stack)

def pop():
    global toppointer
    if toppointer < 0 :
        print("stack is empty")
    else:
        toppointer = toppointer - 1

push(7)
push(32)
pop()
pop()
pop()
push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
push(7)
push(8)
push(9)
push(10)
push(11)
