class A:
    def do_something(self):
        print('From Class A')
        raise NotImplementedError('Derived Class Must Implemet This Meethod')



class B(A):
    def do_something(self):
        print('From B')

class c(A):
    def do_something(self):
        print('from c')




my_instance = B()
my_instance.do_something()