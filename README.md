# Principios Solid
Projeto de codigo focado em principios SOLID, feito para Materia Engenharia de Software da UTFPR-CM.

O código é uma simulação de um jogo de RPG onde os jogadores podem escolher entre quatro classes de personagens: `Mago`, `Guerreiro`, `Clérigo` e `Arqueiro`. Cada classe possui características específicas, como ataques especiais e atributos de força, mana e vida.

Linguagem usada = `PYTHON`.

### Principios SOLID abordados: 

`Princípio da Substituição de Liskov (LSP)`: O Princípio de Substituição de Liskov, nomeado em homenagem a Barbara Liskov, define regras para redefinir métodos em subclasses, garantindo consistência no código.

`Princípio Aberto/Fechado (OCP)`: O Princípio Aberto/Fechado tem como objetivo a construção de classes flexíveis e extensíveis, capazes de se adaptarem a diversos cenários de uso, sem modificações no seu código fonte.

`Princípio da Dependência (DIP)`: O Princípio da Dependência sugere que as classes clientes devem depender de abstrações, como interfaces, em vez de implementações concretas. Isso permite maior flexibilidade e resistência a mudanças, pois as implementações podem ser trocadas sem afetar os clientes. 

`Princípio da Responsabilidade Única (SRP)`: O Princípio da Responsabilidade Única preconiza que cada classe deve ter uma única razão para mudar, promovendo coesão. Ele sugere a separação entre apresentação e regras de negócio para facilitar a manutenção e evolução do sistema. 

## SOLID no Codigo


### Responsabilidade Única (SRP)

A classe `Personagem` é responsável por representar as características individuais de um personagem, enquanto a classe `Escolha` gerencia a seleção de personagens e itens especiais. Deixando as operações e `classes` com apenas uma responsabilidade. Isso promove a coesão e facilita a manutenção do código.

### Aberto/Fechado (OCP)

O sistema é aberto para extensão, mas fechado para modificação. Novos tipos de personagens podem ser adicionados facilmente, criando subclasses de `Personagem`, sem a necessidade de alterar o código existente.

### Liskov Substitution Principle (LSP)

A classe `Personagem` faz com que tratemos todos os personagens do codigo de forma generica. Sendo que todos eles possuem `nome`, `classe`, `atk_especial` e suas `caracteristicas`.

### Princípio da Inversão de Dependência (DIP)

Seguindo o princípio da inversão de dependência, a classes de alto nível, como `Escolha`, dependem de abstrações em vez de implementações concretas. Por exemplo, `Escolha` depende da classe abstrata `Personagem` e de suas subclasses para criar instâncias de personagens, em vez de depender diretamente das implementações específicas.
