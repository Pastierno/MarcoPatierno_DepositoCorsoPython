import pandas as pd


class StatisticalAnalyzer:
    """
    Classe per l'analisi statistica di un DataFrame pandas.
    Include metodi per calcolare media, mediana, deviazione standard,
    varianza, min/max, correlazioni, asimmetria, curtosi, quartili e altro.
    """
    
    def __init__(self, df: pd.DataFrame):
        """
        Inizializza l'oggetto con un DataFrame.
        Tiene solo le colonne numeriche per le analisi statistiche.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Il dato deve essere un DataFrame pandas.")
        self.df = df.select_dtypes(include='number')  # Mantiene solo colonne numeriche

    def mean(self):
        """Restituisce la media aritmetica di ciascuna colonna numerica."""
        return self.df.mean()

    def median(self):
        """Restituisce la mediana di ciascuna colonna numerica."""
        return self.df.median()

    def std_dev(self):
        """Restituisce la deviazione standard di ciascuna colonna numerica."""
        return self.df.std()

    def variance(self):
        """Restituisce la varianza di ciascuna colonna numerica."""
        return self.df.var()

    def min_value(self):
        """Restituisce il valore minimo di ciascuna colonna numerica."""
        return self.df.min()

    def max_value(self):
        """Restituisce il valore massimo di ciascuna colonna numerica."""
        return self.df.max()

    def correlation(self):
        """Restituisce la matrice di correlazione tra le colonne numeriche."""
        return self.df.corr()

    def covariance(self):
        """Restituisce la matrice di covarianza tra le colonne numeriche."""
        return self.df.cov()

    def skewness(self):
        """Restituisce l'asimmetria (skewness) della distribuzione dei dati."""
        return self.df.skew()
    
    def kurtosis(self):
        """Restituisce la curtosi della distribuzione dei dati."""
        return self.df.kurt()
    
    def quartiles(self):
        """
        Calcola i quartili Q1, Q2 (mediana) e Q3 per ogni colonna numerica.
        Restituisce un DataFrame con questi valori.
        """
        q1 = self.df.quantile(0.25)
        q2 = self.df.quantile(0.50)  # Mediana
        q3 = self.df.quantile(0.75)
        return pd.DataFrame({'Q1': q1, 'Q2': q2, 'Q3': q3})
    
    def iqr(self):
        """
        Calcola l'intervallo interquartile (IQR = Q3 - Q1) per ogni colonna numerica.
        Utile per identificare gli outlier.
        """
        q1 = self.df.quantile(0.25)
        q3 = self.df.quantile(0.75)
        return q3 - q1
    
    def distribution_summary(self):
        """
        Restituisce un DataFrame riassuntivo con le principali statistiche descrittive:
        - media, mediana, deviazione standard, skewness, kurtosis
        - Q1, Q3 e IQR
        """
        return pd.DataFrame({
            'mean': self.mean(),
            'median': self.median(),
            'std_dev': self.std_dev(),
            'skewness': self.skewness(),
            'kurtosis': self.kurtosis(),
            'Q1': self.quartiles()['Q1'],
            'Q3': self.quartiles()['Q3'],
            'IQR': self.iqr()
        })
