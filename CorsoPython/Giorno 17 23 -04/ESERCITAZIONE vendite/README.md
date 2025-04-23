# Sistema di Analisi Vendite

Un'applicazione Python per analizzare dati di vendite con funzionalità avanzate di reportistica, analisi e esportazione dati, implementata con un approccio orientato agli oggetti.

## Descrizione

Questo progetto implementa un sistema completo per l'analisi di dati di vendite, utilizzando pandas per l'elaborazione e una struttura OOP per incapsulare le funzionalità. L'applicazione offre un'interfaccia a riga di comando user-friendly che permette di generare rapidamente analisi, statistiche ed esportare i risultati in vari formati.

## Struttura del Progetto

- `menu.py`: Interfaccia utente interattiva
- `analisi_vendite.py`: Classe principale che contiene la logica di analisi dati
- `vendite.csv`: Dataset di esempio (generato da `creazione_csv.py`)
- `creazione_csv.py`: Script per generare dati di test

## Requisiti

- Python 3.6+
- Librerie richieste:
  - pandas
  - numpy

Puoi installare le dipendenze con:

```bash
pip install pandas numpy
```

## Funzionalità

Il sistema offre le seguenti funzionalità principali:

1. **Tabelle Pivot**: Generazione di tabelle pivot per analizzare le vendite per città e prodotto
2. **Analisi per Prodotto**: Calcolo delle vendite totali per ogni prodotto
3. **Analisi Personalizzate**: Creazione di tabelle pivot con parametri personalizzabili
4. **Statistiche Descrittive**: Analisi statistica completa dei dati di vendita
5. **Top Prodotti**: Identificazione dei prodotti con le vendite più elevate
6. **Esportazione Dati**: Esportazione dei risultati in CSV, JSON o Excel

## Come Utilizzare

1. Clona o scarica il repository
2. Assicurati di avere i requisiti installati
3. Esegui lo script principale:

```bash
python menu.py
```

## Esempi di Utilizzo

### Tabella Pivot per Città e Prodotto

Visualizza una tabella pivot che mostra la media delle vendite per ogni combinazione di città e prodotto:

```
Tabella pivot delle vendite medie per città e prodotto:
Prodotto  Birra      Grappa     Vino
Città                              
Milano   124.675325  126.388889  126.750000
Napoli   123.776596  126.833333  123.606061
Roma     125.000000  119.270270  122.068966
```

### Top 3 Prodotti

Visualizza i tre prodotti più venduti con i relativi valori e percentuali:

```
Top 3 prodotti per vendite totali:
Birra: 20821.00 (34.1% del totale)
Vino: 20235.00 (33.2% del totale)
Grappa: 19955.00 (32.7% del totale)
```

## Architettura del Sistema

Il progetto segue un'architettura orientata agli oggetti:

- **Classe `AnalisiVendite`**: Gestisce il caricamento, l'elaborazione e l'analisi dei dati
  - Utilizza tecniche di caching per migliorare le performance
  - Offre metodi per vari tipi di analisi (pivot, groupby, statistiche)
  - Gestisce l'esportazione dei risultati in vari formati

- **Interfaccia menu**: Fornisce un'interfaccia utente intuitiva
  - Gestisce l'interazione con l'utente
  - Presenta i risultati in modo leggibile
  - Offre opzioni per personalizzare le analisi

## Caratteristiche Tecniche

- **Caching dei risultati**: La classe memorizza i risultati di operazioni costose per migliorare le performance
- **Gestione degli errori**: Implementazione di robuste strutture try-except
- **Validazione input**: Controllo e validazione degli input utente
- **Formattazione avanzata**: Presentazione dei risultati con formattazione leggibile
- **Esportazione flessibile**: Supporto per diversi formati di esportazione

## Generazione Dati di Test

Lo script `creazione_csv.py` può essere utilizzato per generare nuovi dati di test:

```bash
python creazione_csv.py
```

Questo script genera 500 record casuali con date, città, prodotti e valori di vendita.

## Contribuire

Sentiti libero di contribuire a questo progetto aggiungendo nuove funzionalità, migliorando il codice esistente o correggendo bug. Pull requests sono benvenute!

## Autore

Marco Patierno