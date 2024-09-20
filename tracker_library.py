import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file) : 
    if file == "various_energy_produced" : 
        df_energy_produced = pd.read_csv("energy_produced.csv", sep=";", encoding='ISO-8859-1')  # Source : EDF
    return df_energy_produced



def load_array(file): 
    if file == "various_energy_produced" : 
        df_energy_produced = load_data("various_energy_produced")
        
        array_energy_produced = np.array(df_energy_produced)

        nuclear_array = array_energy_produced[array_energy_produced[:,6]=="Nuclear"]
        years_nuclear = np.int16(nuclear_array[:,0])
        produced_energy_nuclear = np.int32(nuclear_array[:,7])

        hydraulic_array = array_energy_produced[array_energy_produced[:,6]=="Hydraulic"]
        years_hydraulic = np.int16(hydraulic_array[:,0])
        produced_energy_hydraulic = np.int32(hydraulic_array[:,7])

        thermical_array = array_energy_produced[array_energy_produced[:,6]=="Flame thermal"]
        years_thermical = np.int16(thermical_array[:,0])
        produced_energy_thermical = np.int32(thermical_array[:,7])
        return years_nuclear, produced_energy_nuclear, years_hydraulic, produced_energy_hydraulic, years_thermical, produced_energy_thermical
