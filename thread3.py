#multitasking using two threads
from threading import *
from time import *
class Theatre:
    def __init__(self,  str):
        self.str = str
    def movieshow(self):
        for i in range(1,6):
            print(self.str,":",i)
            sleep(0)
#create two instances to theatre class
obj1 = Theatre('cut ticket')
obj2 = Theatre('show chair')
#create two threads to run moviwshow()
t1 = Thread(target=obj1.movieshow)
t2 = Thread(target=obj2.movieshow)
#run methods
t1.start()
t2.start()