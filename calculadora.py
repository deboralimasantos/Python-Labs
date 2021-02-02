print('****Calculadora em Python****')


numero1 = int(input('Digite o primeiro numero: ')) #colocar int no começo
numero2 = int(input('digite o segundo nnumero: '))

soma = 1
subtracao = 2
divisao = 3
multiplicacao = 4

print('\n soma=1\n subtração=2\n divisao=3\n multiplicacao:4\n')

operacao = int(input('Digite qual operacao deseja efetuar: ')) #colocar int no começo


if operacao == 1:
    resultado = numero1+numero2
    print('a soma é: ',resultado)

if operacao == 2:
    resultado = numero1 - numero2
    print('A subtração é:',resultado)
if operacao == 3:
    resultado = numero1 / numero2
    print('A divisão é: ',resultado)
if operacao == 4:
    resultado = numero1 * numero2
    print('A multiplicação é: ',resultado)
