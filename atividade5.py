#5.2 Exercícios de Prática em Python (Sintaxe)


#8. Verificação de Vida:  Escreva um código que peça  a  vida  do jogador. Se for igual a 0, imprima "Game Over"

vida = int(input("Digite a vida do jogador: "))
if vida == 0:
    print("Game Over")

#9. Teste de Maioridade:  Crie um script que peça a  idade do usuário. Se for 18 ou mais, exiba "Acesso Liberado ao Jogo". Caso contrário, exiba "Acesso Negado"
idade = int(input("Digite a idade do usuário: "))
if idade >= 18:
    print("Acesso Liberado ao Jogo")
else:
    print("Acesso Negado")

#10. Par ou Ímpar:  Peça um número ao usuário. Use o  operador  %  e uma estrutura if/else  para dizer se o número é par ou ímpar

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#11. Sistema de Notas:  Crie um programa que receba  a nota de um aluno:
#●  Se for 7 ou mais: "Aprovado"
#●  Se for entre 5 e 6.9: "Recuperação".
#●  Se for menor que 5: "Reprovado"

nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

#12. Comparando Dois Números:  Peça ao usuário dois  números (  n1  e  n2  ). O programa deve dizer qual deles é o maior ou se são iguais
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"O maior número é: {numero1}")
elif numero2 > numero1:
    print(f"O maior número é: {numero2}")
else:
    print("Os números são iguais.")

#13. Validação de Login:  Crie uma variável  senha_mestra  = "python123"  . Peça ao usuário para digitar uma senha e use um  if  para  verificar se ele acertou. 
senha_mestra = "python123"
senha_usuario = input("Digite a senha: ")

if senha_usuario == senha_mestra:
    print("Acesso Liberado ao Jogo")
else:
    print("Acesso Negado")

#14. Verificador de Número Positivo:  Escreva um código  que diga se um número digitado é positivo, negativo ou zero

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
elif numero == 0:
    print("O número é zero.")
