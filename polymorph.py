class animal:
    def speak(self):
        print("Animal Speaking")
class Elephant(animal):
    def speak(self):
        print ("Elephant Speaking")
anm=animal();
el=Elephant();
Elephant.speak(animal);


