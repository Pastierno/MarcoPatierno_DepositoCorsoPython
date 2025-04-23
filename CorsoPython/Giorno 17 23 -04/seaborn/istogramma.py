import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("penguins")

sns.histplot(data=data, x="flipper_length_mm", kde=True)
plt.title("Lunghezza della pinna dei pinguini")
plt.show()