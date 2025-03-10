from lib import *

class C (A):
    def f (self):
        print("C")
        
class D (C, B):
    pass

D().d()