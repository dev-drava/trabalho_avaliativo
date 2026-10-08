from pessoa import Pessoa

turnos_validos = ("manhã", "tarde", "noite")


class Funcionario(Pessoa):
    "continua abstrata: mostrar_informacoes é implementado nas subclasses."

    def __init__(self, nome, idade, salario, id_func=None):
        super().__init__(nome, idade)
        self._salario = salario
        self._id_func = id_func

    @property
    def salario(self):
        return self._salario

    @property
    def id_func(self):
        return self._id_func

    def calcular_bonus(self):
        return self._salario * 0.05


class Gerente(Funcionario):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, salario)

    def calcular_bonus(self):
        return self._salario * 0.10

    def mostrar_informacoes(self):
        print(f"Gerente: {self.nome}, {self.idade} anos - "
              f"Salário: {self.salario:.2f} + bonus {self.calcular_bonus():.2f}€")

    def gerar_relatorio(self, funcionarios):
        print("--- Relatorio de funcionarios ---")
        for funcionario in funcionarios:
            funcionario.mostrar_informacoes()


class Recepcionista(Funcionario):
    def __init__(self, nome, id_func, idade, salario, turno):
        #chamada direta (nao super) para funcionar na heranca multipla
        Funcionario.__init__(self, nome, idade, salario, id_func)
        self._turno = None
        self.turno = turno #passa no setter

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, novo_turno):
        if novo_turno in turnos_validos:
            self._turno = novo_turno
        else:
            print(f"turno invalido: {novo_turno}. use manhã, tarde ou noite.")

    def mostrar_informacoes(self):
        print(f"recepcionista: {self.nome}, {self.idade} anos - "
              f"salário: {self.salario:.2f}€ - turno: {self.turno}")

    def registrar_hospede(self, hospede, lista_hospedes):
        lista_hospedes.append(hospede)

    def listar_hospedes(self, lista_hospedes):
        print("Hóspedes registados")
        for hospede in lista_hospedes:
            hospede.mostrar_informacoes()


class TecnicoManutencao(Funcionario):
    def __init__(self, nome, idade, salario, especialidade):
        #chamada direta (nao super) para funcionar na herança multipla
        Funcionario.__init__(self, nome, idade, salario)
        self._especialidade = especialidade
        self._reparos = []

    @property
    def especialidade(self):
        return self._especialidade

    def registrar_reparo(self, descricao):
        self._reparos.append(descricao)
        print(f"Reparo registado por {self.nome}: {descricao}")

    def mostrar_informacoes(self):
        print(f"Técnico de manutenção: {self.nome}, {self.idade} anos - "
              f"Salário: {self.salario:.2f}€ - Especialidade: {self.especialidade}")


class TecnicoRecepcao(Recepcionista, TecnicoManutencao):
    "Herança múltipla: recebe hóspedes e regista reparos."

    def __init__(self, nome, id_fun, salario, setor, especialidade,
                 idade=0, turno="manhã"):
        TecnicoManutencao.__init__(self, nome, idade, salario, especialidade)
        Recepcionista.__init__(self, nome, id_fun, idade, salario, turno)
        self._setor = setor
        self._hospedes_registados = []

    def registrar_hospede(self, nome_hospede):
        self._hospedes_registados.append(nome_hospede)
        print(f"hospede registado por {self.nome}: {nome_hospede}")

    def mostrar_info(self):
        print(f"tecnico de receção: {self.nome} (id {self.id_func}) - "
              f"setor: {self._setor}  turno: {self.turno} - "
              f"especialidade: {self.especialidade} - salário: {self.salario:.2f}€")

    def mostrar_informacoes(self):
        self.mostrar_info()
