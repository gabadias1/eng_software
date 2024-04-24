# Principios Solid
Projeto de codigo focado em principios SOLID, feito para Materia Engenharia de Software da UTFPR-CM.

O código é uma simulação de um jogo de RPG onde os jogadores podem escolher entre quatro classes de personagens: `Mago`, `Guerreiro`, `Clérigo` e `Arqueiro`. Cada classe possui características específicas, como ataques especiais e atributos de força, mana e vida.

Linguagem usada = `PYTHON`.

### Principios SOLID abordados: 

`Princípio da Substituição de Liskov (LSP)`: Esse princípio, proposto por Barbara Liskov, afirma que objetos de uma classe base devem poder ser substituídos por objetos de suas classes derivadas sem afetar a corretude do programa. Em outras palavras, se S é um subtipo de T, então os objetos do tipo T podem ser substituídos por objetos do tipo S sem alterar as propriedades do programa.

`Princípio Aberto/Fechado (OCP)`: Esse princípio, de Bertrand Meyer, diz que as entidades de software (classes, módulos, funções, etc.) devem estar abertas para extensão, mas fechadas para modificação. Isso significa que você pode estender o comportamento de uma classe sem precisar alterar seu código-fonte original, usando, por exemplo, herança, interfaces ou composição.

`Princípio da Dependência (DIP)`: Este princípio sugere que módulos de alto nível não devem depender de módulos de baixo nível. Em vez disso, ambos devem depender de abstrações. Além disso, abstrações não devem depender de detalhes, mas sim, detalhes devem depender de abstrações. Isso promove a separação de preocupações e torna o código mais flexível e fácil de manter.

`Princípio da Responsabilidade Única (SRP)`: Este princípio, proposto por Robert C. Martin, afirma que uma classe deve ter apenas uma razão para mudar. Em outras palavras, uma classe deve ter uma única responsabilidade ou tarefa. Isso ajuda a manter o código coeso, facilitando sua compreensão, manutenção e reutilização.

### Responsabilidade Única (SRP)

A classe `Personagem` é responsável por representar as características individuais de um personagem, enquanto a classe `Escolha` gerencia a seleção de personagens e itens especiais. Deixando as operações e `classes` com apenas uma responsabilidade. Isso promove a coesão e facilita a manutenção do código.

### Aberto/Fechado (OCP)

O sistema é aberto para extensão, mas fechado para modificação. Novos tipos de personagens podem ser adicionados facilmente, criando subclasses de `Personagem`, sem a necessidade de alterar o código existente.

### Liskov Substitution Principle (LSP)

A classe `Personagem` faz com que tratemos todos os personagens do codigo de forma generica. Sendo que todos eles possuem `nome`, `classe`, `atk_especial` e suas `caracteristicas`

### Princípio da Inversão de Dependência (DIP)

Seguindo o princípio da inversão de dependência, a classes de alto nível, como `Escolha`, dependem de abstrações em vez de implementações concretas. Por exemplo, `Escolha` depende da classe abstrata `Personagem` e de suas subclasses para criar instâncias de personagens, em vez de depender diretamente das implementações específicas.
