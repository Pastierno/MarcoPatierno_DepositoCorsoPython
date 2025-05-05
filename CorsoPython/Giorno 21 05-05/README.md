# Sistema di Previsione delle Cause di Morte

## 📊 Panoramica
Questo progetto di machine learning analizza dati globali di mortalità per identificare modelli nelle cause di morte in diversi paesi e periodi. Utilizza la regressione XGBoost per predire la distribuzione di probabilità delle cause di morte e consente di fare previsioni per periodi futuri.

## 🔍 Funzionalità
- Caricamento e analisi dei dati di mortalità per paesi e anni
- Analisi interattiva delle correlazioni con heatmap
- Trasformazione dei dati con metodi logaritmici e Yeo-Johnson
- Addestramento di modelli di regressione XGBoost con ottimizzazione degli iperparametri
- Previsione della causa di morte più probabile per un dato paese e anno
- Interfaccia a riga di comando per interagire facilmente con il modello addestrato

## 🛠️ Installazione

### Prerequisiti
- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- joblib

### Configurazione
1. Clona il repository
2. Installa i pacchetti necessari:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn xgboost joblib
    ```
3. Scarica il dataset o utilizza il file cause_of_deaths.csv fornito

## 📚 Dataset
Il dataset contiene informazioni sulle cause di morte in diversi paesi e anni:

- **Country/Territory** - Nome del paese
- **Code** - Codice del paese
- **Year** - Anno del record
- Numerose colonne per malattie (malattie cardiovascolari, cancro, ecc.)

## 🧮 Dettagli Implementativi

### Preprocessing dei Dati
- Trasformazione dei dati in formato lungo
- Calcolo della probabilità di morte per malattia
- Feature engineering con PowerTransformer per variabili numeriche
- One-hot encoding per variabili categoriche (paesi e malattie)

### Addestramento del Modello
- XGBoost Regressor con ottimizzazione degli iperparametri
- Validazione incrociata con GridSearchCV
- Metriche di valutazione: R², MAE, RMSE sia per il training che per il test set

### Deployment del Modello
- Serializzazione del modello addestrato con joblib
- Interfaccia a riga di comando per gli utenti finali
- Sistema di previsione per anni futuri e paesi arbitrari

## 🚀 Utilizzo

### 1. Analisi ed Addestramento (Jupyter Notebook)
Esegui il notebook Jupyter `cause_deaths.ipynb` per:
- Esplorare il dataset
- Addestrare modelli con diverse trasformazioni
- Eseguire analisi di correlazione
- Addestrare il modello finale e salvarlo su disco

### 2. Sistema di Previsione (Riga di Comando)
Esegui lo script Python per le previsioni:
```bash
python main_xgb.py
```

Dal menu:
1. Seleziona l'opzione 1 per prevedere la causa di morte più probabile
2. Inserisci un nome di paese (es. "Italy")
3. Inserisci un anno (es. "2025")
4. Visualizza la previsione e la probabilità

## 📈 Risultati di Esempio

Esempio di previsione:
```
Malattia più probabile in Italy nel 2100: Cardiovascular Diseases (57.32%)
```

Metriche di performance del modello dal notebook:
```
=== Metriche sul TRAIN set ===
R² (train):   0.9971
MAE (train):  0.0021
RMSE (train): 0.0039

=== Metriche sul TEST set ===
R² (test):   0.9882
MAE (test):  0.0042
RMSE (test): 0.0079
```

## 🧠 Approccio Tecnico
- **Trasformazione dei Dati**: Applicazione di trasformazioni logaritmiche e Yeo-Johnson per normalizzare i dati delle malattie con forte asimmetria
- **Feature Engineering**: Creazione di feature di probabilità invece di conteggi grezzi di morti
- **Selezione del Modello**: XGBoost scelto per la sua capacità di gestire relazioni complesse nei dati
- **Ottimizzazione degli Iperparametri**: Ricerca su griglia per parametri tra cui:
  - Numero di stimatori
  - Profondità massima
  - Tasso di apprendimento

## 🔮 Miglioramenti Futuri
- Aggiungere intervalli di confidenza alle previsioni
- Incorporare indicatori socioeconomici per previsioni più accurate
- Sviluppare un'interfaccia web per il sistema di previsione
- Aggiungere visualizzazione geografica delle previsioni
- Implementare metodi ensemble combinando più modelli