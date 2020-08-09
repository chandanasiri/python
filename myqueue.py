from que1 import Queue
q=Queue()
choice=0
while choice<4:
    print('queue operations')
    print('1 Add element')
    print('2 delete element')
    print('3 search for element')
    print('4 exit')
    choice = int(input('your choice: '))
    if choice==1:
        element = float(input('enter element: '))
        q.add(element)
    elif choice==2:
        element = q.delete()
        if element == -1:
            print('the queue is empty')
        else:
            print('remove element= ',element)
    elif choice==3:
        element = float(input('enter element: '))
        pos = q.search(element)
        if pos == -1:
            print('the queue is empty')
        elif pos ==-2:
            print('element not found in the queue')
        else:
            print('element found at position: ', pos)
    else:
        break
print('Queue= ',q.display())