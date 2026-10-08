from abc import ABC, abstractmethod


class Quarto(ABC):
    """Classe abstrata de quartos."""

    def __init__(self, numero, tipo, preco_diaria):
        self._numero = numero
        self._tipo = tipo
        self._ocupado = False
        self._preco_diaria = 0
        self.preco_diaria = preco_diaria  #passa no setter

    @property
    def numero(self):
        return self._numero

    @property
    def tipo(self):
        return self._tipo

    @property
    def ocupado(self):
        return self._ocupado

    @property
    def preco_diaria(self):
        return self._preco_diaria

    @preco_diaria.setter
    def preco_diaria(self, novo_preco):
        if novo_preco >= 0:
            self._preco_diaria = novo_preco

    def ocupar(self):
        self._ocupado = True

    def liberar(self):
        self._ocupado = False

    @abstractmethod
    def descricao(self):
        "Cada tipo de quarto descreve-se à sua maneira."
        pass

    def mostrar_informacoes(self):
        estado = "ocupado" if self._ocupado else "livre"
        print(f"Quarto {self._numero} ({self._tipo}) - "
              f"{self._preco_diaria:.2f}€ por diária - {estado}")


class QuartoSimples(Quarto):
    def __init__(self, numero, preco_diaria):
        super().__init__(numero, "simples", preco_diaria)

    def descricao(self):
        return "Quarto simples"


class QuartoLuxo(Quarto):
    def __init__(self, numero, preco_diaria, servicos=None):
        super().__init__(numero, "luxo", preco_diaria)
        self._servicos = servicos if servicos is not None else []

    def descricao(self):
        return "Quarto de luxo com serviços incluídos"

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        for servico in self._servicos:
            print(f"   - {servico}")
