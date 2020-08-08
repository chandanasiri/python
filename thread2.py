#single task using  single thread
from threading import *
from time import  *

#create our own class
class Mythread:
    def preparebiryani(self):
        self.task1()
        self.task2()
        self.task3()
        self.task4()
    def task1(self):
        print("Do marination of chicken for 3 hours")
        sleep(5)
        print("its done")
    def task2(self):
        print("fry the chicken in handi and boil rice seperatly ")
        sleep(6)
        print("its done")
    def task3(self):
        print("add the rice to chicken handi")
        sleep(7)
        print("its done")
    def task4(self):
        print("now serve it...................")
        sleep(6)
obj=Mythread()
t=Thread(target=obj.preparebiryani)
t.start()