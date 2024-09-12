import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gCO2_per_kwh_nuclear = 3.7 # Source : Le Monde
gCO2_per_GWH_nuclear = gCO2_per_kwh_nuclear * 1e6
df_energy_produced = pd.read_csv("energy_produced.csv", sep=";", encoding='ISO-8859-1')  # Source : EDF
kgCO2_AR_Tokyo_Paris = 1.457e3     # Source : alterna énergie


print(df_energy_produced)



array_energy_produced = np.array(df_energy_produced)
# print(array_energy_produced)

# print(array_energy_produced[:,6])
nuclear_array = array_energy_produced[array_energy_produced[:,6]=="Nuclear"]
hydraulic_array = array_energy_produced[array_energy_produced[:,6]=="Hydraulic"]



plt.figure("Nuclear production vs years")
plt.plot(np.int16(nuclear_array[:,0]), np.int32(nuclear_array[:,7]))
plt.xlabel("Year")
plt.ylabel("Energy production [GWh]")
plt.show()


plt.plot(np.int16(nuclear_array[:,0]),gCO2_per_GWH_nuclear*np.int32(nuclear_array[:,7]) )
plt.xlabel("Year")
plt.ylabel("C02 of nuclear energy production")
plt.show()

plt.figure("Hydraulic production vs years")
plt.plot(np.int16(hydraulic_array[:,0]), np.int32(hydraulic_array[:,7]))
plt.xlabel("Year")
plt.ylabel("Energy production [GWh]")
plt.show()


plt.plot(np.int16(hydraulic_array[:,0]),gCO2_per_GWH_nuclear*np.int32(hydraulic_array[:,7]) )
plt.xlabel("Year")
plt.ylabel("C02 of nuclear energy production")
plt.show()





