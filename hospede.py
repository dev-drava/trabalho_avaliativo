from pessoa import Pessoa


class Hospede(Pessoa):
    def __init__(self, nome, idade, dias_estadia, quarto=None):
        super().__init__(nome, idade)
        self._dias_estadia = dias_estadia
        self._quarto = None
        if quarto is not None:
            self.quarto = quarto

    @property
    def quarto(self):
        return self._quarto

    @quarto.setter
    def quarto(self, novo_quarto):
        #so define o quarto se ele estiver livre
        if novo_quarto is not None and not novo_quarto.ocupado:
            if self._quarto is not None:
                self._quarto.liberar()
            novo_quarto.ocupar()
            self._quarto = novo_quarto
        else:
            print(f"Quarto indisponível para {self.nome}.")

    def atribuir_quarto(self, quarto):
        self.quarto = quarto

    def calcular_conta(self):
        if self._quarto is None:
            return 0
        #dias de estadia * preço da diária 
        return self._dias_estadia * self._quarto.preco_diaria

    def mostrar_informacoes(self):
        numero = self._quarto.numero if self._quarto is not None else "sem quarto"
        print(f"Hóspede: {self.nome}, {self.idade} anos - Quarto: {numero}")

    def checkout(self):
        if self._quarto is not None:
            self._quarto.liberar()
            self._quarto = None
        print(f"{self.nome} fez o checkout. Obrigado pela estadia!")
