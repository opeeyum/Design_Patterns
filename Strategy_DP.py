from abc import abstractmethod


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface()


class Strategy():

    @abstractmethod
    def algorithm_interface(self):
        pass


class Strategy_A(Strategy):
    """Implementation of Algotihms"""
    def algorithm_interface(self):
        pass


class Strategy_B(Strategy):
    def algorithm_interface(self):
        pass


"""A separate class for Item"""
class Product:
    """Contex class"""
    def __init__(self, price, strategy = None):
        self.price = price
        self.strategy = strategy
		
    def price_after_discount(self):
        if self.strategy:
            discount = self.strategy.discount(self.price)
        else:
            discount = 0
        return self.price - discount

    def __str__(self):        
        return f"Price: {self.price}, price after discount: {self.price_after_discount()}"


class Sale_Discount:
    def discount(price):
	    return price * 0.25 + 20

class Regular_Discount:
    def discount(price):
	    return price * 0.20

if __name__ == "__main__":

	print(Product(20000))
	print(Product(20000, strategy = Sale_Discount))
	print(Product(20000, strategy = Regular_Discount))
