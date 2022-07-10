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
        pass