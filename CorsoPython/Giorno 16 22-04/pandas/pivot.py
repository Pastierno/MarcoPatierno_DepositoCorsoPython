import pandas as pd

data = {
    "Data" : ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06", "2023-01-07", "2023-01-08"],
    "Città" : ["Milano", "Roma", "Milano", "Roma", "Milano", "Roma", "Milano", "Roma"],
    "Prodotto" : ["Mouse", "Tastiera", "Monitor", "Mouse", "Tastiera", "Monitor", "Mouse", "Tastiera"],
    "Vendite" : [100, 150, 200, 300, 250, 400, 350, 450],
    
}

df = pd.DataFrame(data)

pivot_df = df.pivot_table(values="Vendite", index=["Prodotto"], columns=["Città"], aggfunc="mean")

print(pivot_df)
#grouped_df = df.groupby("Prodotto").sum()
grouped_df = df.groupby(["Prodotto", "Città"]).sum().reset_index()
print(grouped_df)