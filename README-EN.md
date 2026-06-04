# Exper

Exper is an interpreted programming language written in Python.

The project started as a learning exercise focused on interpreters, language design, and code execution. Over time, it evolved into a language capable of running complete programs, including text-based RPG games.

## Current Features

* Variables
* Functions
* Structs
* Conditionals (`if`, `elif`, `else`)
* Loops (`while`, `for`)
* Lists
* Scopes
* String interpolation
* Struct-based objects
* Mathematical operations
* Built-in functions
* Inventory and RPG systems for testing

## Example

```exper
struct Player {
    name,
    hp = 100
}

player = Player()
player.name = "Callebe"

console.log("{player.name} has {player.hp} HP")
```

Output:

```text
Callebe has 100 HP
```

## Philosophy

Exper is not intended to compete with established programming languages.

Its primary goal is to serve as a playground for studying:

* Interpreters
* Compilers
* Parsing
* Scopes
* Type systems
* Data structures
* Language design

## Current Project

The language is currently being validated through the development of a text-based RPG.

The RPG tests several important language features:

* Structs
* Inventory systems
* Combat systems
* Reference passing
* List manipulation
* Scopes
* Functions
* Loops
* String interpolation

Every new language feature is tested directly within the game.

## Status

The language is under active development.

Many features are still being implemented and improved.

## Roadmap

### Completed

* [x] Variables
* [x] Functions
* [x] Structs
* [x] Loops
* [x] Conditionals
* [x] Lists
* [x] String interpolation

### In Progress

* [ ] Object methods
* [ ] Compound operators
* [ ] Better collection support
* [ ] Modules
* [ ] Classes
* [ ] Exception system

## Motivation

Building a programming language is one of the best ways to understand how modern languages work internally.

Exper is the result of that learning journey.

## Note

English is not my first language. Parts of this documentation were written and reviewed with the help of ChatGPT. Feedback and corrections are welcome.
