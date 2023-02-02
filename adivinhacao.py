import random

print("*********************************")
print("Bem-vindo(a) ao Jogo de Advinhação da Sara!")
print("*********************************")

def jogo():
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil: 20 tentativas\n(2) Médio: 10 tentativas\n(3) Difícil: 5 tentativas")

    while(True):
        nivel = int(input("Escolha: "))

        if (nivel == 1):
            print("**** Nível FÁCIL ****")
            total_de_tentativas = 20
            break
        elif (nivel == 2):
            print("**** Nível MÉDIO ****")
            total_de_tentativas = 10
            break
        elif (nivel == 3):
            print("**** Nível DIFÍCIL ****")
            total_de_tentativas = 5
            break
        else:
            print("Número inválido. Você deve digitar '1' para 'Fácil', '2' para 'Médio' ou '3' para 'Difícil'. Escolha novamente.")
            continue    

        
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou: ", chute)

        erro = (chute < 1 or chute > 100)
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        pontos_perdidos = abs(numero_secreto - chute) #Exemplo: 40 é o nº secreto e 20 meu chute. 40 - 20 =  20 pontos perdidos
        pontos = pontos - pontos_perdidos
        
        if (acertou):
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
            jogar_novamente()
            break

        else:
            if (nivel == 1 and rodada < 20 and chute >= 1 and chute <= 100 and chute > numero_secreto):
                print("Você errou! O seu chute foi maior que o número secreto. Tente de novo.")
                continue
            elif (nivel == 1 and rodada < 20 and chute >= 1 and chute <= 100 and chute < numero_secreto):
                print("Você errou! O seu chute foi menor que o número secreto. Tente de novo.")
                continue
            elif (nivel == 2 and rodada < 10 and chute >= 1 and chute <= 100 and chute > numero_secreto):
                print("Você errou! O seu chute foi maior que o número secreto. Tente de novo.")
                continue
            elif (nivel == 2 and rodada < 10 and chute >= 1 and chute <= 100 and chute < numero_secreto):
                print("Você errou! O seu chute foi menor que o número secreto. Tente de novo.")
                continue
            elif (nivel == 3 and rodada < 5 and chute >= 1 and chute <= 100 and chute > numero_secreto):
                print("Você errou! O seu chute foi maior que o número secreto. Tente de novo.")
                continue
            elif (nivel == 3 and rodada < 5 and chute >= 1 and chute <= 100 and chute < numero_secreto):
                print("Você errou! O seu chute foi menor que o número secreto. Tente de novo.")
                continue
            elif(nivel == 1 and rodada < 20 and erro):
                print("Você deve digitar um número entre 1 e 100. Próxima tentativa.")
                continue
            elif(nivel == 2 and rodada < 10 and erro):
                print("Você deve digitar um número entre 1 e 100. Próxima tentativa.")
                continue
            elif(nivel == 3 and rodada < 5 and erro):
                print("Você deve digitar um número entre 1 e 100. Próxima tentativa.")
                continue
            elif(nivel == 1 and rodada == 20 and erro):
                print("Você deve digitar um número entre 1 e 100. Fim das tentativas. O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
                jogar_novamente()
                break
            elif(nivel == 2 and rodada == 10 and erro):
                print("Você deve digitar um número entre 1 e 100. Fim das tentativas. O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
                jogar_novamente()
                break
            elif(nivel == 3 and rodada == 5 and erro):
                print("Você deve digitar um número entre 1 e 100. Fim das tentativas. O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
                jogar_novamente()
                break
            elif (nivel == 1 and rodada == 20 and chute >= 1 and chute <= 100):
                print("Você errou. O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
                jogar_novamente()
                break
            elif(nivel == 2 and rodada == 10 and chute >= 1 and chute <= 100):
                print("Você errou. O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
                jogar_novamente()
                break
            elif(nivel == 3 and rodada == 5 and chute >= 1 and chute <= 100):
                print("Você errou. O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
                jogar_novamente()
                break


def jogar_novamente():
    de_novo = str(input("Quer jogar mais uma vez? Digite 'S' para 'SIM' ou 'N' para 'NÃO': "))
    if (de_novo == "S" or de_novo == "s"):
        jogo()
    elif(de_novo == "N" or de_novo == "n"):
        print("Obrigado por jogar conosco! Tchau!")
        print("Fim de jogo!")
    else:
        print("Não entendi, você deve digitar 'S' para 'SIM' ou 'N' para 'NÃO'. Escolha novamente.")
        jogar_novamente()

jogo()
