from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, admin = False):
        self._admin = admin

    def is_admin(self):
        return self._admin


# Document --------------------------------------------------------------------------------------------------------------

class Document(ABC):

    _state = None

    def __init__(self, state, user: User, status = True, moderator = False, is_approved = False):
        self._state = state
        self._state.document = self
        self.is_approved = is_approved
        self._moderator = User(moderator)
        self._user = user
        self.expired = not status
        self.render()

    def is_admin(self):
        return self._user.is_admin()

    def is_expired(self):
        return self.expired

    def render(self):
        self._state.render()

    def publish(self):
        self._state.publish()

    def change_to_state(self, state):
        self._state = state
        self._state.document = self
        self.publish()


# State --------------------------------------------------------------------------------------------------------------

class State(ABC):

    @property
    def document(self) -> Document:
        return self._context

    @document.setter
    def document(self, context: Document):
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
        if self.document.is_expired():
            print("Documento no rascunho e já expirado.")
        elif self.document.is_admin():
            print("Documento diretamente publicado por administrador")
            self.document.change_to_state(Published()) 
        else:
            self.document.change_to_state(Moderation()) 

    def publish(self):
        if self.document.is_expired():
            print("Documento no rascunho e já expirado.")
        elif self.document.is_admin():
            print("Documento diretamente publicado por administrador.")
            self.document.change_to_state(Published()) 
        else:
            print("Documento não pode ser publicado.")

class Moderation(State):

    def render(self):
        print("Documento não pode ser renderizado quando está em moderação.")

    def publish(self):
        if self.document.is_expired():
            print("Documento já expirado.")
            self.document.change_to_state(Draft())
        elif self.document._moderator.is_admin() and self.document.is_approved:
            print("Documento em moderação aprovado por administrador e publicado.")
            self.document.change_to_state(Published())
        elif self.document._moderator.is_admin():
            print("Documento em moderação não aprovado pelo administrador e arquivado.")
            self.document.change_to_state(Draft()) 
        else:
            print("Documento em moderação precisa ser analisado por administrador.")

class Published(State):

    def render(self):
        if self.document.is_expired():
            print("Publicação expirada.")
            self.document.change_to_state(Draft())
        else:
            print("Documento não pode ser renderizado quando já está publicado.")

    def publish(self):
        if self.document.is_expired():
            print("Publicação expirada.")
            self.document.change_to_state(Draft())

# Main --------------------------------------------------------------------------------------------------------------

def main():

    print("Rascunho publicado por admin:")
    Document(Draft(), User(True))

    print("\nRascunho publicado por usuário e aprovado por admin:")
    Document(Draft(), User(), True, True, True)

    print("\nRascunho publicado por usuário e não aprovado por admin:")
    Document(Draft(), User(), True, True, False)

    print("\nPublicação expirada:")
    Document(Published(), User(), False)

if __name__ == "__main__":
    main()