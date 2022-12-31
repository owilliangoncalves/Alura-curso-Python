import random
def jogar():
    print("**********************************************")
    print("Bem vindo (a)! Adivinhe nosso número aleatório")
    print("**********************************************")

    numeroDeTentativasP = int (input ("Quantas tentativas você deseja ter?"))
    if (numeroDeTentativasP <= 5):
        print ("Você escolheu o nível difícil!")
    elif (numeroDeTentativasP >= 6 and numeroDeTentativasP < 16):
        print ("Você está em um nível intermediario!")
    if (numeroDeTentativasP >= 16):
        print ("Você está em um nível fácil")

    numero_secreto = random.randrange(1,101)
    numeroDeTentativas = numeroDeTentativasP
    rodada = 1

    for rodada in range  (1, numeroDeTentativas + 1):
        print ("Tentativa {} de {}". format(rodada, numeroDeTentativas))
        
        chute = int (input ("Digite um número entre 1 e 100 "))
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if (chute < 1 or chute > 100):
            print ("Digite um valor entre 1 e 100")
            continue

        if numero_secreto == chute:
            print ("Parabens! Você acertou nosso número secreto")
            break

        else:
            if (maior):
                print ("Seu chute foi maior que o numero secreto.")

            elif (menor):
                print ("Seu chute foi menor que o numero secreto.")
                
    print ("Fim de jogo")
if (__name__ == "__main__"):
    jogar()