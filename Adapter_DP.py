from abc import abstractmethod

#The client - New interface
class Client:
    def __init__(self) -> None:
        self._adaptee = Adaptee()

    @abstractmethod
    def request(self):
        pass

#The existing interface
class Adaptee:  

    def specific_request(self):
        pass

#Adapter the interface of Adaptee to the Target(i.e. client) interface.
class Adapter(Client):    

    def request(self):
        self._adaptee.specific_request()

#The diver code
def main():
    adapter = Adapter()
    adapter.request()


if __name__ == "__main__":
    main()