class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name :<6}: $ {self.price}"

class MenuIterator:
    def __init__(self, items):
        self.indx = 0
        self.items = items

    def has_next(self):
        return False if self.indx >= len(self.items) else True

    def next(self):
        item = self.items[self.indx]
        self.indx += 1
        return item

class Menu:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
    
    def remove(self):
        return self.items.pop()

    def iterator(self):
        return MenuIterator(self.items)

if __name__ == '__main__':
    i1 = FoodItem("Burger", 7)
    i2 = FoodItem("Pizza", 8)
    i3 = FoodItem("Coke", 5)

    menu = Menu()
    menu.add(i1)
    menu.add(i2)
    menu.add(i3)

    print("Displaying Menu:")
    iterator = menu.iterator()
    while iterator.has_next():
        item = iterator.next()
        print(item)