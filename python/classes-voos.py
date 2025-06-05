class Voos:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.passageiros = []

    def adicionar_passageiro(self, nome=None):
        if len(self.passageiros) >= self.capacidade:
            print("Voo lotado. Não é possível adicionar mais passageiros.")
        else:
            if nome is None:
                nome = input("Digite o nome do passageiro: ")
            self.passageiros.append(nome)
            print(f"Passageiro {nome} adicionado com sucesso!")

    def remover_passageiro(self, nome=None):
        if nome is None:
            nome = input("Digite o nome do passageiro a remover: ")
        if nome in self.passageiros:
            self.passageiros.remove(nome)
            print(f"Passageiro {nome} removido.")
        else:
            print(f"Passageiro {nome} não encontrado.")

    def listar_passageiros(self):
        if not self.passageiros:
            print("Nenhum passageiro registrado.")
        else:
            print("\nLista de Passageiros:")
            for passageiro in self.passageiros:
                print(f"- {passageiro}")

    def menu(self):
        while True:
            print("\n===== MENU DO VOO =====")
            print("1 - Adicionar passageiro")
            print("2 - Remover passageiro")
            print("3 - Listar passageiros")
            print("4 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar_passageiro()
            elif opcao == "2":
                self.remover_passageiro()
            elif opcao == "3":
                self.listar_passageiros()
            elif opcao == "4":
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    print("Bem-vindo ao sistema de gerenciamento de voos!")
    
    while True:
        try:
            capacidade = int(input("Defina a capacidade do voo: "))
            if capacidade <= 0:
                print("A capacidade deve ser maior que zero.")
            else:
                break
        except ValueError:
            print("Digite apenas números inteiros!")

    voo = Voos(capacidade)
    print(f"\nVoo criado com capacidade para {capacidade} passageiros.")
    voo.menu()