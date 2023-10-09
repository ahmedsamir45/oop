class Food:
    def __init__(self , name , price):
        self.name = name
        self.price = price

        print(f"{self.name} Is Created From Base Class")
        
    def eat(self):
        print("Wat Method From Base Class")


class Apple(Food):
    def __init__(self , name , price , amount):


        # Food.__init__(self,name)

        super().__init__(name,price)
        self.amount = amount


        print(f"{self.name} Is Created From Derived Class And Is {self.price} And Amount Is {self.amount} ")

    def get_from_tree(self):
        print('Get From Tree from Derived Class')

    def eat(self):
        print("Wat Method From Derived Class")

# food_one = Food('banana')
food_two = Apple('pizza', 150 , 500)
food_two.eat()
food_two.get_from_tree()