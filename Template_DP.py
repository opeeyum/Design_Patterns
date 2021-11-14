from abc import abstractmethod


class AbstractClass():

    def template_method(self):
        self._primitive_operation_1()
        self._primitive_operation_2()

    @abstractmethod
    def _primitive_operation_1(self):
        pass

    @abstractmethod
    def _primitive_operation_2(self):
        pass


class ConcreteClass(AbstractClass):
    """ Implement the primitive operations """

    def _primitive_operation_1(self):
        pass

    def _primitive_operation_2(self):
        pass

"""Abstract Class"""
class Meal():
    # template method
    def do_meal(self):
        self.get_ingredients()
        self.cook()
        self.eat()
        self.clean_up()

    def eat(self):
        print(f"Mmm, {type(self).__name__} is good.")

    @abstractmethod
    def get_ingredients(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def clean_up(self):
        pass


class Pizza(Meal):
    def get_ingredients(self):
        print("Getting pizza base, pizza sauce, and vegetables")

    def cook(self):
        print("Baking pizza in an oven.")

    def clean_up(self):
        print("Throwing away paper plates.")


class Tea(Meal):
    def get_ingredients(self):
        print("Getting tea leaves, milk and water.")

    def cook(self):
        print("Boliing water, putting tea leaves, adding milk.")

    def clean_up(self):
        print("Doing the dishes")


if __name__ == '__main__':
    meal1 = Pizza()
    meal1.do_meal()
    print("-----"*5)

    meal2 = Tea()
    meal2.do_meal()
    print("-----"*5)