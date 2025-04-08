# Cifrario di Cesare
# def cesare(input_c, k):
#     c_list = 'abcdefghijklmnopqrstuvwxyz'
#     e_list = []
#     res = [c for c in c_list]
#     input_c = [c for c in input_c.lower() if c.isalpha()]

#     for c in input_c:
#         position = res.index(c)
#         new_position = position + k
#         e_list.append(new_position)
    
#     nuova_stringa = [c_list[i] for i in e_list]
#     nuova_stringa2 = ''.join(nuova_stringa)
#     return nuova_stringa2

# def decesare(input_c, k):
#     return cesare(input_c, -k)


def cifra(testo,chiave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    risultato = ""

    for lettera in testo:
        if lettera.islower():
            posizione = alfabeto.find(lettera)
            nuova_posizione = (posizione + chiave) % 26
            risultato += alfabeto[nuova_posizione]
        else:
            risultato += lettera # non cifra caratteri non alfabetici

    print(risultato)
    return risultato


def decifra(testo, chiave):
    return cifra(testo, -chiave)

def menu():
    while True:
        choise = int(input('Ciao! che operazione vuoi effettuare?  \n'
                           '1. Cifra una stringa \n'
                           '2. Decifra una stringa \n'
                           '3. Esci \n'))
        match choise:
            case 1:
                stringa = input('Inserisci la stringa da cifrare: ')
                chiave = int(input('Inserisci la chiave (0 - 25): '))
                #if chiave >= 0 and chiave <= 25:
                testo_cifrato = cifra(stringa, chiave)
                print(testo_cifrato)
                #else:
                   # print('Numero non valido, riprova.')
                    
            case 2:
                stringa = input('Inserisci la stringa da cifrare: ')
                chiave = int(input('Inserisci la chiave (0 - 25): '))
                #if chiave >= 0 and chiave <= 25:
                testo_cifrato = decifra(stringa, chiave)
                print(testo_cifrato)
                #else:
                 #3
                 #print('Numero non valido, riprova.')
            
            case 3:
                print('Cià')
                break
menu()
