# Sistema di Gestione Vendite e Analisi Statistica con MySQL e NumPy

## Descrizione
Questo progetto implementa un sistema di gestione vendite completo con database relazionale MySQL e analisi statistica usando NumPy. L'applicazione permette di generare dati casuali significativi, gestire relazioni tra clienti, prodotti e vendite, ed eseguire analisi statistiche sui dati generati.

## Caratteristiche principali
- Generazione randomizzata di clienti
- Creazione di prodotti con prezzi uniformemente distribuiti
- Simulazione di vendite con date spalmate su un periodo di un anno
- Analisi statistica avanzata (media, varianza, deviazione standard, min, max)
- Interfaccia interattiva a riga di comando

## Requisiti
- Python 3.6+
- MySQL Server
- Librerie Python:
  - numpy
  - mysql-connector-python
  - datetime

## Installazione
1. Clona o scarica il repository
2. Installa le dipendenze necessarie:
```bash
pip install numpy mysql-connector-python
```
3. Configura MySQL con:
   - Host: localhost
   - User: root
   - Password: (vuota)
4. Esegui lo script principale:
```bash
python esercizio.py
```

## Struttura del database
Il sistema crea automaticamente un database `vendite` con tre tabelle:

### clienti
- `id_cliente` (PK)
- `nome` - Nome del cliente
- `eta` - Età del cliente
- `regione` - Regione di provenienza

### prodotti
- `id_prodotto` (PK)
- `nome` - Nome del prodotto
- `prezzo` - Prezzo unitario
- `categoria` - Categoria di appartenenza

### vendite
- `id_vendita` (PK)
- `id_cliente` (FK)
- `id_prodotto` (FK)
- `quantita` - Quantità acquistata
- `prezzo_totale` - Prezzo totale della vendita
- `data_vendita` - Data dell'acquisto

## Funzionalità

### 1. Generazione clienti
Genera un numero specificato di clienti con:
- Nomi selezionati casualmente da una lista predefinita
- Età distribuite tra 18 e 80 anni usando numpy.randint
- Regione selezionata casualmente da una lista predefinita

### 2. Generazione prodotti
Crea prodotti con:
- Nomi incrementali per tipologia (es. "Laptop 1", "Laptop 2", "Mouse 1")
- Prezzi distribuiti uniformemente tra un minimo e un massimo usando numpy.linspace
- Categorie assegnate casualmente

### 3. Generazione vendite
Simula vendite con:
- Clienti e prodotti selezionati casualmente dal database
- Quantità tra 1 e 10 utilizzando numpy.randint
- Date distribuite uniformemente negli ultimi 365 giorni usando numpy.arange
- Calcolo automatico del prezzo totale

### 4. Calcoli statistici
Permette di eseguire diverse operazioni statistiche:
- Media
- Varianza
- Deviazione standard
- Minimo
- Massimo

Su diverse tabelle e colonne a scelta dell'utente.

### 5. Gestione stati (implementazione didattica)
Questa funzionalità è stata implementata principalmente come esempio didattico per dimostrare tecniche di alterazione di tabelle esistenti e implementazione di relazioni in un database MySQL:

- **Creazione tabella stati**: Creazione di una tabella ausiliaria contenente nomi di stati/nazioni
- **Modifica di tabelle esistenti**: Aggiunta di campi `id_stato` con vincoli di chiave esterna a tabelle già popolate
- **Criteri di assegnazione diversificati** per ogni tabella:
  - Per **clienti**: casuale, per regione geografica, o per fascia d'età
  - Per **prodotti**: casuale, per categoria merceologica, o per fascia di prezzo
  - Per **vendite**: casuale, cronologica, per importo, o ereditata dal cliente

#### Aspetti didattici della funzionalità
Questa implementazione non è tanto finalizzata all'utilità pratica quanto a dimostrare:

1. **Alterazione di schema DB**: utilizzo di `ALTER TABLE` per modificare tabelle esistenti
2. **Normalizzazione**: separazione dei dati in tabelle relazionate per minimizzare la ridondanza
3. **Vincoli di integrità referenziale**: implementazione di `FOREIGN KEY` per mantenere coerenza tra tabelle
4. **Query complesse**: utilizzo di `JOIN` e `UPDATE` condizionali
5. **Gestione delle eccezioni**: verifica dell'esistenza di colonne prima di tentare modifiche
6. **Algoritmi di distribuzione**: metodi di mapping tra insiemi di dati basati su criteri specifici

Questa sezione del progetto è particolarmente utile per comprendere come modificare lo schema di un database in produzione senza perdere i dati esistenti, un'operazione comune in scenari reali di sviluppo e manutenzione di database.

## Esempio di utilizzo
1. Genera 100 clienti casuali
2. Crea 50 prodotti con prezzi tra €10 e €500
3. Genera 200 vendite distribuite nell'ultimo anno
4. Calcola la media dei prezzi totali delle vendite
5. Analizza la varianza dei prezzi dei prodotti
6. Trova l'età minima e massima dei clienti

## Note implementative
- Utilizzo di NumPy per generazione di dati statisticamente significativi
- Implementazione di foreign keys per mantenere l'integrità referenziale
- Formattazione appropriata dell'output (valori monetari vs. numerici)
- Gestione degli errori e validazione dell'input

