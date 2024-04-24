#Liskov Substitution Principle : A classe Personagem possui métodos condicionais que verificam o tipo de personagem para retornar informações.
#Isso viola Liskov, pois os métodos não podem ser substituídos livremente por subtipos.

#Responsabilidade Única : A classe Personagem tem múltiplas responsabilidades, pois ela é responsável por retornar
#informações específicas de cada tipo de personagem. Isso viola a Responsabilidade unica, pois a classe tem mais de uma razão para mudar.

class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe

    def Nomeper(self):
        if self.classe == "mago":
            return "Meu nome é " + self.nome
        elif self.classe == "guerreiro":
            return "Sou da classe " + self.classe
        elif self.classe == "clerigo":
            return "Meu ataque especial é " + self.atk_especial()
        elif self.classe == "arqueiro":
            return "Minhas Caracteristicas são " + self.caracteriscias()

#Open/Closed Principle:Para adicionar um novo tipo de personagem, 
#seria necessário modificar a classe Personagem, o que viola o Open/Close.

    def atk_especial(self):
        if self.classe == "mago":
            return "Ataque Especial: Bola de fogo"
        elif self.classe == "guerreiro":
            return "Ataque Especial: Espadas duplas"
        elif self.classe == "clerigo":
            return "Ataque Especial: Cura divina"
        elif self.classe == "arqueiro":
            return "Ataque Especial: Flecha envenenada"

    def caracteriscias(self):
        if self.classe == "mago":
            return "Força:50\nMana:200\nVida:100"
        elif self.classe == "guerreiro":
            return "Força:200\nMana:53\nVida:150"
        elif self.classe == "clerigo":
            return "Força:35\nMana:180\nVida:90"
        elif self.classe == "arqueiro":
            return "Força:135\nMana:100\nVida:120"


#Princípio da Inversão de Dependência: A classe "Escolha" depende diretamente da classe Personagem para criar 
#pedidos de personagens.Isso viola a Dependencia, pois a classe "Escolha" depende de uma implementação concreta.

class Escolha:
    def escolher_personagem():
        opcao = input("Escolha um personagem (Mago, Guerreiro, Clerigo ou Arqueiro): ")

        if opcao == "mago":
            return Personagem("Merlin", "mago")
        elif opcao == "guerreiro":
            return Personagem("Arthur", "guerreiro")
        elif opcao == "clerigo":
            return Personagem("Nicolau", "clerigo")
        elif opcao == "arqueiro":
            return Personagem("Link", "arqueiro")
        else:
            print("Opção inválida")
            return Escolha.escolher_personagem()

    def escolher_item_especial():
        opcao = input("Escolha um item especial (Espada de Diamante, Pedra Filosofal, Colar Abençoado ou Arco das Trevas): ")

        itens_especiais = {
            "espada de diamante": "Espada de Diamante",
            "pedra filosofal": "Pedra Filosofal",
            "colar abençoado": "Colar Abençoado",
            "arco das trevas": "Arco das Trevas"
        }

        if opcao.lower() in itens_especiais:
            return itens_especiais[opcao.lower()]
        else:
            print("Item especial inválido.")
            return Escolha.escolher_item_especial()


personagem = Escolha.escolher_personagem()
print(personagem.Nomeper())
print(personagem.Specialatk())
print(personagem.caracteriscias())

item_especial = Escolha.escolher_item_especial()
if item_especial:
    print("Item especial escolhido:", item_especial)
