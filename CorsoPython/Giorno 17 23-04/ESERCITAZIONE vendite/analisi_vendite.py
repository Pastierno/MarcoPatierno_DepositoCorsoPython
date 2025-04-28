import pandas as pd
import numpy as np
import os

class AnalisiVendite:
    def __init__(self, file_path): # costruttore che inizializza il percorso del file e carica i dati
        self.file_path = file_path
        self.df = self.carica_dati()
        # Cache per analisi frequenti così non ricarichiamo ogni volta
        self._pivot_mean = None
        self._groupby_sum = None
        
    def carica_dati(self):
        try:
            return pd.read_csv(self.file_path)
        except Exception as e:
            print(f"Errore nel caricamento dei dati: {e}")
            return pd.DataFrame()  # Dataframe vuoto in caso di errore
    
    def get_colonne(self):
        return self.df.columns.tolist()
    
    def get_pivot_mean(self):
        if self._pivot_mean is None: # se cache è vuota la creiamo
            # Creazione tabella pivot per analizzare le vendite per città e prodotto
            self._pivot_mean = self.df.pivot_table(
                index='Città', 
                columns='Prodotto', 
                values='Vendite', 
                aggfunc='mean'
            )
        return self._pivot_mean
    
    def get_groupby_sum(self):
        if self._groupby_sum is None: # se cache è vuota la creiamo
            # Metodo groupby per vendite totali per ogni prodotto
            self._groupby_sum = self.df.groupby('Prodotto')['Vendite'].sum().reset_index()
        return self._groupby_sum
    
    def pivot_personalizzato(self, index_col, columns_col, values_col='Vendite', aggfunc='mean'):
        # Validazione parametri per verificare se le colonne esistono nel dataframe
        if index_col not in self.df.columns or columns_col not in self.df.columns:
            raise ValueError("Colonna non trovata nel dataframe")
        if values_col not in self.df.columns:
            raise ValueError(f"Colonna {values_col} non trovata per i valori")
            
        # Creazione pivot table
        return self.df.pivot_table(
            index=index_col,
            columns=columns_col,
            values=values_col,
            aggfunc=aggfunc
        )
    
    def esporta_analisi(self, df_to_export, nome_file):
        """Esporta un dataframe nel formato specificato dall'utente"""
        try:
            type_file = input("Vuoi esportare in CSV, JSON o Excel? (csv/json/excel): ").lower()
            if type_file not in ['csv', 'json', 'excel']:
                raise ValueError("Tipo di file non supportato")
                
            extension = 'csv' if type_file == 'csv' else 'json' if type_file == 'json' else 'xlsx'
            file_path = os.path.join(os.getcwd(), f"{nome_file}.{extension}")
            
            # Esegue l'effettiva esportazione in base al tipo di file scelto
            if type_file == 'csv':
                df_to_export.to_csv(file_path)
            elif type_file == 'json':
                # Gestione particolare per tabelle pivot che non possono essere convertite direttamente in JSON
                try:
                    df_to_export.to_json(file_path)
                except TypeError:
                    # Se è una pivot table, resettiamo l'indice prima dell'esportazione
                    df_to_export.reset_index().to_json(file_path)
            elif type_file == 'excel':
                df_to_export.to_excel(file_path)
                
            return f"Dati esportati con successo in {file_path}"
        except Exception as e:
            return f"Errore nell'esportazione: {e}"
    
    def statistiche_descrittive(self):
        return self.df['Vendite'].describe()
    
    def top_n_prodotti(self, n=3):
        return self.df.groupby('Prodotto')['Vendite'].sum().sort_values(ascending=False).head(n)