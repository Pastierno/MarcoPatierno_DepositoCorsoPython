# Creare un sistema di gestione per la fabbrica che produce e vende vari
# tipi di prodotti. Gli studenti dovranno creare una classe base chiamata
# Prodotto e diverse classi parallele che rappresentano diversi tipi di prodotti
# Inoltre, dovranno creare una classe Fabbrica che gestisce l'inventario e 
# le vendite dei prodotti



class Prodotto():
    def __init__(self, nome, costo_produzione, prezzo): # Costruttore iniziale prodotto
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo = prezzo
        
    def calcola_profitto(self): # Metodo per calcolo profitto
        profitto = self.prezzo - self.costo_produzione
        return profitto
        
class Fabbrica:
    def __init__(self, prodotti={}): # Costruttore fabbrica
        self.prodotti = prodotti

    def aggiungi_prodotto(self): # Metoto per aggiungere prodotto e crea nuovo oggetto Prodotto
        nome = input('Inserisci il nome del prodotto: \n').lower()
        quantita = int(input('Inserisci la quantità: \n'))
        costo = float(input("Inserisci il costo di produzione: "))
        prezzo = float(input("Inserisci il prezzo di vendita: "))
        nuovo_prodotto = Prodotto(nome, costo, prezzo) # Nuovo oggetto prodotto
        if nome in self.prodotti:
            self.prodotti[nome][1] += quantita # Aggiunge quantità se presente nell'inventario
        else:
            self.prodotti[nome] = [nuovo_prodotto, quantita] # Aggiunge nuovo prodotto
        print(f"Prodotto '{nome}' aggiunto, quantità attuale: {self.prodotti[nome][1]}")

    def vendi_prodotto(self): # Metodo vendi prodotto
        print("Inventario:")
        for nome, (prodotto, quantita) in self.prodotti.items(): 
            print(f"{nome}: {quantita} disponibili, Prezzo: {prodotto.prezzo} €") # Stampa nome quantità e prezzo
            
        scelta = input('Quale prodotto vuoi acquistare? ').lower()
        if scelta in self.prodotti: # Se il prodotto esiste
            prodotto, quantita_disponibile = self.prodotti[scelta] # Recupera i dati
            if quantita_disponibile > 0:
                quantita_venduta = int(input('Quanti ne vuoi acquistare? \n'))
                if quantita_venduta <= quantita_disponibile: # Se disponibile diminuisce quantità e calcola profitto e ricavo
                    self.prodotti[scelta][1] -= quantita_venduta # Diminuisce quantità
                    ricavo = prodotto.prezzo * quantita_venduta # Calcola ricavo
                    profitto_unitario = prodotto.calcola_profitto() # Utilizza metodo per calcolare profitto unitario
                    profitto_totale = profitto_unitario * quantita_venduta # Calcola il profitto totale
                    print(f"Acquisto effettuato per {quantita_venduta} unità di '{scelta}'!")
                    print(f"Ricavo totale: {ricavo} €")
                    print(f"Profitto: {profitto_totale} €")
                else:
                    print(f"Quantità non disponibile, ne abbiamo solo {quantita_disponibile}")
            else:
                print("Quantità non disponibile")
        else:
            print("Prodotto non esistente")
            
    def reso_prodotto(self): # aggiunge quantità resa
        scelta = input('Di quale prodotto vuoi effettuare il reso? ').lower()
        if scelta in self.prodotti: # Controlla se presente in dict prodotti
            quantita = int(input('Che quantità vuoi restituire? \n'))
            self.prodotti[scelta][1] += quantita # Aggiunge quantità
            print(f"Reso effettuato! Nuova quantità disponibile: {self.prodotti[scelta][1]}")
        else:
            print("Prodotto non esistente") 

    def visualizza_inventario(self): # visualizzare prodotti nell'inventario
        print("Inventario attuale:")
        for nome, (prodotto, quantita) in self.prodotti.items():
            print(f"{nome}: {quantita} disponibili, Prezzo: {prodotto.prezzo} €")

def menu_fabbrica1(): # funzione per avviare il menu
    fabbrica = Fabbrica() # istanza
    while True: # ciclo per tenere apero il menù
        scelta = int(input('\nBenvenuto, che operazione desideri effettuare? \n'
                           '1- Aggiungi prodotto\n'
                           '2- Bendi prodotto\n'
                           '3- Reso prodotto\n'
                           '4- Visualizza inventario\n'
                           '5- Esci\n'))
        if scelta == 1:
            fabbrica.aggiungi_prodotto()
        elif scelta == 2:
            fabbrica.vendi_prodotto()
        elif scelta == 3:
            fabbrica.reso_prodotto()
        elif scelta == 4:
            fabbrica.visualizza_inventario()
        elif scelta == 5:
            print("Ciao!")
            break
        else:
            print("Opzione non valida.")
            
            
menu_fabbrica1()
            
        