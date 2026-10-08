from pessoa import Pessoa
from quartos import QuartoSimples, QuartoLuxo
from hospede import Hospede
from funcionarios import Gerente, Recepcionista, TecnicoManutencao, TecnicoRecepcao


def main():
   
    try:
        Pessoa("Teste", 20)
    except TypeError:
        print("pessoa é abstrata e não pode ser instanciada.")

    #quartos
    quartos = [
        QuartoSimples(67, 50.0),
        QuartoSimples(42, 50.0),
        QuartoLuxo(167, 120.0, ["spa", "pequeno-almoço"]),
        QuartoLuxo(342, 172.0, ["spa", "jacuzzi", "minibar"]),
    ]
    quartos_por_numero = {q.numero: q for q in quartos}

    print("Quartos")
    for quarto in quartos:  #polimorfismo
        quarto.mostrar_informacoes()

    #funcionarios
    gerente = Gerente("Ana", 45, 2500)
    recepcionista = Recepcionista("David", 1, 30, 1200, "manhã")
    tecnico = TecnicoManutencao("Edson", 38, 1400, "eletricidade")
    tecnico_rececao = TecnicoRecepcao("Hery", 2, 1500, "Receção", "canalização")
    funcionarios = [gerente, recepcionista, tecnico, tecnico_rececao]
    print()
    +
    gerente.gerar_relatorio(funcionarios)

    #hospedes
    lista_hospedes = []
    hospedes = [
        Hospede("Drava Jones", 28, 3),
        Hospede("Henry", 35, 5),
        Hospede("Sengadas", 50, 2),
    ]
    for hospede in hospedes:
        recepcionista.registrar_hospede(hospede, lista_hospedes)

    hospedes[0].atribuir_quarto(quartos_por_numero[67])
    hospedes[1].atribuir_quarto(quartos_por_numero[42])
    hospedes[2].atribuir_quarto(quartos_por_numero[101])  #ocupado
    print()
    
    recepcionista.listar_hospedes(lista_hospedes)
    print()
    recepcionista.turno = "madrugada"  #invalido
    tecnico_rececao.registrar_hospede("sofia")
    tecnico_rececao.registrar_reparo("torneira a pingar no quarto 102")
    print("\nContas e checkout")

    for hospede in lista_hospedes:
        print(f"conta de {hospede.nome}: {hospede.calcular_conta():.2f}€")
        hospede.checkout()

    print()
    for quarto in quartos:
        quarto.mostrar_informacoes()


if __name__ == "__main__":
    main()
