from abc import abstractmethod


"""The user class"""
class User():
    def __init__(self, med, name):
        self.mediator = med
        self.name = name

    @abstractmethod
    def send(self, msg):
        pass

    @abstractmethod
    def receive(self, msg):
        pass


"""The Mediator"""
class ChatMediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, msg, user):
        for u in self.users:
            if u != user:
                u.receive(msg)


"""Concrete implementation of user class"""
class ConcreteUser(User):
    def send(self, msg):
        print(self.name + ": Sending Message: " + msg)
        self.mediator.send_message(msg, self)

    def receive(self, msg):
        print(self.name + ": Received Message: " + msg)


"""The driver Code"""
if __name__ == '__main__':
    mediator = ChatMediator()
    user1 = ConcreteUser(mediator, "John")
    user2 = ConcreteUser(mediator, "Harry")
    user3 = ConcreteUser(mediator, "Jack")
    user4 = ConcreteUser(mediator, "Tom")
    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)
    mediator.add_user(user4)

    user1.send("Hello every one.")