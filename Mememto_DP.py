"""class Memento:
    def __init__(self, value):
        self.state = value
    
    def SetState(self, value):
        self.state = value

    def GetState(self):
        return self.state

class Originator:
    def SetState(self, value):
        self.state = value
    
    def GetState(self):
        return self.state
    
    def CreateMemento(self):
        return Memento(self.state)
    
    def SetMemento(self, memento):
        print("Going to previous state.")
        self.state = memento.GetState()

class Caretaker:
    def __init__(self, originatorObj):
        self.memento = None
        self.origin = originatorObj
    
    def Execute(self):
        self.memento = self.origin.CreateMemento()
        self.origin.SetState(0)

    def Unexecute(self):
        self.origin.SetMemento(self.memento)

if __name__ == "__main__":
    originator = Originator()
    originator.SetState(1)

    print("The state value is: ", originator.GetState())

    caretaker = Caretaker(originator)
    caretaker.Execute()
    print("The state value is: ", originator.GetState())

    caretaker.Unexecute()
    print("The state value is: ", originator.GetState())"""

class Memento(object):
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state

class Originator(object):
    _state = ""

    def set(self, state):
        self._state = state
        print("Originator: Setting state to", self._state)

    def save_to_memento(self):
        print("Originator: Saving to Memento.")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_saved_state()
        print("Originator: State after restoring from Memento:", self._state)

saved_states = []
originator = Originator()
originator.set("State-1")
originator.set("State-2")
saved_states.append(originator.save_to_memento())

originator.set("State-3")
saved_states.append(originator.save_to_memento())

originator.set("State-4")

originator.restore_from_memento(saved_states[0])