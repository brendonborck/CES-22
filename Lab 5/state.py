from abc import ABC

class User(ABC):

    def __init__(self, user = "usuário"):
        self.user = user


# Document --------------------------------------------------------------------------------------------------------------

class Document(ABC):

    def __init__(self, state: State, user: User ,status = True):
        self._state = state
        self._user = user
        self.expired = not status
        if self.expired == True:
            print("Documento arquivado.")

    def render(self):
        self._state.render()

    def publish(self):
        self._state.publish()

    def changeState(self, state: State):
        if self._user == "admin":
            print("Documento publicado por administrador.")
        else:




# State --------------------------------------------------------------------------------------------------------------

class State(ABC):

    def __init__(self, context: Document):
        self._context = context

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def publish(self):
        pass


# Concrete states --------------------------------------------------------------------------------------------------------------

class Draft(State):

    def render(self):
        print("Documento enviado para moderação.")

    def publish(self):
        print("Documento aprovado e publicado.")

class Moderation(State):

    def render(self):
        print("Documento enviado para moderação.")

    def publish(self):
        print("Documento aprovado e publicado.")

class Published(State):

    def render(self):
        print("Documento enviado para moderação.")

    def publish(self):
        print("Documento aprovado e publicado.")

# Main --------------------------------------------------------------------------------------------------------------

def main():

    print("Documento publicado por admin:")
    Document(1)

    print("Documento publicado por usuário e não aprovado por admin:")
    Document(2)

    print("Documento publicado por usuário e não aprovado:")
    Document(3)

    print("Documento expirado:")
    Document(3)

if __name__ == "__main__":
    main()