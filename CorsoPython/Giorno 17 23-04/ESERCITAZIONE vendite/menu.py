import os
from analisi_vendite import AnalisiVendite

def main():
    file_path = r'CorsoPython\Giorno 17 23 -04\ESERCITAZIONE vendite\vendite.csv'
    
    # Verifica esistenza file prima di procedere
    if not os.path.exists(file_path):
        print(f"Errore: il file {file_path} non esiste.")
        file_path = input("Inserisci il percorso corretto del file CSV: ")
        if not os.path.exists(file_path):
            print("File non trovato. Uscita dal programma.")
            return
    
    # Creazione dell'oggetto analisi
    analisi = AnalisiVendite(file_path)
    
    # Visualizza il menu
    menu(analisi)

def menu(analisi):
    print("\nANALISI VENDITE")
    
    while True:
        print("\nSeleziona un'opzione:")
        print("1. Visualizza tabella pivot delle vendite medie per città e prodotto")
        print("2. Visualizza vendite totali per ogni prodotto")
        print("3. Analisi personalizzata")
        print("4. Statistiche descrittive")
        print("5. Top 5 prodotti per vendite")
        print("6. Esporta dati")
        print("7. Esci")
        
        try:
            choice = input("\nInserisci il numero dell'opzione desiderata: ")
            
            if choice == '1':
                print("\nTabella pivot delle vendite medie per città e prodotto:")
                pivot_result = analisi.get_pivot_mean()
                print(pivot_result)
                
                # Opzione rapida per esportare SOLO la tabella pivot
                if input("\nVuoi esportare questa tabella? (s/n): ").lower() == 's':
                    nome_file = input("Inserisci il nome del file (senza estensione): ")
                    print(analisi.esporta_analisi(pivot_result, nome_file))
                
            elif choice == '2':
                print("\nVendite totali per ogni prodotto:")
                vendite_totali = analisi.get_groupby_sum()
                print(vendite_totali)
                
                # Formattazione migliore per i risultati
                print("\nRiepilogo:")
                totale_generale = vendite_totali['Vendite'].sum()
                for i, row in vendite_totali.iterrows():
                    percentuale = (row['Vendite'] / totale_generale) * 100
                    print(f"{row['Prodotto']}: {row['Vendite']:.2f} ({percentuale:.1f}% del totale)")
                
            elif choice == '3':
                # Analisi personalizzata
                print("\nANALISI PERSONALIZZATA")
                print("Colonne disponibili:")
                colonne = analisi.get_colonne()
                for i, col in enumerate(colonne, 1):
                    print(f"{i}. {col}")
                
                try:
                    # Selezione colonne tramite indici per evitare errori di battitura
                    idx1 = int(input("\nSeleziona il numero della prima colonna (indice): ")) - 1
                    idx2 = int(input("Seleziona il numero della seconda colonna (features)): ")) - 1
                    
                    if idx1 < 0 or idx1 >= len(colonne) or idx2 < 0 or idx2 >= len(colonne):
                        raise ValueError("Indice colonna non valido")
                    
                    col1 = colonne[idx1]
                    col2 = colonne[idx2]
                    
                    # Funzioni di aggregazione disponibili
                    print("\nFunzioni di aggregazione disponibili:")
                    print("1. Media (mean)")
                    print("2. Somma (sum)")
                    print("3. Conteggio (count)")
                    print("4. Massimo (max)")
                    print("5. Minimo (min)")
                    
                    func_choice = input("Seleziona la funzione (1-5): ")
                    func_map = {
                        '1': 'mean',
                        '2': 'sum',
                        '3': 'count',
                        '4': 'max',
                        '5': 'min'
                    }
                    
                    if func_choice not in func_map:
                        raise ValueError("Funzione non valida")
                    
                    func = func_map[func_choice]
                    
                    # Selezione colonna valori
                    idx_val = int(input("\nSeleziona il numero della colonna per i valori (values): ")) - 1
                    if idx_val < 0 or idx_val >= len(colonne):
                        raise ValueError("Indice colonna non valido")
                    values_col = colonne[idx_val]
                    
                    df_pivot = analisi.pivot_personalizzato(col1, col2, values_col=values_col, aggfunc=func)
                    
                    print(f"\nTabella pivot personalizzata ({func}) per {col1} e {col2}:")
                    print(df_pivot)
                    
                    # Opzione per esportare
                    if input("\nVuoi esportare questa analisi? (s/n): ").lower() == 's':
                        nome_file = input("Inserisci il nome del file (senza estensione): ")
                        print(analisi.esporta_analisi(df_pivot, nome_file))
                    
                except ValueError as e:
                    print(f"Errore: {e}")
                    
            elif choice == '4':
                print("\nStatistiche descrittive sulle vendite:")
                stats = analisi.statistiche_descrittive()
                print(stats)
                
                # Interpretazione dei risultati
                print("\nInterpretazione:")
                print(f"Media vendite: {stats['mean']:.2f}")
                print(f"Deviazione standard: {stats['std']:.2f}")
                print(f"Valore minimo: {stats['min']:.2f}")
                print(f"Valore massimo: {stats['max']:.2f}")
                print(f"25° percentile: {stats['25%']:.2f}")
                print(f"Mediana (50° percentile): {stats['50%']:.2f}")
                print(f"75° percentile: {stats['75%']:.2f}")
                
            elif choice == '5':
                n = 3
                try:
                    n_input = input(f"Quanti prodotti top vuoi visualizzare? (default: {n}): ")
                    if n_input.strip():
                        n = int(n_input)
                except ValueError:
                    print(f"Valore non valido, uso il default: {n}")
                
                print(f"\nTop {n} prodotti per vendite totali:")
                top_prodotti = analisi.top_n_prodotti(n)
                
                # Formattazione migliorata per i risultati
                totale = top_prodotti.sum()
                for prodotto, vendite in top_prodotti.items():
                    percentuale = (vendite / totale) * 100
                    print(f"{prodotto}: {vendite:.2f} ({percentuale:.1f}% del totale)")
                    
            elif choice == '6':
                print("\nESPORTAZIONE DATI")
                print("1. Esporta pivot città-prodotto")
                print("2. Esporta vendite per prodotto")
                print("3. Esporta dataset completo")
                
                export_choice = input("Cosa vuoi esportare? (1-3): ")
                nome_file = input("Inserisci il nome del file (senza estensione): ")
                
                if export_choice == '1':
                    print(analisi.esporta_analisi(analisi.get_pivot_mean(), nome_file))
                elif export_choice == '2':
                    print(analisi.esporta_analisi(analisi.get_groupby_sum(), nome_file))
                elif export_choice == '3':
                    print(analisi.esporta_analisi(analisi.df, nome_file))
                else:
                    print("Opzione non valida")
                    
            elif choice == '7':
                print("\nGrazie per aver utilizzato il sistema di analisi vendite. Arrivederci!")
                break
                
            else:
                print("Opzione non valida. Riprova.")
                
        except Exception as e:
            print(f"Si è verificato un errore: {e}")
            print("Riprova o seleziona un'altra opzione.")

if __name__ == "__main__":
    main()