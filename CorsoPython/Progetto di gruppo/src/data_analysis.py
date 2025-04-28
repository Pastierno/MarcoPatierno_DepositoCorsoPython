import numpy as np
import pandas as pd
from src.data_cleaning import dataframe # Importa una funzione o un oggetto chiamato `dataframe` da un modulo locale


class DataframeAnalizer:
    """Classe per effettuare analisi statistiche e temporali 
    su un DataFrame contenente dati musicali (es. Spotify charts)"""
    def __init__(self, df):
        self.df = df.copy()  # Lavora su una copia per evitare modifiche accidentali all'originale
        if 'Date' in self.df.columns:
            # Se c'è una colonna 'Date', la converte in tipo datetime per facilitare le analisi temporali
            self.df['Date'] = pd.to_datetime(self.df['Date'])

    # ANALISI GENERALI
    def top_tracks(self, n=10):
        """Restituisce i primi n brani con il maggior numero di stream"""
        return self.df.nlargest(n, 'Streams')

    def top_artists(self, n=10):
        """Raggruppa per artista e somma gli stream totali, restituendo i primi n"""
        return self.df.groupby('Artist')['Streams'].sum().nlargest(n)

    def most_streamed_track(self):
        """Trova l'indice del brano con più stream e restituisce l'intera riga"""
        idx = np.argmax(self.df['Streams'].values)
        return self.df.iloc[idx]

    def streams_by_artist(self, artist):
        """Filtra il dataframe per un artista specifico (case insensitive)"""
        return self.df[self.df['Artist'].str.lower() == artist.lower()]

    def tracks_above_threshold(self, threshold):
        """Restituisce tutti i brani che superano una certa soglia di stream"""
        return self.df[self.df['Streams'] > threshold]

    def artists_track_count(self):
        """Conta quanti brani ha ogni artista e restituisce un nuovo DataFrame"""
        return self.df.groupby('Artist')['Track'].count().reset_index(name='Track Count')

    # ANALISI TEMPORALI GIORNALIERE
    def filter_by_day(self, day):
        """Filtra i brani dal giorno specificato in poi"""
        return self.df[self.df['Date'] >= pd.to_datetime(day)]

    def daily_streams_custom(self, day):
        """Calcola il totale di stream per giorno a partire da una certa data"""
        df_filtered = self.filter_by_day(day)
        return df_filtered.groupby('Date')['Streams'].sum().reset_index()

    def top_artists_since(self, day, n=10):
        """Restituisce i top n artisti per stream dal giorno specificato in poi"""
        df_filtered = self.filter_by_day(day)
        return df_filtered.groupby('Artist')['Streams'].sum().nlargest(n)

    # ANALISI TEMPORALI MENSILI
    def filter_by_month_range(self, start_month, end_month=None):
        """Aggiunge una colonna 'Month' con solo anno e mese"""
        self.df['Month'] = self.df['Date'].dt.to_period('M')
        start = pd.Period(start_month, freq='M')
        end = pd.Period(end_month, freq='M') if end_month else start
        # Filtra per intervallo di mesi (o un singolo mese)
        return self.df[(self.df['Month'] >= start) & (self.df['Month'] <= end)]

    def top_track_in_month(self, start_month, end_month=None):
        """Trova il brano con più stream per ogni mese nell'intervallo specificato"""
        df_filtered = self.filter_by_month_range(start_month, end_month)
        idx = df_filtered.groupby('Month')['Streams'].idxmax()  # Indici dei massimi
        return df_filtered.loc[idx].sort_values(by='Date')

    def top_artists_in_month(self, start_month, end_month=None, n=10):
        """Restituisce i top n artisti per stream nell'intervallo di mesi"""
        df_filtered = self.filter_by_month_range(start_month, end_month)
        return df_filtered.groupby('Artist')['Streams'].sum().nlargest(n)

    def monthly_streams(self, start_month, end_month=None):
        """Calcola il totale di stream per mese in un intervallo di mesi"""
        df_filtered = self.filter_by_month_range(start_month, end_month)
        return df_filtered.groupby('Month')['Streams'].sum()


# ESEMPIO DI UTILIZZO

# Crea un'istanza della classe DataframeAnalizer usando il dataframe importato
analisis = DataframeAnalizer(dataframe())
# Stampa il totale degli stream per giorno a partire dal 1 gennaio 2018
print(analisis.daily_streams_custom('2018-01-01'))
# Stampa i brani con più stream da gennaio a marzo 2018
print(analisis.top_track_in_month('2018-01', '2018-03'))
