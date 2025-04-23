# Indovina il numero

import random

random_num = random.randint(1, 100)
# print(random_num)

def find_number():
    # Messaggio di benvenuto
    print('Benvenuto nel gioco \n')
   
    check = True
    while check:
        exit = int(input('Vuoi uscire (0) o continuare? (1)'))
        num = int(input('Scegli un numero da 1 a 100: '))
        if num > 0 and num < 100:
            # Scelta per uscire dal gioco
            if exit == 0:
                print('Ciao!')
            else:
                # Condizioni in caso di minore, maggiore o indovinato
                if num == random_num:
                    print('Bravo, hai indovinato')
                    check = False
                elif num < random_num:
                    print('Il numero è maggiore')
                    continue
                else:
                    print('Il numero è minore')
                    continue


find_number()
        
    