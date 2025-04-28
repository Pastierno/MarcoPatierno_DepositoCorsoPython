# 📊 **Progetto Analisi Spotify**

## 🎶 Descrizione

Benvenuti nel progetto **Analisi Spotify**! Questo progetto è un'analisi approfondita dei dati musicali di Spotify, che esplora le classifiche giornaliere dal 2018 fino a ottobre 2020. Utilizzando Python e librerie come `pandas`, `matplotlib`, e `seaborn`, l'obiettivo è quello di scoprire trend musicali, analizzare performance di canzoni e artisti, e visualizzare le tendenze nel tempo. 

Le principali attività di questo progetto includono:
- **Analisi statistica** delle classifiche giornaliere.
- **Visualizzazione** delle tendenze musicali nel tempo.
- Esplorazione di **informazioni significative** riguardanti le performance delle canzoni più ascoltate.

## 🚀 Funzionalità

### 🔧 **Struttura del Progetto**

Il progetto è diviso in vari moduli per una gestione più semplice e chiara dei dati:

- **`main.py`**: È il punto di ingresso principale, che orchestrerà l'esecuzione del programma.
- **`menus.py`**: Contiene tutti i menu principali a cui è possibile accedere dal main.
- **`data_analysis.py`**: Contiene funzioni per analisi dei dati riguardanti il dataframe delle classifiche spotify.
- **`data_cleaning.py`**: Definisce il DataFrame che contiene le classifiche e le operazioni su di esso.
- **`utils.py`**: È il modulo che contiene i decoratori.
- **`statistical_analysis.py`**: Contiene funzioni di analisi statistica di dati numerici.
- **`visualization.py`**: Gestisce la creazione dei grafici per visualizzare le tendenze e le performance musicali.

### 📈 **Caratteristiche principali**

- Analisi delle canzoni più popolari nel tempo.
- Esplorazione di come diversi **generi musicali** abbiano dominato le classifiche.
- Analisi delle performance per **artista** e **album**.
- **Visualizzazioni interattive** per una facile interpretazione dei dati.

## 🔍 Documentazione

Il progetto è stato sviluppato da un team di tre membri:

- **Giovanni**: Responsabile per la fase di analisi del dataframe delle classifiche spotify, inclusa la scrittura della classe `DataframeAnalyzer` e del file di avviamento `main.py`.
- **Marco**: Ha lavorato sulla visualizzazione grafica, creando la classe `Visualyzer`, assicurandosi della corretta integrazione dei moduli di analisi (`data_analysis.py` e `statistical_analysis.py`).
- **Nunzio**: Ha sviluppato la classe `StatisticalAnalyzer`, che ha contribuito all'analisi dei dati numerici, e si è occupato del refactoring del file di avviamento `main.py` disaccoppiando le dipendenze e scrivendo i file `menus.py` e `utils.py`.

## 🛠 Requisiti

Assicurati di avere Python 3.x e le seguenti librerie installate:

- **pandas**: Per la gestione dei dati.
- **matplotlib**: Per la creazione di grafici statici.
- **seaborn**: Per visualizzazioni più avanzate.

Installa le dipendenze con il comando:

```bash
pip install pandas matplotlib seaborn
```
vedi anche il file requirements.txt

## 🧑‍💻 Autori

Il progetto è stato sviluppato da un team di tre membri:

- **Marco**
[Linkedin](https://www.linkedin.com/in/marco-patierno-a933a6352/) | [Mail]()
- **Giovanni**
[Linkedin](https://www.linkedin.com/in/giovanni-pisaniello-094201317/) | [Mail](pisaniellogiovanni53@gmail.com)
- **Nunzio**
[Linkedin](https://www.linkedin.com/in/nunzio-de-cicco/) | [Mail](decicconunzio@gmail.com)
