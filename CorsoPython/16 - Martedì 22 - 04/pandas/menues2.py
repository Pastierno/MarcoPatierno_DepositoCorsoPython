import pandas as pd
import os

def carica_dati():
    df = pd.read_csv(r"CorsoPython\16 - Martedì 22 - 04\pandas\data2.csv")
    
    # Conversione dati in formato numerico
    df['Quantità'] = pd.to_numeric(df['Quantità'], errors='coerce')
    df['PrezzoUnitario'] = pd.to_numeric(df['PrezzoUnitario'], errors='coerce')
    
    # Gestione valori mancanti e conversione tipi
    df['Quantità'] = df['Quantità'].fillna(0).astype(int)
    df['PrezzoUnitario'] = df['PrezzoUnitario'].fillna(0).astype(float)
    
    # Calcolo vendite totali
    df['Totale vendite'] = df['Quantità'] * df['PrezzoUnitario']
    
    return df

def mostra_dataframe(df):
    print("\nDataFrame completo:")
    print(df)
    input("\nPremi Enter per continuare...")

def analisi_base(df):
    print("\nInformazioni sul DataFrame:")
    print(f"Numero di righe: {df.shape[0]}")
    print(f"Numero di colonne: {df.shape[1]}")
    print("\nColonne presenti:")
    for col in df.columns:
        print(f"- {col}")
    
    print("\nStatistiche descrittive:")
    print(df.describe())
    input("\nPremi Enter per continuare...")

def trova_prodotto_piu_venduto(df):
    # prodotto più venduto per valore
    df_grouped = df.groupby('Prodotto')['Totale vendite'].sum().reset_index()
    prodotto_piu_venduto = df_grouped.loc[df_grouped['Totale vendite'].idxmax()]
    
    print("\nProdotto più venduto:")
    print(f"Prodotto: {prodotto_piu_venduto['Prodotto']}")
    print(f"Totale vendite: €{prodotto_piu_venduto['Totale vendite']:.2f}")
    input("\nPremi Enter per continuare...")

def analisi_per_citta(df):
    # Numero articoli venduti per città
    df_citta = df.groupby('Città')['Quantità'].sum().reset_index()
    # Valore totale delle vendite per città
    df_citta_valore = df.groupby('Città')['Totale vendite'].sum().reset_index()
    
    print("\nNumero di articoli venduti per città:")
    print(df_citta.sort_values('Quantità', ascending=False))
    
    print("\nValore totale vendite per città:")
    print(df_citta_valore.sort_values('Totale vendite', ascending=False))
    input("\nPremi Enter per continuare...")

def filtra_vendite(df):
    try:
        soglia = float(input("\nInserisci la soglia di vendita (es. 500): "))
        df_filtrato = df[df['Totale vendite'] > soglia]
        
        if df_filtrato.empty:
            print(f"Nessuna vendita superiore a €{soglia:.2f}")
        else:
            print(f"\nVendite superiori a €{soglia:.2f}:")
            print(df_filtrato)
    except ValueError:
        print("Inserisci un valore numerico valido.")
    
    input("\nPremi Enter per continuare...")

def pivot_prodotto_citta(df):
    print("\nPivot Table: Prodotto vs Città")
    
    print("Scegli il valore da aggregare:")
    print("1. Quantità")
    print("2. Totale vendite")
    
    scelta = input("Scelta (1-2): ")
    
    if scelta == "1":
        valore = 'Quantità'
        formato = "{:.0f}"
    else:
        valore = 'Totale vendite'
        formato = "€{:.2f}"
    
    # Crea la pivot table
    pivot = pd.pivot_table(
        df, 
        values=valore,
        index='Prodotto',
        columns='Città',
        aggfunc='sum',
        fill_value=0
    )
    
    print("\nRisultato pivot table:")
    print(pivot)
    
    # Opzione per salvare il risultato
    if input("\nVuoi salvare questa pivot table in CSV? (s/n): ").lower() == 's':
        pivot.to_csv('pivot_prodotto_citta.csv')
        print("File salvato come 'pivot_prodotto_citta.csv'")
    
    input("\nPremi Enter per continuare...")

