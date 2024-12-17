# it is the blueprint of creating an object
class Person:
    name="Ritivk";
    age=20;
    dish="ramen";
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Dish: {self.dish}");
a=Person()
a.info()