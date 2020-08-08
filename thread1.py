#creating a thread without using a class
from threading import *

#creating function
def display():
    print('love you')
 #creating a thread and run function for 100 times
for i in range(100):
    t=Thread(target=display)
    t.start()