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

Cada classe no sistema possui uma única responsabilidade bem definida. Por exemplo, a classe `Personagem` é responsável por representar as características individuais de um personagem, enquanto a classe `Escolha` gerencia a seleção de personagens e itens especiais. Isso promove a coesão e facilita a manutenção do código.

### Aberto/Fechado (OCP)

O sistema é aberto para extensão, mas fechado para modificação. Novos tipos de personagens podem ser adicionados facilmente, criando subclasses de `Personagem`, sem a necessidade de alterar o código existente. Isso promove a extensibilidade do sistema e evita impactos indesejados em partes já funcionais do código.

### Liskov Substitution Principle (LSP)

Embora não haja uma violação clara, o princípio de substituição de Liskov pode ser mais plenamente alcançado. Atualmente, a classe `Personagem` possui métodos condicionais que verificam o tipo de personagem para retornar informações específicas. Isso pode limitar a substituição livre por subtipos sem alterar o comportamento esperado. Uma abordagem mais adequada pode ser fornecer uma interface mais genérica para todas as subclasses de personagens.

### Princípio da Inversão de Dependência (DIP)

O código segue o princípio da inversão de dependência, pois as classes de alto nível, como `Escolha`, dependem de abstrações em vez de implementações concretas. Por exemplo, `Escolha` depende da classe abstrata `Personagem` e de suas subclasses para criar instâncias de personagens, em vez de depender diretamente das implementações específicas.
