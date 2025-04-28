import seaborn as sns
import matplotlib.pyplot as plt

fmri = sns.load_dataset("fmri")

sns.lineplot(x="timepoint", y="signal", hue="region", style="event", data=fmri)
plt.title("Segnale in funzione del tempo")
plt.show()