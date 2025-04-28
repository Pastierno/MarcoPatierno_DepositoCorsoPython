# Analisi Dati Clienti

## Descrizione del Progetto
Questo esercizio è pensato per guidarti passo dopo passo nell’analisi di un dataset di clienti. Scoprirai come caricare, esplorare, pulire e arricchire i dati, fino ad applicare tecniche statistiche e di machine learning come ANOVA, chi-quadrato, regressione logistica e clustering K-Means. Il tutto implementato in un pratico script Python con menu interattivo.

> **Suggerimento:** Segui l’ordine delle operazioni suggerito dal menu. Ogni fase si basa sui risultati di quella precedente!

---

## Struttura del Progetto

```
├── main.py           # Script principale con menu interattivo
└── clienti.csv       # Dataset di esempio dei clienti
```  

- **main.py**: Contiene funzioni modulari per ogni fase dell’analisi (caricamento, esplorazione, pulizia, feature engineering, analisi statistica, machine learning, esportazione).  
- **clienti.csv**: File CSV con le colonne essenziali (`ETA`, `TARIFFA_MENSILE`, `DATI_CONSUMATI`, eventuale colonna `CHURN`).

---

## Requisiti

- Python 3.7 o superiore
- Librerie Python:
  - pandas
  - numpy
  - scipy
  - matplotlib
  - seaborn
  - scikit-learn
  - statsmodels
  - kneed

Puoi installarle tutte con:
```bash
pip install pandas numpy scipy matplotlib seaborn scikit-learn statsmodels kneed
```

---

## Installazione e Avvio

1. **Clona o scarica** la cartella del progetto.  
2. Assicurati di avere `clienti.csv` nella stessa directory di `main.py`.  
3. Apri un terminale e posizionati nella cartella del progetto.  
4. Esegui:
   ```bash
   python main.py
   ```  
5. Segui le istruzioni a schermo: seleziona l’opzione desiderata dal menu numerato.

> **Nota:** Se il file `clienti.csv` non viene trovato, verranno provati percorsi alternativi. In caso di problemi, inserisci manualmente il percorso quando richiesto.

---

## Descrizione delle Funzioni

1. **load_data(file_path)**  
   - Carica il dataset da CSV.  
   - Verifica esistenza del file e colonne essenziali (`ETA`, `TARIFFA_MENSILE`, `DATI_CONSUMATI`).

2. **display_data(df, rows=5)**  
   - Mostra le prime righe e l’elenco delle colonne.  
   - Visualizza dimensioni del DataFrame.

3. **descriptive_analysis(df)**  
   - Statistiche descrittive: media, mediana, quartili.  
   - Informazioni su tipi di dato e valori nulli.  
   - Distribuzione di variabili categoriche con grafici a barre.

4. **clean_data(df)**  
   - Filtra età tra 18 e 80 anni.  
   - Imputa valori nulli (mediana per numeriche, moda per categoriche).  
   - Rimuove outlier basati sull’IQR per `TARIFFA_MENSILE` e `DATI_CONSUMATI`.

5. **create_features(df)**  
   - Crea nuove colonne:  
     - `COSTO_PER_GB` (costo mensile diviso dati consumati).  
     - `ETA_GRUPPO` (fasce d’età).  
     - `UTILIZZO_MEDIO` (media consumo per fascia).  
     - `CONSUMO_CATEGORIA` (classi Basso/Medio/Alto).  
     - `TARIFFA_CATEGORIA` (Economica/Media/Premium).  
     - `RAPPORTO_ETA_CONSUMO`.
   - Standardizza la colonna `CHURN` (SI/NO) se presente.

6. **correlation_analysis(df)**  
   - Calcola e stampa la matrice di correlazione per variabili numeriche.  
   - Heatmap con seaborn e segnalazione di correlazioni > |0.5|.

7. **anova_test(df)**  
   - ANOVA per confrontare `DATI_CONSUMATI` tra fasce d’età (`ETA_GRUPPO`).  
   - Se p < 0.05, esegue test post-hoc di Tukey.  
   - Grafici boxplot e violin plot per visualizzare le differenze.

8. **chi_square_test(df)**  
   - Test del chi-quadrato tra `ETA_GRUPPO` e `CONSUMO_CATEGORIA`.  
   - Stampa tabella di contingenza e percentuali.  
   - Verifica residui standardizzati per individuare associazioni significative.  
   - Grafici stacked bar e mosaic.

9. **logistic_regression(df)**  
   - Previsioni di churn con regressione logistica.  
   - Selezione manuale delle feature numeriche, standardizzazione e imputazione.  
   - Ricerca dell’iperparametro C ottimale tramite cross-validation.  
   - Metriche di performance: accuratezza, ROC AUC, matrice di confusione, report di classificazione.  
   - Grafici di importanza feature e curva ROC.

10. **clustering_kmeans(df)**  
    - Segmentazione clienti con K-Means.  
    - Scelta delle feature, determinazione di k ottimale (metodo del gomito e silhouette).  
    - Analisi e visualizzazione dei cluster (2D, 3D, PCA).  
    - Interpretazione delle caratteristiche distintive di ogni cluster.

11. **export_data(df)**  
    - Esporta il DataFrame in CSV, Excel, JSON o Pickle.  
    - Mostra dimensione del file generato.

12. **clear_screen()**  
    - Pulisce il terminale per un’interfaccia più pulita.

13. **main()**  
    - Menu interattivo per eseguire tutte le fasi descritte.

---

## Consigli Utili

- **Ordine consigliato:**  
  1. Carica i dati  
  2. Analisi descrittiva  
  3. Pulizia dati  
  4. Creazione features  
  5. Analisi correlazioni e test statistici  
  6. Machine learning (regressione, clustering)  
  7. Esporta i risultati

- **Sperimenta** modificando soglie di pulizia o scegliendo diverse feature per capire l’impatto sui risultati.  
- **Approfondisci** i grafici generati per cogliere pattern nascosti e presentare insight significativi.

---

Buon lavoro con l’analisi dei dati! 🚀

