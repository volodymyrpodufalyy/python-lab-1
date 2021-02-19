class Parfums:
    fragnance_author = "Nathalie Lorson"
    def __init__(self,fragrance_type,brand,composition,name = "Encre Noire",volume = 100,price = 590):
            self.name = name
            self.volume = volume
            self.price = price
            self.brand = brand
            self.composition = composition
            self.fragrance_type = fragrance_type
    def __del__(self):
        del self
    def __str__(self):
        return f"{self.brand} {self.name} \n {self.volume}ml \n {self.price} грн \n" \
         f" Склад:{self.composition} \n {self.fragrance_type} "
    @staticmethod
    def static_method(value):
         print(value)