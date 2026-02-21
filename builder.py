class BurgerMeal:
    def __init__(self,builder):
        self.bun=builder.bun
        self.pattie=builder.pattie
        
        ##optional
        self.cheese=builder.cheese
        self.coke=builder.coke
        self.salad=builder.salad
        

        class Bugerbuilder:
            def __init__(self,bun,pattie):
                self.bun=bun
                self.pattie=pattie

                ##optional
                self.cheese=False
                self.coke=False
                self.salad=False
            
            def withcheese(self,cheese):
                self.cheese=cheese
                return self
            
            def withcoke(slef,coke):
                self.coke=coke
                return self
                       
            def withsalad(self,salad):
                self.salad=salad
                return self 

            def build(self):
                BurgerMeal(self)

plain_burger = BurgerMeal.BurgerBuilder("wheat", "veg").build()

# Burger with cheese only
burger_with_cheese = (
    BurgerMeal.BurgerBuilder("wheat", "veg")
    .withcheese(True)
    .build()
)
