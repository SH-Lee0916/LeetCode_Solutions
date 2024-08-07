'''
https://leetcode.com/problems/print-in-order/description/
'''

from threading import Lock

from typing import Callable


class Foo:
    def __init__(self):
        self.locks = (Lock(), Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.locks[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.locks[0]:
            printSecond()
            self.locks[1].release() 


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.locks[1]:
            printThird()
            

if __name__ == "__main__":
    pass
    # Pass test codes...
    