def esempio_basilare():
    """
    Legge due numeri da input e ne stampa la somma.
    Se si verifica *qualsiasi* errore (input non numerico, EOF, ecc.), 
    stampa un messaggio generico.
    """
    class Pippo:
        pass
    try:
        a = int(input("Inserisci il primo numero: "))
        b = int(input("Inserisci il secondo numero: "))
        print(f"La somma è: {a + b}")
    except Pippo as e:
        # Cattura tutte le eccezioni ereditate da Exception
        print(f"Errore generico: {e}")
    else:
        # Eseguito solo se non è caduto alcun except
        print("Operazione completata con successo.")
    finally:
        # Viene sempre eseguito
        print("Fine funzione esempio_basilare.")
if __name__ == "__main__":
    esempio_basilare() 