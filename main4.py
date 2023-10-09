class BaseOne:
    def __init__(self):
        print("Base One")

    def func_one(self):
        print('one')



class BaseTwo:
    def __init__(self):
        print("Base Two")

    def func_Two(self):
        print('two')

class Derived(BaseOne,BaseTwo):
    pass

my_var = Derived()



class Base:
    pass

class DerivedOne(Base):
    pass


class DeerivedTwo(DerivedOne):
    pass


# print(my_var.func_one)
# print(my_var.func_Two)

# my_var.func_one()
# my_var.func_Two()

# print(Derived.mro())