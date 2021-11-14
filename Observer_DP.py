from abc import abstractmethod


class Subject:
    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def register(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def deregister(self, observer):
        observer._subject = None
        self._observers.remove(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)

    @property
    def subject_state(self):
        return self._subject_state

    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()


class Observer():
    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abstractmethod
    def update(self, arg):
        pass


class ConcreteObserver(Observer):
    def update(self, arg):
        self._observer_state = arg
        # ...


def main():
    subject = Subject()
    concrete_observer = ConcreteObserver()
    subject.register(concrete_observer)
    subject.subject_state = 123


if __name__ == "__main__":
    main()