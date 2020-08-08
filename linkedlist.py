linkedlist=[]
linkedlist.append("swift")
linkedlist.append("verito")
linkedlist.append("waganor")
linkedlist.append("alto")
#display  your list
print("the existing list=",linkedlist)
choice=0
while choice<5:
    print('linked list operations')
    print('1.append')
    print('2.remove')
    print('3.replace')
    print('4.search')
    print('5.exit')
    choice = int(input('your choice'))
    if choice==1:
        element = input('enter element:')
        pos = int(input("at what position? "))
        linkedlist.insert(pos,element)
    elif choice==2:
        try:
            element = input('enter element:')
            linkedlist.remove(element)
        except ValueError:
            print('Element not found')
    elif choice==3:
        element = input("enter new element:")
        pos = int(input("at what position?"))
        linkedlist.pop(pos)
        linkedlist.insert(pos,element)
    elif choice==4:
        element = input("enter elements")
        try:
            pos = linkedlist.index(element)
            print('element found at position: ',pos)
        except ValueError:
            print('element not found')
    else:
        break
    print('list =',linkedlist)
