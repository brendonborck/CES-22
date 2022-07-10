from abc import ABC
from tkinter import *
from tkinter import ttk

class Command(ABC):
    def __init__(self, command):
        self.command = command

    def execute(self, command):
        self.command = command

# Invoker --------------------------------------------------------------------------------------------------------------

class Invoker(ABC):
    def __init__(self, command: Command):
        self.command = command

    def set_command(self, command):
        self.command = command

    def execute_comand(self):
        self.command.execute()

# Commands --------------------------------------------------------------------------------------------------------------

class VerificarSaldo(Command):
    def __init__(self, command):
        self.command = command

    def execute(self, command):
        self.command = command


class VerificarExtrato(Command):
    def __init__(self, command):
        self.command = command

    def execute(self, command):
        self.command = command


class RealizarTransferencia(Command):
    def __init__(self, command):
        self.command = command

    def execute(self, command):
        self.command = command

# Receiver --------------------------------------------------------------------------------------------------------------

class Receiver(ABC):

    def operations(self, a):
        a = a + 1

# Application --------------------------------------------------------------------------------------------------------------

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