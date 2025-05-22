from threading import Thread
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(8):
            print("hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(8):
            print("hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()  # to wait for threads to rejoin before moving ahead
t2.join()
print("Bye")
