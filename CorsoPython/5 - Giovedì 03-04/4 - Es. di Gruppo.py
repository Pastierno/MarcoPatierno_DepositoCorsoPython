# Esercitazione ristorante

class Ristorante(): # Creazione classe Ristorante
    
    def __init__(self, nome, tipo_cucina): # Costruttore
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.menu = {}      
        self.aperto = False 
        
    # Metodi della classe
    
    def descrivi_ristorante(self): # Metodo per mandare nome e tipo di cucina
        print(f'Benvenuto nel ristorante {self.nome}')
        print(f'{self.tipo_cucina} è la nostra specialità')
        
    def stato_apertura(self): # Metodo per controllare se il locale è aperto o no
        if self.aperto:
            print('Il ristorante è aperto, ha la prenotazione?')
        else:
            print('Siamo chiusi, a presto!')
        
    def apri_ristorante(self): # Metodo per aprire ristorante
        self.aperto = True
        print('Siamo aperti, jamm ja')
        
    def chiudi_ristorante(self): # Metodo per chiudere il ristorante
        self.aperto = False
        print('Cià guagliò, statt buon')
    
    def aggiungi_al_menu(self): # Aggiunta di piatti al menù
        aggiunta = input('Cosa vuoi aggiungere al menù? ')
        prezzo = float(input('A che prezzo? '))
        prezzo_form = f'€{prezzo:.2f}' # Aggiunge simbolo € e formatta a 2 decimali
        self.menu[aggiunta] = prezzo_form # Aggiunge al dizionario
        print(self.menu)
        
    def togli_dal_menu(self): # Rimuovere dal menù
        print(self.menu) # Stampa il menu
        rimuovi = input('Quale prodotto vuoi rimuovere? ').lower()
        if rimuovi in self.menu:
            del self.menu[rimuovi]
            print(f'\'{rimuovi}\' rimosso!')
        else:
            print(f'\'{rimuovi}\' non è presente nel menù')
            
    def stampa_menu(self): # Stampa il menu
        for piatto, prezzo in self.menu.items():
            print(f'{piatto}, {prezzo}')
    
test = Ristorante('F.lli MAX 3', 'Pizza')

test.aggiungi_al_menu()
test.togli_dal_menu()
test.descrivi_ristorante()
test.apri_ristorante()
test.stato_apertura()
test.chiudi_ristorante()
test.stato_apertura()
test.stampa_menu()

# def pizzeria_bomber():
#     #Un giorno ci sarà un menù
#     ist = Ristorante('Max 3 Pizza', 'Max 3 Pizze')