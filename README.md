

-----

# Minha Jornada de Aprendizado em Python (Guia para Iniciantes)

Olá\! Excelente escolha começar a estudar Python. É uma linguagem poderosa, versátil e ótima para iniciantes. Este documento é um resumo dos meus primeiros passos, servindo como um guia para quem também está começando.

## Índice
- [1. Configurando o Ambiente (macOS)](#1-configurando-o-ambiente-macos)
- [2. O Terminal é Seu Amigo: Comandos Essenciais](#2-o-terminal-é-seu-amigo-comandos-essenciais)
- [3. Integrando o Terminal com o VS Code](#3-integrando-o-terminal-com-o-vs-code)
- [4. Conceitos Fundamentais do Python](#4-conceitos-fundamentais-do-python)
    - [Tipagem: Forte e Dinâmica](#tipagem-forte-e-dinâmica)
    - [Constantes em Python: Uma Convenção](#constantes-em-python-uma-convenção)
    - [Variáveis e Operadores](#variáveis-e-operadores)
    - [Estruturas Condicionais e Laços](#estruturas-condicionais-e-laços)
    - [Funções e Entradas do Usuário](#funções-e-entradas-do-usuário)
- [5. Instalando Pacotes com pip](#5-instalando-pacotes-com-pip)
- [6. Tipos de Dados](#6-Tipos-de-Dados)
- [7. Tudo Sobre Strings](#7-Tudo-Sobre-Strings)
- [8. Conversão de Unidades de Tempo](#8-Conversão-de-Unidades-de-Tempo)

-----

### 1\. Configurando o Ambiente (macOS)

O primeiro passo é garantir que você tem o Python instalado e saber como encontrá-lo.

#### Verificando a Versão do Python

Abra o **Terminal** (Use o Spotlight: `⌘ + Espaço`, digite `Terminal` e pressione `Enter`).

Para desenvolvimento moderno, sempre use **Python 3**. Para verificar a versão, use o comando:

```bash
python3 --version
```

Você deverá ver algo como `Python 3.12.4`.

> **⚠️ Ponto de Atenção: `python` vs `python3`**
> O macOS vem com uma versão antiga, o Python 2, para compatibilidade. Se você digitar `python --version`, verá algo como `Python 2.7.18`. **Ignore esta versão\!** Sempre use os comandos `python3` e `pip3`.

#### E se o Python 3 não estiver instalado?

Se o comando `python3 --version` der erro, baixe e instale a versão mais recente diretamente do site oficial:
➡️ **[python.org/downloads/macos/](https://www.python.org/downloads/macos/)**

-----

### 2\. O Terminal é Seu Amigo: Comandos Essenciais

Interagir com pastas e arquivos pelo terminal é uma habilidade fundamental.

| Comando | Nome Completo | O que faz |
| :--- | :--- | :--- |
| `pwd` | Print Working Directory | Mostra em qual diretório você está. |
| `ls` | List | Lista o conteúdo do diretório atual. |
| `cd [pasta]` | Change Directory | **Entra** em um diretório. Ex: `cd Desktop`. |
| `cd ..` | Change Directory (Up) | **Sobe** um nível (vai para a pasta pai). |
| `cd ~` ou `cd`| Change Directory (Home)| Leva você de volta à sua pasta de usuário. |
| `mkdir [nome]`| Make Directory | Cria uma nova pasta. Ex: `mkdir meu_projeto`. |
| `open .` | Open Current Directory| **Abre o diretório atual** em uma janela do Finder. |

> **Dica de Mestre:** Use a tecla `Tab` para autocompletar nomes de arquivos e pastas. É um superpoder\!

-----

### 3\. Integrando o Terminal com o VS Code

Abrir seus projetos no editor de código Visual Studio Code diretamente do terminal acelera muito o trabalho.

O comando mágico é:

```bash
code .
```

Este comando abre o diretório atual (`.`) no VS Code.

#### Habilitando o comando `code` (passo único)

1.  Abra o VS Code.
2.  Abra a Paleta de Comandos com `⇧⌘P` (Shift + Command + P).
3.  Digite `shell command` e selecione a opção **`Shell Command: Install 'code' command in PATH`**.
4.  Reinicie o seu terminal.

Agora o comando `code .` estará disponível para sempre\!

-----

### 4\. Conceitos Fundamentais do Python

#### Tipagem: Forte e Dinâmica

Python tem um sistema de tipos que é:

  * **Forte:** Ele não permite operações entre tipos incompatíveis sem conversão explícita. Ele não "adivinha" o que você quer. `10 + "5"` causa um `TypeError`. Você precisa ser explícito: `10 + int("5")`.
  * **Dinâmica:** Você não precisa declarar o tipo de uma variável. Uma variável pode guardar um número e, depois, um texto. O tipo pertence ao valor, não à variável.

<!-- end list -->

```python
# Tipagem dinâmica em ação
minha_variavel = 100      # Agora é um inteiro
minha_variavel = "Python" # Agora é uma string
```

#### Constantes em Python: Uma Convenção

Python não tem constantes reais que não podem ser alteradas. Em vez disso, usamos uma **convenção**:

> Nomes de variáveis que não devem ser alterados são escritos em **LETRAS MAIÚSCULAS**.

```python
VELOCIDADE_DA_LUZ = 299792458
PI = 3.14159
```

É um "acordo de cavalheiros": você pode alterar, mas não deve.

#### Variáveis e Operadores

```python
# Tipos de dados básicos
nome = "Alice"      # String
idade = 30          # Inteiro
preco = 19.99       # Float (ponto flutuante)
ativo = True        # Booleano

# Operadores Aritméticos
soma = 10 + 5       # 15
subtracao = 10 - 5  # 5
multiplicacao = 10 * 5 # 50
divisao = 10 / 5    # 2.0
modulo = 10 % 3     # 1 (resto da divisão)
exponenciacao = 10 ** 2 # 100
```

#### Estruturas Condicionais e Laços

```python
# if / else
if idade >= 18:
    print(f"{nome} é maior de idade.")
else:
    print(f"{nome} é menor de idade.")

# Laço 'for'
for i in range(5):  # Itera de 0 a 4
    print(f"Número: {i}")
```

#### Funções e Entradas do Usuário

```python
# Definindo uma função
def saudar(nome_pessoa):
    return f"Olá, {nome_pessoa}!"

# Chamando a função
mensagem = saudar("Bob")
print(mensagem)  # Saída: Olá, Bob!

# Pegando dados do usuário
# A função input() sempre retorna uma string!
nome_usuario = input("Qual é o seu nome? ")
idade_usuario = int(input("Qual é a sua idade? ")) # Convertendo para inteiro
print(f"Bem-vindo, {nome_usuario} de {idade_usuario} anos!")
```

-----

### 5\. Instalando Pacotes com `pip`

`pip` é a "App Store" do Python. Ele permite instalar bibliotecas incríveis criadas pela comunidade.

O comando usa `pip3` para garantir a instalação no Python 3.

```bash
# Sintaxe geral
pip3 install nome_do_pacote

# Exemplo: instalando a biblioteca 'pandas' para análise de dados
pip3 install pandas
```

Para verificar se um pacote foi instalado, use `pip3 show nome_do_pacote`.

> **Próximo Passo:** Para organizar melhor seus projetos, pesquise sobre **Ambientes Virtuais (`venv`)**. Eles criam uma "caixa" de pacotes isolada para cada projeto, evitando conflitos.

-----

-----

#### 6\. Tipos de Dados

  * **`String` (str):** Usado para texto. É imutável, o que significa que seu valor não pode ser alterado após a criação. Ex: `"Olá, mundo!"`.
  * **`Integer` (int):** Representa números inteiros. Ex: `10`, `42`.
  * **`Float` (float):** Representa números de ponto flutuante (com casas decimais). Ex: `3.14`, `2.5`.
  * **`Boolean` (bool):** Representa valores lógicos, sendo apenas `True` ou `False`.
  * **`List` (list):** Uma coleção ordenada e **mutável** de itens. Os itens podem ser de diferentes tipos. Ex: `["maçã", 2, True]`.
  * **`Tuple` (tuple):** Uma coleção ordenada e **imutável** de itens. Ex: `("terra", "água", "fogo")`.
  * **`Dictionary` (dict):** Uma coleção não ordenada de pares `chave: valor`. As chaves devem ser únicas. Ex: `{"nome": "João", "idade": 30}`.

#### 7\. Tudo Sobre Strings

Strings são objetos poderosos em Python. Aqui estão alguns conceitos importantes:

  * **Criação:** Podem ser criadas com aspas simples (`' '`), duplas (`" "`) ou triplas (`""" """`). As triplas são úteis para strings de várias linhas.
  * **F-Strings:** A forma mais moderna e recomendada de formatar strings. Permitem incorporar variáveis diretamente.
    ```python
    nome = "Weslley"
    print(f"Olá, {nome}!")
    ```
  * **Concatenação:** A união de strings pode ser feita com o operador `+`. Ex: `"Olá" + " " + "Mundo"`.
  * **Métodos Comuns:**
      * `.upper()`: Retorna a string em maiúsculas.
      * `.lower()`: Retorna a string em minúsculas.
      * `.strip()`: Remove espaços em branco do início e do fim.
      * `.split(delimitador)`: Divide a string em uma lista de substrings, usando um delimitador.
      * `.replace(old, new)`: Substitui todas as ocorrências de uma substring por outra.
  * **Indexação e Fatiamento (Slicing):**
      * `string[0]` acessa o primeiro caractere.
      * `string[1:4]` acessa os caracteres do índice 1 até o 3.

#### 8\. Conversão de Unidades de Tempo

É possível criar funções simples para converter unidades de tempo.

  * **Converter Horas para Minutos:**
    ```python
    def horas_para_minutos(horas):
        return horas * 60

    print(horas_para_minutos(2))  # Saída: 120
    ```
  * **Converter Minutos para Horas:**
    ```python
    def minutos_para_horas(minutos):
        return minutos / 60

    print(minutos_para_horas(180)) # Saída: 3.0
    ```

    ----
