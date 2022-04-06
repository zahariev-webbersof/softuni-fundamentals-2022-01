from object_and_classes.class_test import GreetingByName


class Person(GreetingByName):
    pass

ivan = Person('Ivan', 'Ivanov')
print(ivan.say_hello())