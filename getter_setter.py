class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self.__name=name
    
person=Person("ritvik",20)

print(person.get_name())
# person.get_age()
person.set_name("ESHU")

print(person.get_name())