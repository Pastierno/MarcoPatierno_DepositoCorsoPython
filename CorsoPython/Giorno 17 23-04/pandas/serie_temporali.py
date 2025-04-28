import pandas as pd

date_range = pd.date_range(start='2023-01-01', periods=5, freq='M')

df = pd.DataFrame(date_range, columns=['Data'])

df["prev_day"] = df["Data"].shift(1)
df["next_day"] = df["Data"].shift(-1)
df["dailky_return"] = df["Data"].pct_change()

# rolling
df["rolling_mean7"] = df["Data"].rolling(window=7).mean()
df["rolling_std7"] = df["Data"].rolling(window=7).std()