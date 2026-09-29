# 📊 Gerador de Tabuada em Python

Este projeto é um programa simples desenvolvido em **Python** que permite ao usuário informar um número inicial e um número final. A partir desses valores, o programa gera a **tabuada de 1 a 10** para cada número dentro do intervalo informado.

## 🚀 Funcionamento

O programa solicita duas informações:

- **Número inicial:** define onde começa a sequência de tabuadas.
- **Número final:** define onde termina a sequência.

Depois disso, o programa percorre os números do intervalo e calcula suas multiplicações de **1 até 10**.

### Exemplo

Se o usuário informar:

```text
Digite o número em que a tabuada inicia: 2
Digite o número em que a tabuada termina: 4
```

O programa irá gerar:

```text
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
...
2 X 10 = 20

3 X 1 = 3
3 X 2 = 6
...
3 X 10 = 30

4 X 1 = 4
4 X 2 = 8
...
4 X 10 = 40
```

## 🧠 Conceitos utilizados

Este exercício utiliza alguns conceitos fundamentais da programação em Python:

### `input()`

Utilizado para receber os números digitados pelo usuário.

```python
inicio = int(input("Digite o número em que a tabuada inicia: "))
```

O `int()` converte o valor recebido, que inicialmente é uma string, para um número inteiro.

### `range()`

Utilizado para criar os intervalos de números percorridos pelos loops.

```python
range(inicio, fim + 1)
```

O `+ 1` é utilizado porque o segundo valor do `range()` não é incluído.

Para a tabuada:

```python
range(1, 11)
```

Isso gera os números de **1 até 10**.

### `for`

O primeiro `for` percorre os números que terão suas tabuadas calculadas:

```python
for tabuada in range(inicio, fim + 1):
```

O segundo `for` percorre os multiplicadores de 1 a 10:

```python
for numeros in range(1, 11):
```

### F-strings

Utilizadas para formatar a saída do programa:

```python
print(f"{comeco} X {numeros} = {calculo}")
```

Isso permite apresentar o resultado de maneira mais organizada.

## 🛠️ Código

```python
inicio = int(input("Digite o número em que a tabuada inicia: "))
fim = int(input("Digite o número em que a tabuada termina: "))
comeco = 0

for tabuada in range(inicio, fim + 1):
    
    if comeco <= fim:        
        comeco += 1
        
        for numeros in range(1, 11):
            calculo = comeco * numeros
            print(f"{comeco} X {numeros} = {calculo}")
```

## ▶️ Como executar

É necessário ter o **Python 3** instalado.

Execute o arquivo pelo terminal:

```bash
python nome_do_arquivo.py
```

Em alguns sistemas, pode ser necessário utilizar:

```bash
python3 nome_do_arquivo.py
```

## 📚 Objetivo do exercício

O objetivo deste exercício é praticar:

- Entrada de dados com `input()`
- Conversão de tipos com `int()`
- Estruturas de repetição `for`
- Utilização de `range()`
- Estruturas condicionais `if`
- Operações matemáticas
- Formatação de textos com f-strings
- Loops aninhados

## 💡 Possível melhoria

O código pode ser simplificado utilizando diretamente a variável `tabuada` no cálculo, eliminando a necessidade da variável `comeco`.

Por exemplo:

```python
inicio = int(input("Digite o número em que a tabuada inicia: "))
fim = int(input("Digite o número em que a tabuada termina: "))

for tabuada in range(inicio, fim + 1):
    for numero in range(1, 11):
        calculo = tabuada * numero
        print(f"{tabuada} X {numero} = {calculo}")
```

Essa versão mantém o mesmo objetivo, mas possui menos variáveis e uma lógica mais direta.