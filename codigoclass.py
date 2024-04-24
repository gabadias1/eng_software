#Liskov, A classe 'personagem' permite tratarmos todos os persoganens de forma generica,
#sendo que todos tem nome, classe, um tipo de atckespecial e suas caracteristicas.

class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe

    def Nomeper(self):
        return "Meu nome é " + self.nome

    def Infoclasse(self):
        return "Sou da classe " + self.classe

    def atk_especial(self):
        return "Meu ataque especial é " + self.atk_especial()
    
    def caracteriscias(self):
        return "Minhas Caracteristicas são " + self.caracteriscias()


###OPEN/CLOSE. É possivel implementar qualquer outri tipo de personagems/classe, sem fazer alterações que mudariam o codigo.
###EXEMPLO:  class Ladrão(Personagem):
###             def atk_especial(self):
###                  return "Velocidade Aumentada"
###              def caracteriscias(self):
###                  return "Força:80\nMana:65\nVida:120"


class Mago(Personagem):
    def atk_especial(self):
        return "Ataque Especial : Bola de fogo"

    def caracteriscias(self):
        return "Força:50\nMana:200\nVida:100"

class Guerreiro(Personagem):
    def atk_especial(self):
        return "Ataque Especial : Espada Flamejante"
    
    def caracteriscias(self):
        return "Força:200\nMana:53\nVida:150"

class Clerigo(Personagem):
    def atk_especial(self):
        return "Ataque Especial : Cura divina"

    def caracteriscias(self):
        return "Força:35\nMana:180\nVida:90"

class Arqueiro(Personagem):
    def atk_especial(self):
        return "Ataque Especial : Flecha envenenada"

    def caracteriscias(self):
        return "Força:135\nMana:100\nVida:120"     


opcao = input("Escolha um personagem (Mago, Guerreiro, Clerigo ou Arqueiro): ")

#####Responsabilidade Unica: A classe "escolha"" está encarregada de uma unico operação,
#####fazer o jogador escolher um dos personagens disponiveis para ele começar o jogo.

class Escolha:
    def escolher_personagem():

        if opcao == "mago":
            return Mago("Merlin", "mago")
        elif opcao == "guerreiro":
            return Guerreiro("Arthur", "guerreiro")
        elif opcao == "clerigo":
            return Clerigo("Nicolau", "clerigo")
        elif opcao == "arqueiro":
            return Arqueiro("Link", "arqueiro")
        else:
            print("Opção inválida")
            return Escolha.escolher_personagem()


### Princípio da Inversão de Dependência, pois a classe não está vinculada a 
### implementações concretas de itens especiais, permitindo uma maior flexibilidade e extensibilidade do código.
  
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
print(personagem.Infoclasse())
print(personagem.atk_especial())
print(personagem.caracteriscias())

item_especial = Escolha.escolher_item_especial()
if item_especial:
    print("Item especial escolhido:", item_especial)