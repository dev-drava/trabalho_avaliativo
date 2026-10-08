from abc import ABC, abstractmethod


class Pessoa(ABC):
    "Classe abstrata: base de Hospede."

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = 0
        self.idade = idade        #passa no setter (nao negativo)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade

    @abstractmethod
    def mostrar_informacoes(self):
        """Sobrescrito pelas subclasses."""
        pass
