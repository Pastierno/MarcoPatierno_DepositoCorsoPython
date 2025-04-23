# Marco Patierno – Deposito Corso Python 🐍

Benvenuto nella repository che raccoglie tutte le lezioni del corso di **Python e Machine Learning**! 🎓  
Qui troverai esempi, esercizi, database di supporto e diagrammi UML, per accompagnarti in un percorso che va dalle basi del linguaggio fino a progetti pratici di Data Science e Machine Learning. Prendi confidenza, sperimenta e non aver paura di sbagliare: ogni errore è un passo avanti!

---

## 📚 Struttura della Repository

La repository è organizzata in cartelle corrispondenti ai giorni di corso, ciascuna contenente gli esercizi, esempi e progetti sviluppati durante le lezioni:

```
MarcoPatierno_DepositoCorsoPython/
├── CorsoPython/
│   ├── 01 - Introduzione/
│   ├── 02 - Strutture dati/
│   ├── ...
│   ├── Giorno 16 22-04/ 
│   │   ├── db.py
│   │   ├── esercizio.py
│   │   └── pandas/
│   │       ├── data2.csv
│   │       └── esercizio_due.py
│   │
│   └── Giorno 17 23-04/
│       └── ESERCITAZIONE vendite/
│           ├── README.md
│           ├── analisi_vendite.py
│           ├── menu.py
│           ├── creazione_csv.py
│           └── vendite.csv
│
└── README.md
```

---

## 🎯 Obiettivi del corso

1. **Basi di Python**: sintassi, tipi di dato, condizioni e cicli  
2. **Funzioni e script**: definizione, parametri, gestione file ed eccezioni  
3. **Strutture dati e OOP**: liste, dizionari, classi, incapsulamento, ereditarietà  
4. **Database**: utilizzo di SQLite con Python (`sqlite3`) e file `.db`  
5. **Programmazione strutturata**: espressioni regolari, manipolazione avanzata di stringhe e file  
6. **Moduli e librerie**: NumPy, matplotlib, e introduzione alla probabilità/statistica  
7. **Data Science & ML**: Pandas per il data wrangling e Scikit‑Learn per modellare dati  
8. **Progetti pratici**: applicazioni reali (gestione di una biblioteca, analisi vendite, recommender)

---

## 📋 Progetti principali

### [Sistema di Gestione Vendite](CorsoPython/Giorno%2016%2022-04/)
Sistema che utilizza NumPy e MySQL per analizzare dati di vendite, generare clienti casuali e produrre statistiche.
- Manipolazione database relazionale
- Calcolo di media, varianza, deviazione standard
- Utilizzo avanzato di NumPy per generazione dati

### [Sistema di Analisi Vendite OOP](CorsoPython/Giorno%2017%2023-04/ESERCITAZIONE%20vendite/)
Un'applicazione completa per l'analisi dei dati di vendite con struttura orientata agli oggetti e funzionalità avanzate di reportistica.
- [Documentazione dettagliata](CorsoPython/Giorno%2017%2023-04/ESERCITAZIONE%20vendite/README.md)
- Implementazione con paradigma OOP
- Tabelle pivot e analisi statistiche
- Esportazione dati in vari formati

### [Analisi Dati con Pandas](CorsoPython/Giorno%2016%2022-04/pandas/)
Esercizi di manipolazione e analisi dati utilizzando la libreria Pandas.
- Pulizia e trasformazione dati
- Aggregazioni e tabelle pivot
- Visualizzazione e reportistica

---

## 🔧 Prerequisiti

- **Python 3.8+**  
- Ambiente virtuale (consigliato `venv` o [Conda](https://docs.conda.io/))  
- Librerie principali:
  ```bash
  pip install numpy pandas scikit-learn matplotlib jupyter
  ```

## 🚀 Come iniziare

```bash
# 1. Clona il repository
git clone https://github.com/Pastierno/MarcoPatierno_DepositoCorsoPython.git
cd MarcoPatierno_DepositoCorsoPython

# 2. Crea e attiva un ambiente virtuale
python3 -m venv env

# macOS/Linux
source env/bin/activate

# Windows
env\Scripts\activate

# 3. Installa le dipendenze
pip install numpy pandas scikit-learn matplotlib jupyter
```

---

## 🗂️ Contenuto dettagliato

### Modulo 1: Fondamenti di Python
- Variabili e tipi di dati
- Strutture di controllo: if, for, while
- Funzioni e moduli
- Programmazione orientata agli oggetti

### Modulo 2: Strutture dati e algoritmi
- Liste, tuple, set e dizionari
- List comprehension
- Algoritmi di ordinamento e ricerca
- Gestione delle eccezioni

### Modulo 3: Database e File
- Operazioni su file e directory
- Database SQLite
- Query SQL da Python
- Connessione a MySQL

### Modulo 4: Data Analysis
- Manipolazione dati con NumPy
- Analisi dati con Pandas
- Visualizzazione con Matplotlib
- Statistica descrittiva

### Modulo 5: Machine Learning
- Preprocessing dei dati
- Modelli supervisionati e non supervisionati
- Valutazione delle performance
- Progetti pratici

---

## 💡 Suggerimenti per lo studio

1. **Eseguire gli esercizi**: Non limitarti a leggere il codice, ma eseguilo e sperimentalo
2. **Modificare gli esempi**: Prova a cambiare i parametri per vedere come si comporta il codice
3. **Consultare la documentazione**: Impara a cercare informazioni nella documentazione ufficiale
4. **Creare mini-progetti**: Applica le conoscenze acquisite in piccoli progetti personali

---

## 📞 Contatti

Per qualsiasi domanda o chiarimento sui contenuti del corso, contattami su:
- 📧 Email: [marco.patierno@example.com](mailto:marco.patierno@example.com)
- 🔗 LinkedIn: [Marco Patierno](https://www.linkedin.com/in/marcopatierno/)
- 💻 GitHub: [Pastierno](https://github.com/Pastierno)

---

## 📝 Licenza

Questo materiale è concesso in licenza sotto MIT License. Sei libero di utilizzarlo per scopi personali e didattici.

---

*"Il modo migliore per prevedere il futuro è inventarlo." - Alan Kay*

