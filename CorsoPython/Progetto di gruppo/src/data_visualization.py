import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.dates as mdates
from matplotlib.colors import LinearSegmentedColormap
from src.data_analysis import DataframeAnalizer
from src.data_cleaning import dataframe # clean the dataframe


class Visualizer:
    def __init__(self, analizer=None):
        """
        Inizializza il visualizzatore con un oggetto Analizer.
        
        Args:
            analizer: Un'istanza di DataframeAnalizer o None (in tal caso verrà creata)
        """
        # Configurazione stile
        plt.style.use('seaborn-v0_8-whitegrid')
        sns.set(font_scale=1.1)
        self.colors = sns.color_palette("viridis", 10)
        self.highlight_color = "#1DB954"  # Spotify green
        
        # Se non viene fornito un analizzatore, creane uno nuovo
        if analizer is None:
            df = dataframe()
            self.analizer = DataframeAnalizer(df)
        else:
            self.analizer = analizer

    def visualize_top_tracks(self, n=10):
        """Visualizza le top n tracce per numero di stream"""
        top_tracks = self.analizer.top_tracks(n=n)
        
        plt.figure(figsize=(12, 8))
        ax = sns.barplot(x='Streams', y='Track', data=top_tracks, palette='viridis')
        
        # Aggiungi etichette con il valore
        for i, v in enumerate(top_tracks['Streams']):
            ax.text(v + v*0.01, i, f'{v:,}', va='center')
        
        plt.title(f'Top {n} Brani per Numero di Stream', fontsize=16, fontweight='bold')
        plt.xlabel('Numero di Stream', fontsize=14)
        plt.ylabel('Brano', fontsize=14)
        
        # Aggiungi l'artista accanto al titolo del brano
        labels = [f"{track} - {artist}" for track, artist in zip(top_tracks['Track'], top_tracks['Artist'])]
        ax.set_yticklabels(labels)
        
        plt.tight_layout()
        plt.show()
        
    def visualize_top_artists(self, n=10):
        """Visualizza i top n artisti per numero totale di stream"""
        top_artists = self.analizer.top_artists(n=n)
        
        plt.figure(figsize=(12, 8))
        ax = sns.barplot(x=top_artists.index, y=top_artists.values, palette='viridis')
        
        # Ruota le etichette
        plt.xticks(rotation=45, ha='right')
        
        # Aggiungi etichette con il valore
        for i, v in enumerate(top_artists.values):
            ax.text(i, v + v*0.01, f'{v:,}', ha='center', fontweight='bold')
        
        plt.title(f'Top {n} Artisti per Numero Totale di Stream', fontsize=16, fontweight='bold')
        plt.xlabel('Artista', fontsize=14)
        plt.ylabel('Stream Totali', fontsize=14)
        plt.tight_layout()
        plt.show()
        
    def visualize_most_streamed_track(self):
        """Visualizza un grafico a barre per la traccia più ascoltata"""
        track = self.analizer.most_streamed_track()
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x=['Stream'], y=[track['Streams']], palette=[self.highlight_color])
        
        plt.title(f"Brano Più Ascoltato: {track['Track']} - {track['Artist']}", 
                 fontsize=16, fontweight='bold')
        plt.xlabel('')
        plt.ylabel('Numero di Stream', fontsize=14)
        
        # Aggiungi etichetta con il valore
        plt.text(0, track['Streams'] + track['Streams']*0.01, 
                f'{track["Streams"]:,}', ha='center', fontweight='bold')
        
        plt.tight_layout()
        plt.show()
        
    def visualize_streams_by_artist(self, artist):
        """Visualizza un grafico a barre per tutti i brani di un artista specifico"""
        artist_tracks = self.analizer.streams_by_artist(artist)
        
        if artist_tracks.empty:
            print(f"Nessun brano trovato per l'artista '{artist}'")
            return
            
        # Ordina per numero di stream (decrescente)
        artist_tracks = artist_tracks.sort_values('Streams', ascending=False)
        
        plt.figure(figsize=(12, 8))
        ax = sns.barplot(x='Streams', y='Track', data=artist_tracks, palette='viridis')
        
        # Aggiungi etichette con il valore
        for i, v in enumerate(artist_tracks['Streams']):
            ax.text(v + v*0.01, i, f'{v:,}', va='center')
        
        plt.title(f'Brani di {artist} per Numero di Stream', fontsize=16, fontweight='bold')
        plt.xlabel('Numero di Stream', fontsize=14)
        plt.ylabel('Brano', fontsize=14)
        plt.tight_layout()
        plt.show()
        
    def visualize_tracks_above_threshold(self, threshold):
        """Visualizza i brani con stream superiori a una soglia"""
        tracks = self.analizer.tracks_above_threshold(threshold)
        
        if tracks.empty:
            print(f"Nessun brano trovato con più di {threshold:,} stream")
            return
            
        # Ordina per numero di stream (decrescente)
        tracks = tracks.sort_values('Streams', ascending=False)
        
        # Limita a 20 brani per leggibilità 
        if len(tracks) > 20:
            print(f"Mostro solo i primi 20 brani su {len(tracks)} totali")
            tracks = tracks.head(20)
        
        plt.figure(figsize=(12, 10))
        ax = sns.barplot(x='Streams', y='Track', data=tracks, palette='viridis')
        
        # Aggiungi etichette con il valore
        for i, v in enumerate(tracks['Streams']):
            ax.text(v + v*0.01, i, f'{v:,}', va='center')
        
        # Aggiungi linea per la soglia
        plt.axvline(x=threshold, color='red', linestyle='--', 
                   label=f'Soglia: {threshold:,}')
        
        # Aggiungi l'artista accanto al titolo del brano
        labels = [f"{track} - {artist}" for track, artist in zip(tracks['Track'], tracks['Artist'])]
        ax.set_yticklabels(labels)
        
        plt.title(f'Brani con più di {threshold:,} Stream', fontsize=16, fontweight='bold')
        plt.xlabel('Numero di Stream', fontsize=14)
        plt.ylabel('Brano', fontsize=14)
        plt.legend()
        plt.tight_layout()
        plt.show()
        
    def visualize_artists_track_count(self, top_n=15):
        """Visualizza un grafico a barre con il numero di brani per artista"""
        artist_counts = self.analizer.artists_track_count()
        
        # Ordina per conteggio (decrescente) e prendi i top N
        artist_counts = artist_counts.sort_values('Track Count', ascending=False).head(top_n)
        
        plt.figure(figsize=(12, 8))
        ax = sns.barplot(x='Artist', y='Track Count', data=artist_counts, palette='viridis')
        
        # Ruota le etichette
        plt.xticks(rotation=45, ha='right')
        
        # Aggiungi etichette con il valore
        for i, v in enumerate(artist_counts['Track Count']):
            ax.text(i, v + 0.1, str(v), ha='center', fontweight='bold')
        
        plt.title(f'Top {top_n} Artisti per Numero di Brani', fontsize=16, fontweight='bold')
        plt.xlabel('Artista', fontsize=14)
        plt.ylabel('Numero di Brani', fontsize=14)
        plt.tight_layout()
        plt.show()
        
    def visualize_daily_streams(self, start_day, days=30):
        """Visualizza gli stream giornalieri a partire da un giorno specifico"""
        try:
            daily_streams = self.analizer.daily_streams_custom(start_day)
            
            # Limita il numero di giorni
            if len(daily_streams) > days:
                daily_streams = daily_streams.head(days)
                
            plt.figure(figsize=(14, 8))
            ax = sns.lineplot(x='Date', y='Streams', data=daily_streams, 
                             marker='o', linewidth=2.5, color=self.highlight_color)
            
            # Formatta l'asse x
            plt.gcf().autofmt_xdate()
            date_format = mdates.DateFormatter('%d %b')
            plt.gca().xaxis.set_major_formatter(date_format)
            
            # Aggiungi etichette con il valore sui punti
            for x, y in zip(daily_streams['Date'], daily_streams['Streams']):
                ax.annotate(f'{y:,}', 
                           (x, y), 
                           textcoords="offset points", 
                           xytext=(0,10), 
                           ha='center',
                           fontsize=9)
                
            plt.title(f'Stream Giornalieri dal {start_day}', fontsize=16, fontweight='bold')
            plt.xlabel('Data', fontsize=14)
            plt.ylabel('Stream Totali', fontsize=14)
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Errore nella visualizzazione degli stream giornalieri: {e}")
            
    def visualize_top_artists_since(self, day, n=10):
        """Visualizza i top artisti a partire da un giorno specifico"""
        try:
            top_artists = self.analizer.top_artists_since(day, n=n)
            
            plt.figure(figsize=(12, 8))
            ax = sns.barplot(x=top_artists.index, y=top_artists.values, palette='viridis')
            
            # Ruota le etichette
            plt.xticks(rotation=45, ha='right')
            
            # Aggiungi etichette con il valore
            for i, v in enumerate(top_artists.values):
                ax.text(i, v + v*0.01, f'{v:,}', ha='center', fontweight='bold')
            
            plt.title(f'Top {n} Artisti dal {day}', fontsize=16, fontweight='bold')
            plt.xlabel('Artista', fontsize=14)
            plt.ylabel('Stream Totali', fontsize=14)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Errore nella visualizzazione dei top artisti: {e}")
    
    def visualize_monthly_streams(self, start_month, end_month=None):
        """Visualizza gli stream mensili per un intervallo di mesi"""
        try:
            monthly_data = self.analizer.monthly_streams(start_month, end_month)
            
            if monthly_data.empty:
                print("Nessun dato trovato per il periodo specificato")
                return
                
            plt.figure(figsize=(14, 8))
            ax = monthly_data.plot(kind='bar', color=self.highlight_color, figsize=(14, 8))
            
            # Formatta le etichette dell'asse x
            plt.xticks(rotation=45, ha='right')
            
            # Converti le etichette dei periodi in stringhe più leggibili
            labels = [str(idx).replace('M', '-') for idx in monthly_data.index]
            ax.set_xticklabels(labels)
            
            # Aggiungi etichette con il valore
            for i, v in enumerate(monthly_data.values):
                ax.text(i, v + v*0.01, f'{v:,}', ha='center', fontweight='bold')
            
            plt.title('Trend Mensile degli Stream', fontsize=16, fontweight='bold')
            plt.xlabel('Mese', fontsize=14)
            plt.ylabel('Stream Totali', fontsize=14)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Errore nella visualizzazione degli stream mensili: {e}")
    
    def visualize_top_track_in_month(self, start_month, end_month=None):
        """Visualizza le tracce più ascoltate per ogni mese in un intervallo"""
        try:
            top_tracks = self.analizer.top_track_in_month(start_month, end_month)
            
            if top_tracks.empty:
                print("Nessun dato trovato per il periodo specificato")
                return
                
            plt.figure(figsize=(14, 8))
            
            # Usa Month sia per le etichette che per il colore
            if 'Month' in top_tracks.columns:
                ax = sns.barplot(x='Month', y='Streams', data=top_tracks, hue='Month', palette='viridis')
                
                # Converti le etichette dei periodi in stringhe più leggibili
                labels = [str(month).replace('M', '-') for month in top_tracks['Month']]
                ax.set_xticklabels(labels)
            else:
                ax = sns.barplot(x='Date', y='Streams', data=top_tracks, palette='viridis')
            
            # Ruota le etichette
            plt.xticks(rotation=45, ha='right')
            
            # Aggiungi etichette con brano e artista sopra le barre
            for i, (_, row) in enumerate(top_tracks.iterrows()):
                ax.text(i, row['Streams'] + row['Streams']*0.01, 
                       f"{row['Track']} - {row['Artist']}", 
                       ha='center', fontsize=9, rotation=45)
            
            plt.title('Brani Più Ascoltati per Mese', fontsize=16, fontweight='bold')
            plt.xlabel('Mese', fontsize=14)
            plt.ylabel('Stream', fontsize=14)
            
            # Rimuovi la legenda se presente (ridondante)
            if plt.legend():
                plt.legend().remove()
                
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Errore nella visualizzazione dei top track per mese: {e}")
    
    def visualize_top_artists_in_month(self, start_month, end_month=None, n=10):
        """Visualizza i top artisti in un mese specifico o intervallo di mesi"""
        try:
            top_artists = self.analizer.top_artists_in_month(start_month, end_month, n=n)
            
            if top_artists.empty:
                print("Nessun dato trovato per il periodo specificato")
                return
                
            plt.figure(figsize=(12, 8))
            ax = sns.barplot(x=top_artists.index, y=top_artists.values, palette='viridis')
            
            # Ruota le etichette
            plt.xticks(rotation=45, ha='right')
            
            # Aggiungi etichette con il valore
            for i, v in enumerate(top_artists.values):
                ax.text(i, v + v*0.01, f'{v:,}', ha='center', fontweight='bold')
            
            # Prepara il titolo a seconda che sia un singolo mese o un intervallo
            if end_month is None:
                title = f'Top {n} Artisti nel Mese {start_month}'
            else:
                title = f'Top {n} Artisti da {start_month} a {end_month}'
                
            plt.title(title, fontsize=16, fontweight='bold')
            plt.xlabel('Artista', fontsize=14)
            plt.ylabel('Stream Totali', fontsize=14)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Errore nella visualizzazione dei top artisti: {e}")
    
    def visualize_position_vs_streams(self):
        """Visualizza la relazione tra posizione in classifica e numero di stream"""
        plt.figure(figsize=(10, 8))
        
        sns.scatterplot(x='Position', y='Streams', data=self.analizer.df, 
                       alpha=0.7, size='Streams', sizes=(50, 200), hue='Position')
        
        plt.title('Relazione tra Posizione in Classifica e Stream', fontsize=16, fontweight='bold')
        plt.xlabel('Posizione', fontsize=14)
        plt.ylabel('Stream', fontsize=14)
        
        # Inverti l'asse x (posizione 1 è la migliore)
        plt.gca().invert_xaxis()
        
        plt.tight_layout()
        plt.show()
    
    def visualize_streams_pie_chart(self, top_n=7):
        """Visualizza un grafico a torta con la distribuzione degli stream per i top artisti"""
        top_artists = self.analizer.top_artists(n=top_n)
        
        # Calcola il totale degli stream
        total_streams = self.analizer.df['Streams'].sum()
        
        # Calcola gli stream degli altri artisti
        other_streams = total_streams - top_artists.sum()
        
        # Aggiungi la categoria "Altri"
        if other_streams > 0:
            complete_data = pd.Series({**top_artists.to_dict(), 'Altri': other_streams})
        else:
            complete_data = top_artists
            
        plt.figure(figsize=(12, 10))
        
        # Evidenzia il primo spicchio
        explode = [0.1] + [0 for _ in range(len(complete_data)-1)]
        
        patches, texts, autotexts = plt.pie(
            complete_data.values, 
            labels=complete_data.index, 
            autopct='%1.1f%%',
            explode=explode,
            startangle=90,
            shadow=True,
            colors=sns.color_palette('viridis', len(complete_data))
        )
        
        # Migliora la leggibilità delle etichette
        for text in texts:
            text.set_fontsize(12)
        for autotext in autotexts:
            autotext.set_fontsize(10)
            autotext.set_color('white')
            
        plt.title('Distribuzione degli Stream per Artista', fontsize=16, fontweight='bold')
        plt.axis('equal')  # Mantiene la forma circolare
        plt.tight_layout()
        plt.show()
        
    def visualize_all(self):
        """Esegue tutte le visualizzazioni principali per una panoramica completa"""
        # Panoramica generale
        self.visualize_top_tracks(n=7)
        self.visualize_top_artists(n=7)
        self.visualize_streams_pie_chart()
        self.visualize_position_vs_streams()
        self.visualize_artists_track_count(top_n=10)
        
        # Se ci sono date nel dataset, aggiungi le visualizzazioni temporali
        if 'Date' in self.analizer.df.columns:
            # Prendi la prima e ultima data disponibile
            min_date = self.analizer.df['Date'].min().strftime('%Y-%m-%d')
            min_month = self.analizer.df['Date'].min().strftime('%Y-%m')
            
            # Visualizzazioni temporali
            self.visualize_daily_streams(min_date)
            self.visualize_monthly_streams(min_month)


