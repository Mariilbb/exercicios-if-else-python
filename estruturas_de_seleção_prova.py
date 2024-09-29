# 1 - determine se um número é positivo ou negativo

num = int(input("Digite um número: "))

if num > 0:
    print("O número é positivo")
else:
    print("O número é negativo")

print("FIM DO EXERCICIO 1")

#2 - escreva um programa que determine se a pessoa pode dirigir ou não (+18)

ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = 2024
idade = ano_atual - ano_nasc

if idade >= 18:
    print("Você pode dirigir")
else:
    print("Você não pode dirigit")

print("FIM DO EXERCICIO 2")

# 3 - escreva um programa que verifique se o numero é divisivel por 3 ou por 5

num = int(input("Digite um numero: "))

if num % 3 == 0 or num % 5 == 0:
    print("o numero é divisivel por 3 ou por 5")
else:
    print("o numero não é divisivel por 3 ou por 5")

print("FIM DO EXERCICIO 3")

# 4 - escreva um programa que ordene 3 numeros em ordem crescente

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

if num1 <= num2 and num2 <= num3:
    print("os numeros em ordem crescente são:", num1, num2, num3)
elif num1 <= num3 and num3 <= num2:
    print("os numeros em ordem crescente são:", num1, num3, num2)
elif num2 <= num1 and num1 <= num3:
    print("os numeros em ordem crescente são:", num2, num1, num3)
elif num2 <= num3 and num3 <= num1:
    print("os numeros em ordem crescente são:", num2, num3, num1)
elif num3 <= num1 and num1<= num2:
    print("os numeros em ordem crescente são:", num3, num1, num2)
else:
    print("os numeros em ordem crescente são:", num3, num2, num1)

print("FIM DO EXERCICIO 4")

# 5 - Escreva um programa que receba duas notas e calcule a média.
# Se a média for maior ou igual a 7, imprima "Aprovado".
# Se a média for menor que 7 e maior ou igual a 5, imprima "Recuperação".
# Caso contrário, imprima "Reprovado".

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7:
    print("aprovado")
elif media < 7 and media >= 5:
    print("recuperação")
else:
    print("reprovado")

print("FIM DO EXERCICIO 5")

# 6 - calcule o IMC. Se o IMC for menor que 18,5, imprima "Abaixo do peso".
# Se o IMC for maior ou igual a 18,5 e menor que 25, imprima “Peso normal”.
# Se o IMC for maior ou igual a 25 e menor que 30, imprima "Acima do peso".
# Se o IMC for maior ou igual a 30, imprima "Obeso".

imc = float(input("digite seu IMC: "))

if imc < 18.5:
    print("abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("peso normal")
elif imc >= 25 and imc < 30:
    print("acima do peso")
else:
    print("obeso")

print("FIM DO EXERCICIO 6")

# 7 - calcule o IRPF segundo a tabela:
# Salário             IRPF
# Até R$1.903,98            Isento
# De R$1.903,99 até R$2.826,65    7,5%
# De R$2.826,66 até R$3.751,05    15%
# De R$3.751,06 até R$4.664,68    22,5%

salario = float(input("digite seu salario: "))

if salario <= 1903.98:
    print("isento de imposto")
elif salario <= 2826.65:
    irpf = salario * 0.075
    print(f"o imposto é de R$ {irpf}")
elif salario <= 3751.05:
    irpf = salario * 0.15
    print(f"o imposto é de R$ {irpf}")
else:
    irpf = salario * 0.225
    print(f"o imposto é de R$ {irpf}")

print("FIM DO EXERCICIO 7")

# 8 - A partir de três notas de um aluno e informe o conceito a partir da media
#Média de aproveitamento      Conceito
#Entre 9.0 e 10.0                A
#Entre 7.5 e 9.0                 B
#Entre 6.0 e 7.5                 C
#Entre 4.0 e 6.0                 D
#Entre 4.0 e zero                E
#Caso, o conceito seja abaixo de C, indique reprovado, caso contrário aprovado.

nota1 = float(input("digite sua nota: "))
nota2 = float(input("digite sua nota: "))
nota3 = float(input("digite sua nota: "))
media = (nota1 + nota2 + nota3) / 3

if media > 9:
    conceito = "A"
elif media > 7.5:
    conceito = "B"
elif media > 6:
    conceito = "C"
elif media > 4:
    conceito = "D"
else:
    conceito = "E"

print(f"a media é: {media:.1f}")
print(f"o conceito é: {conceito}")

if media >= 6:
    print("aprovado")
else:
    print("reprovado")

print("FIM DO EXERCICIO 8")

# 9 - calcule o frete dadas as seguintes condições:
#Para compras até R$ 100,00 reais, o frete é 10% do valor do produto

#Para compras acima de R$ 100,00 o frete é grátis, se o volume não ultrapassar a franquia de 1m3 e 3 KGs

#Para os demais casos, o frete custa 25 reais por cada m3 ou KG (o que for mais caro).

valor_compra = float(input("digite o valor da compra: R$ "))
peso = float(input("digite o peso da caixa: "))
volume = float(input("digite o volume da caixa: "))

if valor_compra <= 100:
    frete = valor_compra * 0.1
elif peso <= 3 and volume <= 1:
    frete = 0
else:
    volume *= 25
    peso *= 25
    if volume > peso:
        frete = volume
    else:
        frete = peso

print(f"o valor do frete é de: R$ {frete:.2f}")

print("FIM DO EXERCICIO 9")

# 10 - implemente um jogo de dupla de par ou impar

escolha_jogador1 = input("Jogador 1, escolha 'par' ou 'ímpar': ")
if escolha_jogador1 == 'par' or escolha_jogador1 == 'ímpar':
    numero_jogador1 = int(input("Jogador 1, escolha um número de 0 a 10: "))
    numero_jogador2 = int(input("Jogador 2, escolha um número de 0 a 10: "))

    soma = numero_jogador1 + numero_jogador2
    print("A soma dos números jogados é:", soma)

    if soma % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"

    if escolha_jogador1 == resultado:
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")



