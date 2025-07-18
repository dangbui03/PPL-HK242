# Principles of Programming Languages (PPL-HK242)
This repository contains assignments for the Principles of Programming Languages course, which focuses on compiler construction techniques for a simplified Go-like language called MiniGo.

## Overview

The course assignments walk through the complete process of building a compiler, divided into four main assignments:

1. **Assignment 1**: Lexical Analysis and Syntax Analysis
   - Implementation of a lexer and parser for MiniGo using ANTLR
   - Understanding tokenization and parsing techniques

2. **Assignment 2**: Abstract Syntax Tree (AST) Generation
   - Building an AST representation of MiniGo programs
   - Transforming parse trees into abstract syntax trees

3. **Assignment 3**: Static Checking
   - Type checking and semantic analysis
   - Symbol table management
   - Scope handling and type inference

4. **Assignment 4**: Code Generation
   - Generating JVM bytecode from AST
   - Using Jasmin to assemble bytecode into Java class files
   - Creating runtime libraries for program execution

## MiniGo Language

MiniGo is a simplified version of the Go programming language with features including:
- Variable and constant declarations
- Basic data types (int, float, string, boolean, arrays)
- Functions and procedures
- Control structures (if, for)
- Interface declarations
- Expressions and statements

## Project Structure

```
.
├── Ass1/          # Assignment 1: Lexical and Syntax Analysis
├── Ass2/          # Assignment 2: AST Generation
├── Ass3/          # Assignment 3: Static Checking  
├── ASS4/          # Assignment 4: Code Generation
├── MiniGo Spec.pdf  # Language specification
└── README.md
```

## Running the Code

Each assignment has its own run script and test suites:

```bash
# Run lexer tests
python run.py test LexerSuite [test_case]

# Run parser tests
python run.py test ParserSuite [test_case]

# Run AST generation tests
python run.py test ASTGenSuite [test_case]

# Run static checker tests
python run.py test CheckSuite [test_case]

# Run code generation tests
python run.py test CodeGenSuite [test_case]
```

## Code Generation

The final assignment generates Jasmin bytecode that can be assembled into Java class files. To run the generated code:

1. Generate the Jasmin file:
   ```
   python run.py test CodeGenSuite test_case
   ```

2. Assemble the Jasmin file:
   ```
   java -jar jasmin.jar MiniGoClass.j
   ```

3. Run the resulting Java class:
   ```
   java -cp _io:. MiniGoClass
   ```

## Development Tools

- ANTLR 4.9.2: For lexer and parser generation
- Python: Main implementation language
- Jasmin: For assembling Java bytecode

## Documentation

For more details about the MiniGo language, refer to the MiniGo Spec document included in the repository.

The code includes extensive comments following the structure outlined by the course instructors.