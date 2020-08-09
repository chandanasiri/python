from stack import Stack
s = Stack()
choice = 0
while choice<5:
    print('Stack operations')
    print('1 push element')
    print('2 pop element')
    print('3 peep element')
    print('4 search for element')
    print('5 Exit')
    choice = int(input('your choice: '))
    if choice==1:
        element = int(input('enter element:'))
        s.push(element)
    elif choice==2:
        element = s.pop()
        if element == -1:
            print('the stack is empty')
        else:
            print('popped element= ', element)
    elif choice==3:
        element = s.peep()
        print('topmost element= ',element)
    elif choice==4:
        element = int(input('enter element: '))
        pos = s.search(element)
        if pos == 1:
            print('element not found in the stack')
        else:
            print('element found at position: ', pos)
    else:
        break
print('Stack= ', s.display())