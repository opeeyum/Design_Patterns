from abc import abstractmethod


class Context:
    _state = None
    """ A reference to the current state."""

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        """Method to make transition"""

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self
    
    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State:
    """An abstract class for Concrete sub-classes"""

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context: Context):
        self._context = context

    @abstractmethod
    def handle1(self):
        pass

    @abstractmethod
    def handle2(self):
        pass


class State_A(State):
    def handle1(self):
        print("State_A handles request1.")
        print("State_A wants to change the state of the context.")
        self.context.transition_to(State_B())

    def handle2(self):
        print("State_A handles request2.")


class State_B(State):
    def handle1(self):
        print("State_B handles request1.")

    def handle2(self):
        print("State_B handles request2.")
        print("State_B wants to change the state of the context.")
        self.context.transition_to(State_A())


if __name__ == "__main__":
    # The Driver code.

    context = Context(State_A())
    context.request1()
    context.request2()




class EmotionalState():
    @abstractmethod
    def say_hello(self):
        pass

    @abstractmethod
    def say_goodbye(self):
        pass

class HappyState(EmotionalState):
    def say_goodbye(self):
        return "Bye, friend!"

    def say_hello(self):
        return "Hello, friend!"

class SadState(EmotionalState):
    def say_goodbye(self):
        return "Bye. Sniff, sniff."

    def say_hello(self):
        return "Hello. Sniff, sniff."

class Person(EmotionalState):
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def say_goodbye(self):
        return self.state.say_goodbye()

    def say_hello(self):
        return self.state.say_hello()

if __name__ == '__main__':
    person = Person(HappyState())
    print("Hello in happy state: " + person.say_hello())
    print("Goodbye in happy state: " + person.say_goodbye())

    person.set_state(SadState())
    print("Hello in sad state: " + person.say_hello())
    print("Goodbye in sad state: " + person.say_goodbye())