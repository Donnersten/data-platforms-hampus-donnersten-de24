import pandas as pd
import seaborn as sns
from pathlib import Path

data_path = Path(__file__).parent

df = pd.read_csv(data_path / "athlete_events.csv")
print(df.head())


plot = sns.barplot(df, x="Sex", y="Age")

fig = plot.get_figure()
fig.savefig(data_path/"output.png")