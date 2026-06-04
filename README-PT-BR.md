# Exper

Exper é uma linguagem de programação interpretada escrita em Python.

O projeto nasceu com um objetivo simples: aprender mais sobre interpretadores, design de linguagens e execução de código. Com o tempo, ele evoluiu para uma linguagem capaz de executar programas completos, incluindo jogos de texto.

## Recursos atuais

* Variáveis
* Funções
* Estruturas (Structs)
* Condicionais (`if`, `elif`, `else`)
* Loops (`while`, `for`)
* Listas
* Escopos
* Interpolação de strings
* Objetos baseados em Structs
* Operações matemáticas
* Funções nativas
* Sistema de inventário e RPG para testes

## Exemplo

```exper
struct Player {
    name,
    hp = 100
}

player = Player()
player.name = "Callebe"

console.log("{player.name} possui {player.hp} HP")
```

Saída:

```text
Callebe possui 100 HP
```

## Filosofia

A Exper não pretende competir com linguagens estabelecidas.

O objetivo principal é servir como laboratório para estudar:

* Interpretadores
* Compiladores
* Parsing
* Escopos
* Sistemas de tipos
* Estruturas de dados
* Design de linguagens

## Projeto atual

Atualmente a linguagem está sendo validada através da criação de um RPG de texto.

O RPG testa diversos recursos importantes:

* Structs
* Inventário
* Combate
* Passagem por referência
* Manipulação de listas
* Escopos
* Funções
* Loops
* Interpolação de strings

Cada novo recurso da linguagem é testado diretamente dentro do jogo.

## Status

A linguagem está em desenvolvimento ativo.

Muitos recursos ainda estão sendo implementados e refinados.

## Roadmap

### Concluído

* [x] Variáveis
* [x] Funções
* [x] Structs
* [x] Loops
* [x] Condicionais
* [x] Listas
* [x] Interpolação de strings

### Em desenvolvimento

* [ ] Métodos em objetos
* [ ] Operadores compostos
* [ ] Melhor suporte a coleções
* [ ] Módulos
* [ ] Classes
* [ ] Sistema de exceções

## Motivação

Criar uma linguagem é uma excelente forma de aprender como linguagens modernas funcionam internamente.

A Exper é resultado dessa jornada de aprendizado.