def pivot_personalizzata(df):
    print("\nCreazione Pivot Table Personalizzata")
    
    # Mostra le colonne disponibili
    print("\nColonne disponibili:")
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")
    
    # Selezione indice (righe)
    try:
        idx_righe = int(input("\nSeleziona il numero della colonna per le righe: ")) - 1
        if idx_righe < 0 or idx_righe >= len(df.columns):
            print("Indice non valido.")
            input("\nPremi Enter per continuare...")
            return
        colonna_righe = df.columns[idx_righe]
        
        # Selezione colonne
        idx_colonne = int(input("\nSeleziona il numero della colonna per le colonne: ")) - 1
        if idx_colonne < 0 or idx_colonne >= len(df.columns):
            print("Indice non valido.")
            input("\nPremi Enter per continuare...")
            return
        colonna_colonne = df.columns[idx_colonne]
        
        # Selezione valori
        idx_valori = int(input("\nSeleziona il numero della colonna per i valori: ")) - 1
        if idx_valori < 0 or idx_valori >= len(df.columns):
            print("Indice non valido.")
            input("\nPremi Enter per continuare...")
            return
        colonna_valori = df.columns[idx_valori]
        
        # Selezione funzione di aggregazione
        print("\nFunzioni di aggregazione disponibili:")
        print("1. Somma")
        print("2. Media")
        print("3. Conteggio")
        print("4. Minimo")
        print("5. Massimo")
        
        agg_choice = input("\nSeleziona la funzione di aggregazione (1-5): ")
        agg_funcs = {
            "1": "sum",
            "2": "mean",
            "3": "count",
            "4": "min",
            "5": "max"
        }
        
        if agg_choice not in agg_funcs:
            print("Scelta non valida.")
            input("\nPremi Enter per continuare...")
            return
        
        aggfunc = agg_funcs[agg_choice]
        
        # Creazione della pivot table
        pivot = pd.pivot_table(
            df,
            values=colonna_valori,
            index=colonna_righe,
            columns=colonna_colonne,
            aggfunc=aggfunc,
            fill_value=0
        )
        
        print(f"\nPivot Table ({colonna_righe} vs {colonna_colonne}, valori: {colonna_valori}, agg: {aggfunc}):")
        print(pivot)
        
        # Opzione per salvare il risultato
        if input("\nVuoi salvare questa pivot table in CSV? (s/n): ").lower() == 's':
            nome_file = f"pivot_{colonna_righe}_{colonna_colonne}_{aggfunc}.csv"
            pivot.to_csv(nome_file)
            print(f"File salvato come '{nome_file}'")
            
    except (ValueError, IndexError) as e:
        print(f"Errore: {e}")
    
    input("\nPremi Enter per continuare...")

def esporta_dataframe(df):
    print("\nEsportazione DataFrame")
    print("Scegli il formato:")
    print("1. CSV")
    print("2. Excel")
    print("3. HTML")
    
    scelta = input("Scelta (1-3): ")
    
    nome_file = input("Inserisci il nome del file (senza estensione): ")
    
    try:
        if scelta == "1":
            df.to_csv(f"{nome_file}.csv", index=False)
            print(f"File salvato come '{nome_file}.csv'")
        elif scelta == "2":
            df.to_excel(f"{nome_file}.xlsx", index=False)
            print(f"File salvato come '{nome_file}.xlsx'")
        elif scelta == "3":
            df.to_html(f"{nome_file}.html")
            print(f"File salvato come '{nome_file}.html'")
        else:
            print("Scelta non valida.")
    except Exception as e:
        print(f"Errore durante l'esportazione: {e}")
    
    input("\nPremi Enter per continuare...")

def analisi_avanzata(df):
    print("\nAnalisi Avanzata")
    print("1. Top 3 prodotti più venduti")
    print("2. Percentuale vendite per città")
    print("3. Relazione tra quantità e prezzo unitario")
    
    scelta = input("Scelta (1-3): ")
    
    if scelta == "1":
        top_prodotti = df.groupby('Prodotto')['Totale vendite'].sum().sort_values(ascending=False).head(3)
        print("\nTop 3 prodotti più venduti:")
        for prod, vendite in top_prodotti.items():
            print(f"{prod}: €{vendite:.2f}")
    
    elif scelta == "2":
        vendite_citta = df.groupby('Città')['Totale vendite'].sum()
        totale = vendite_citta.sum()
        percentuali = (vendite_citta / totale * 100).sort_values(ascending=False)
        
        print("\nPercentuale vendite per città:")
        for citta, perc in percentuali.items():
            print(f"{citta}: {perc:.2f}%")
    
    elif scelta == "3":
        # Calcola la correlazione
        corr = df['Quantità'].corr(df['PrezzoUnitario'])
        print(f"\nCorrelazione tra Quantità e Prezzo Unitario: {corr:.4f}")
        
        # Calcola prezzo medio per range di quantità
        df['Range Quantità'] = pd.cut(df['Quantità'], bins=[0, 1, 5, 10, 100], 
                                    labels=['1', '2-5', '6-10', '11+'])
        
        prezzo_per_range = df.groupby('Range Quantità')['PrezzoUnitario'].mean()
        print("\nPrezzo medio unitario per range di quantità:")
        for range_q, prezzo in prezzo_per_range.items():
            print(f"Quantità {range_q}: €{prezzo:.2f}")
    
    else:
        print("Scelta non valida.")
    
    input("\nPremi Enter per continuare...")

def menu_principale():
    df = carica_dati()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nAnalisi Vendite")
        print("1. Visualizza dati")
        print("2. Statistiche di base")
        print("3. Trova prodotto più venduto")
        print("4. Analisi per città")
        print("5. Filtra vendite per valore")
        print("6. Pivot Table: Prodotto vs Città")
        print("7. Pivot Table personalizzata")
        print("8. Esporta dati")
        print("9. Analisi avanzata")
        print("0. Esci")
        
        scelta = input("\nScegli un'opzione (0-9): ")
        
        if scelta == "1":
            mostra_dataframe(df)
        elif scelta == "2":
            analisi_base(df)
        elif scelta == "3":
            trova_prodotto_piu_venduto(df)
        elif scelta == "4":
            analisi_per_citta(df)
        elif scelta == "5":
            filtra_vendite(df)
        elif scelta == "6":
            pivot_prodotto_citta(df)
        elif scelta == "7":
            pivot_personalizzata(df)
        elif scelta == "8":
            esporta_dataframe(df)
        elif scelta == "9":
            analisi_avanzata(df)
        elif scelta == "0":
            print("\nUscita dal programma...")
            break
        else:
            print("\nOpzione non valida. Riprova.")
            input("Premi Enter per continuare...")

if __name__ == "__main__":
    menu_principale()