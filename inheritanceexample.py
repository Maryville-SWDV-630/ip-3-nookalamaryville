class Shoe:
    def __init__(self, color, name, price):
      self.color = color
      self.name = name
      self.price = price
      
    def get_price(self):
        print(self.price)

class Converse(Shoe): # Inherits from Shoe
    def __init__(self, color, name, price, lowOrHighTop, tongueColor, brand):
        Shoe.__init__(self, color, name, price)
        self.lowOrHighTop = lowOrHighTop,
        self.tongueColor = tongueColor
        self.brand = brand
        
    def get_info(self):
        print(self.color,',',self.name,',',self.brand,',',self.lowOrHighTop,',',self.tongueColor,',',self.brand)

class CombatBoot(Shoe): # Inherits from Shoe
    def __init__(self, color, name, price, militaryBranch, desertOrJungle):
        Shoe.__init__(self, color, name, price)
        self.militaryBranch = militaryBranch
        self.desertOrJungle = desertOrJungle
        
    def get_info(self):
        print(self.color,',',self.name,',',self.militaryBranch,',',self.desertOrJungle)

class Sandal(Shoe): # Inherits from Shoe
    def __init__(self, color, name, price, openOrClosedToe, waterproof):
        Shoe.__init__(self, color, name, price)
        self.openOrClosedToe = openOrClosedToe
        self.waterproof = waterproof
        
    def get_info(self):
        print(self.color,',',self.name,',',self.openOrClosedToe,',',self.waterproof)
        
shoe1 = Converse('Blue', 'Seasonal Color Chuck Taylor All Star', 29.99, 'low', 'white', 'sneakers')
shoe1.get_info()