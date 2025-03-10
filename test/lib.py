class A:
    def f (self):
        print("A")
        
class B(A):
    def d (self):
        super().f()