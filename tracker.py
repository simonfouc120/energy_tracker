import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gCO2_per_kwh_nuclear = 3.7 # Source : Le Monde, EDF
gCO2_per_kwh_hydraulic = 6.0 # Source : alterna énergie
gCO2_per_GWH_nuclear = gCO2_per_kwh_nuclear * 1e6
gCO2_per_GWH_hydraulic = gCO2_per_kwh_hydraulic * 1e6


df_energy_produced = pd.read_csv("energy_produced.csv", sep=";", encoding='ISO-8859-1')  # Source : EDF
kgCO2_AR_Tokyo_Paris = 1.457e3 * 2     # Source : impact CO2 transport

gCO2_per_person_per_year = 8,9e6  # Source : statistique.developpement-durable.gouv.fr

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

plt.figure("Various energy production vs years")

plt.plot(years_nuclear, produced_energy_nuclear, marker='x', label = " nuclear")
plt.plot(years_hydraulic, produced_energy_hydraulic, marker='x', label = "hydraulic")
plt.plot(years_thermical ,produced_energy_thermical,marker ='x', label = "thermical")
plt.xlabel("Year")
plt.ylabel("Energy production [GWh]")
plt.legend()
plt.show()


 

print("Equivalent CO2 en nombre d'aller retour Paris - Tokyo pour une production maximale annuelle via le nucléaire : ",np.int32(np.max(produced_energy_nuclear)/kgCO2_AR_Tokyo_Paris*1e3))
print("Equivalent CO2 en nombre d'aller retour Paris - Tokyo pour une même production annuelle mais via le nucléaire : ",np.int32(np.max(produced_energy_nuclear)/kgCO2_AR_Tokyo_Paris*1e3))





plt.figure("Nuclear production vs years")
plt.plot(years_nuclear, produced_energy_nuclear)
plt.xlabel("Year")
plt.ylabel("Energy production [GWh]")
plt.show()


plt.figure("Date vs gCO2 for nuclear")
plt.plot(years_nuclear,gCO2_per_GWH_nuclear*produced_energy_nuclear)
plt.xlabel("Year")
plt.ylabel("C02 of nuclear energy production")
plt.show()

plt.figure("Hydraulic production vs years")
plt.plot(years_hydraulic, produced_energy_hydraulic)
plt.xlabel("Year")
plt.ylabel("Energy production [GWh]")
plt.show()

plt.figure("Date vs gCO2 for hydraulic")
plt.plot(years_hydraulic,gCO2_per_GWH_hydraulic*produced_energy_hydraulic )
plt.xlabel("Year")
plt.ylabel("C02 of nuclear energy production")
plt.show()



