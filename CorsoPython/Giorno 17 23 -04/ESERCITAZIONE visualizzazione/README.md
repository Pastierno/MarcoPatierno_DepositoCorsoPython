# Data Visualizer CLI

## Descrizione
Questo progetto è un semplice **Data Visualizer** da riga di comando, sviluppato in Python, che:
- Genera un dataset sintetico di 1.000 individui con altezza, peso, età e sesso.
- Calcola il BMI (Body Mass Index) di ciascun individuo.
- Normalizza le variabili numeriche con **Min-Max Scaling**.
- Offre una serie di opzioni per visualizzare relazioni e distribuzioni tramite `matplotlib` e `seaborn`.
- Permette di aggiungere un filtro personalizzato basato su un range di valori scelto dall’utente e di vedere subito come il filtro influisce sui grafici.

## Caratteristiche principali
- **Scatter plot** altezza vs peso (originale e normalizzato).
- **Distribuzioni** di altezza, peso, età, BMI (istogrammi, KDE).
- **Box plot** per confronti tra sesso e variabili numeriche.
- **Heatmap** della matrice di correlazione.
- **Pair plot** per tutte le variabili.
- **Regression plot** per la relazione età-peso.
- **Filtro dinamico** per qualsiasi variabile (età, altezza, peso, BMI) con:
  - Colonna booleana `*_in_range`
  - Colonna categorica `*_categoria` (“Sotto range”, “Nel range”, “Sopra range”)
  - Grafici dedicati che mostrano l’effetto del filtro

## Requisiti
- Python 3.7+
- Librerie:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`

Puoi installarle tutte con:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Struttura del progetto
```
.
├── README.md
└── data_visualizer.py   # Script principale con tutte le funzioni
```

## Utilizzo
1. Clona la repository o scarica lo script `data_visualizer.py`.
2. Apri un terminale e posizionati nella cartella contenente lo script.
3. Avvia il programma con:
   ```bash
   python data_visualizer.py
   ```
4. Segui le istruzioni a schermo: ti verrà mostrato un menu numerato con tutte le opzioni di visualizzazione.
5. Seleziona un’opzione digitando il numero corrispondente e premi **Invio**.
6. Per aggiungere un filtro personalizzato, scegli l’opzione **10** e definisci il range su una delle variabili.
7. Se hai applicato un filtro, apparirà l’opzione **11** per esplorare i grafici filtrati.
8. Digita **0** per uscire.

## Panoramica delle funzioni
- `create_dataframe(num_rows=1000)`:  
  Genera il DataFrame con:  
  - **sesso** (M/F),  
  - **età** (18–75, distribuzione normale centrata a 40 anni),  
  - **altezza** (differenziata per sesso),  
  - **peso** calcolato da un BMI di base e modificato dall’età,  
  - **bmi** calcolato come `peso / (altezza/100)^2`.

- `min_max(df)`:  
  Applica il **MinMaxScaler** di scikit-learn su colonne numeriche (`altezza`, `peso`, `eta`, `bmi`) restituendo un DataFrame normalizzato.

- `add_range_column(df)`:  
  - Chiede all’utente di selezionare una variabile (`età`, `altezza`, `peso`, `bmi`).  
  - Mostra il range disponibile e richiede un intervallo `[min, max]`.  
  - Aggiunge due colonne:  
    - `<var>_in_range` (booleano),  
    - `<var>_categoria` (categorico: “Sotto range”, “Nel range”, “Sopra range”).  
  - Ritorna il DataFrame aggiornato e i parametri del range.

- Ciclo principale (`main()`):  
  - Costruisce i DataFrame (`df` e `df_scaled`).  
  - Mostra il menu delle 11 opzioni (+ uscita).  
  - In base alla scelta, genera e visualizza il grafico corrispondente usando `seaborn` e `matplotlib`.

## Suggerimenti per l’estensione
- Aggiungere altre variabili sintetiche (ad es. livello di attività, dieta).
- Esportare i grafici in file PNG invece di visualizzarli a schermo.
- Creare report automatici con `ReportLab` o `Plotly`.
- Integrare un’interfaccia grafica (es. con `Tkinter` o `Dash`).
- Permettere il caricamento di dataset reali da file CSV.

---

Spero che questo README ti sia utile per comprendere e utilizzare al meglio l’esercizio! Se hai domande o vuoi approfondire qualche aspetto, sono qui per aiutarti. Buon lavoro e divertiti a esplorare i dati!