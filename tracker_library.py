import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file) : 
    if file == "various_energy_produced" : 
        df_energy_produced = pd.read_csv("energy_produced.csv", sep=";", encoding='ISO-8859-1')  # Source : EDF
    return df_energy_produced
