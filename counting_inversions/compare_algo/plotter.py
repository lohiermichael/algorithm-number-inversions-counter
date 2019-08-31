import matplotlib.pyplot as plt
import pandas as pd

def algo_plotter(df_comparison: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 10))
    df_comparison.plot(kind='line', ax=ax)
    ax.set_xlabel(xlabel="List length")
    ax.set_ylabel(ylabel="Time")