# ESEMPIO DI UTILIZZO

# # Crea un'istanza di Visualizer (che caricherà automaticamente il dataframe)
# viz = Visualizer()

# # Visualizza i top 10 brani per numero di stream
# viz.visualize_top_tracks(n=10)

# # Visualizza i top 10 artisti per numero totale di stream
# viz.visualize_top_artists(n=10)

# # Visualizza il brano più ascoltato
# viz.visualize_most_streamed_track()

# # Visualizza tutti i brani di un artista specifico (sostituisci con un artista presente nei tuoi dati)
# viz.visualize_streams_by_artist("Ed Sheeran")

# # Visualizza i brani con più di 1 milione di stream
# viz.visualize_tracks_above_threshold(1000000)

# # Visualizza il numero di brani per artista
# viz.visualize_artists_track_count()

# # Visualizza la relazione tra posizione in classifica e stream
# viz.visualize_position_vs_streams()

# # Visualizza un grafico a torta con la distribuzione degli stream per artista
# viz.visualize_streams_pie_chart()

# # Per visualizzazioni temporali (usa date presenti nel tuo dataset)
# # viz.visualize_daily_streams("2022-01-01")
# # viz.visualize_monthly_streams("2022-01")

# # Panoramica completa con tutte le visualizzazioni principali
# # viz.visualize_all()
