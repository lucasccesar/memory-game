import random
import os
clear = lambda: os.system('cls')

winners = []

while True:
    nome = input('Digite Seu Nome: ')
    matriz = [['  ', 'A:', 'B:', 'C:', 'D:'], ['1:'], ['2:',], ['3:'], ['4:']]
    matrizTemp = [['  ', 'A:', 'B:', 'C:', 'D:'],['1:', '__', '__', '__', '__'], ['2:', '__', '__', '__', '__'], ['3:', '__', '__', '__', '__'], ['4:', '__', '__', '__', '__']]
    languages = ['js', 'js', 'py', 'py', 'go', 'go', 'cs', 'cs', 'rs', 'rs', 'kt', 'kt', 'rb', 'rb', 'ts', 'ts']
    atempts = 0
    corrects = 0


    while len(languages) > 0:
        x = random.randint(0, 3)
        while len(matriz[x]) >= 5:
            x = random.randint(1, 4)
        y = random.randint(0, len(languages) - 1)
        matriz[x].append(languages[y])
        del languages[y]

    print()

    while corrects < 8:
        res = input('Digite Uma Linha e Uma Coluna (Ex: 1A): ')

        try:
            line1 = int(res[0])
        except:
            line1 = 5
        if len(res) == 2:
            if res[1].lower() == 'a':
                column1 = 1
            elif res[1].lower() == 'b':
                column1 = 2
            elif res[1].lower() == 'c':
                column1 = 3
            elif res[1].lower() == 'd':
                column1 = 4
            else:
                column1 = 5
        else:
            column1 = 5

        while (line1 > 4 or column1) > 4 or (matrizTemp[line1][column1] != '__'):
            res = input('\nDigite Uma Linha e Uma Coluna Válida e Que Não Tenha Acertado Ainda (Linha: 1-4, Coluna: A-D): ')
            try:
                line1 = int(res[0])
            except:
                line1 = 5
            if len(res) == 2:
                if res[1].lower() == 'a':
                    column1 = 1
                elif res[1].lower() == 'b':
                    column1 = 2
                elif res[1].lower() == 'c':
                    column1 = 3
                elif res[1].lower() == 'd':
                    column1 = 4
                else:
                    column1 = 5
            else:
                column1 = 5
        clear()
        
        matrizTemp[line1][column1] = matriz[line1][column1]

        print()

        for i in range(len(matrizTemp)):
            for j in range(len(matrizTemp[i])):
                print(matrizTemp[i][j], end=' ')
            print()

        print()

        res = input('Digite Outra Uma Linha e Uma Coluna (Ex: 1A): ')
        try:
            line2 = int(res[0])
        except:
            line2 = 5
        if len(res) == 2:
            if res[1].lower() == 'a':
                column2 = 1
            elif res[1].lower() == 'b':
                column2 = 2
            elif res[1].lower() == 'c':
                column2 = 3
            elif res[1].lower() == 'd':
                column2 = 4
            else:
                column2 = 5
        else:
            column2 = 5

        while (line2 > 4 or column2 > 4) or (line1 == line2 and column1 == column2) or (matrizTemp[line2][column2] != '__'):
            res = input('\nDigite Uma Linha e Uma Coluna Válida, Diferente da Anterior e Que Não Tenha Acertado Ainda (Linha: 1-4, Coluna: A-D): ')
            try:
                line2 = int(res[0])
            except:
                line2 = 5
            if len(res) == 2:
                if res[1].lower() == 'a':
                    column2 = 1
                elif res[1].lower() == 'b':
                    column2 = 2
                elif res[1].lower() == 'c':
                    column2 = 3
                elif res[1].lower() == 'd':
                    column2 = 4
                else:
                    column2 = 5
            else:
                column2 = 5

        print()

        matrizTemp[line2][column2] = matriz[line2][column2]

        for i in range(len(matrizTemp)):
            for j in range(len(matrizTemp[i])):
                print(matrizTemp[i][j], end=' ')
            print()

        print()

        if matrizTemp[line1][column1] != matriz[line2][column2]:
            matrizTemp[line1][column1] = '__'
            matrizTemp[line2][column2] = '__'
            print('Tente Novamente\n')
        else:
            print('Acertou!\n')
            corrects+=1

        for i in range(len(matrizTemp)):
            for j in range(len(matrizTemp[i])):
                print(matrizTemp[i][j], end=' ')
            print()

        print()

        atempts+=1

    print(f'Parabéns, {nome}! Você Ganhou Em {atempts} tentativas!')
    winners.append((nome, atempts))

    jogar = input('Deseja Jogar Novamente (S/N)? ')
    print(jogar)

    if jogar.lower() == 'n':
        break

clear()

winners.sort(key=lambda x: x[1])
print('Placar:')
for e in range(len(winners)):
    print(f'{e+1}º Jogador: {winners[e][0]}, Pontuação: {winners[e][1]}')
