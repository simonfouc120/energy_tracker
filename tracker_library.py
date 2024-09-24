import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


GCO2_PER_KWH_NUCLEAR = 3.7 # Source : Le Monde, EDF
GCO2_PER_KWH_HYDRAULIC = 6.0 # Source : alterna énergie
GCO2_PER_GWH_NUCLEAR = GCO2_PER_KWH_NUCLEAR * 1e6
GCO2_PER_GWH_HYDRAULIC = GCO2_PER_KWH_HYDRAULIC * 1e6

GCO2_PER_KWH_THERMICAL = 500   # Source : climate.selectra.com      # A modif faire meilleure approx 
GCO2_PER_GWH_THERMICAL = GCO2_PER_KWH_THERMICAL * 1e6

KGCO2_AR_TOKYO_PARIS = 1.457e3 * 2     # Source : impact CO2 transport
GCO2_PER_PERSON_YR = 8,9e6  # Source : statistique.developpement-durable.gouv.fr



def load_data(file) : 
    if file == "various_energy_produced" : 
        df_energy_produced = pd.read_csv("energy_produced.csv", sep=";", encoding='ISO-8859-1')  # Source : EDF
        return df_energy_produced

    if file == "centrale_nuclear" :
        df_nuclear_centrales = pd.read_csv("centrales-de-production-nucleaire-edf.csv", sep=";", encoding='ISO-8859-1')  # Source : EDF
        return df_nuclear_centrales



def load_array(file): ### A MODIF
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
    if file == "centrale_nuclear" : 
        df_nuclear_centrales = load_data("centrale_nuclear")
        array_nuclear_centrale = np.array(df_nuclear_centrales)
        city_centrale = array_nuclear_centrale[1:,6]
        installed_power = array_nuclear_centrale[1:,14]
        unique_pairs = list(set(zip(city_centrale, installed_power)))
        city_centrale, installed_power = zip(*unique_pairs)
        city_centrale = np.array(city_centrale)
        installed_power = np.array(installed_power)
        sorted_city_centrale = city_centrale[np.argsort(-installed_power)]
        sorted_installed_power = installed_power[np.argsort(-installed_power)]
        
        ### Ajout combustible
        
        return sorted_city_centrale, sorted_installed_power

def centrale_rank(city_centrale, installed_power) :
    print("Classement des centrales par puissance installée :")
    for i, (city, power) in enumerate(zip(city_centrale, installed_power), 1):
        print(f"{i}. Centrale: {city}, Puissance installée: {power} MW")

def plot(years_nuclear, produced_energy_nuclear, years_hydraulic, produced_energy_hydraulic, years_thermical, produced_energy_thermical):
    plt.figure("Various energy production vs years")
    plt.plot(years_nuclear, produced_energy_nuclear, marker='x', label = " nuclear")
    plt.plot(years_hydraulic, produced_energy_hydraulic, marker='x', label = "hydraulic")
    plt.plot(years_thermical ,produced_energy_thermical,marker ='x', label = "thermical")
    plt.xlabel("Year")
    plt.ylabel("Energy production [GWh]")
    plt.legend()
    plt.show()

    plt.figure("Various energy CO2 vs years")
    plt.plot(years_nuclear, produced_energy_nuclear*GCO2_PER_GWH_NUCLEAR, marker='x', label = " nuclear")
    plt.plot(years_hydraulic, produced_energy_hydraulic*GCO2_PER_GWH_HYDRAULIC, marker='x', label = "hydraulic")
    plt.plot(years_thermical ,produced_energy_thermical*GCO2_PER_GWH_THERMICAL,marker ='x', label = "thermical")
    plt.xlabel("Year")
    plt.ylabel("gCO2 eq")
    plt.legend()
    plt.show()


def calcul_equ_co2(produced_energy_nuclear) :
    print("Equivalent CO2 en nombre d'aller retour Paris - Tokyo pour une production maximale annuelle via le nucléaire : ",  np.int64((np.max(produced_energy_nuclear)*GCO2_PER_GWH_NUCLEAR)/(KGCO2_AR_TOKYO_PARIS*1e3)))
    print("Equivalent CO2 en nombre d'aller retour Paris - Tokyo pour une même production annuelle mais via le thermique : ", np.int64((np.max(produced_energy_nuclear)*GCO2_PER_GWH_THERMICAL)/(KGCO2_AR_TOKYO_PARIS*1e3)))


# plt.figure("Nuclear production vs years")
# plt.plot(years_nuclear, produced_energy_nuclear)
# plt.xlabel("Year")
# plt.ylabel("Energy production [GWh]")
# plt.show()


# plt.figure("Date vs gCO2 for nuclear")
# plt.plot(years_nuclear,gCO2_per_GWH_nuclear*produced_energy_nuclear)
# plt.xlabel("Year")
# plt.ylabel("C02 of nuclear energy production")
# plt.show()

# plt.figure("Hydraulic production vs years")
# plt.plot(years_hydraulic, produced_energy_hydraulic)
# plt.xlabel("Year")
# plt.ylabel("Energy production [GWh]")
# plt.show()

# plt.figure("Date vs gCO2 for hydraulic")
# plt.plot(years_hydraulic,gCO2_per_GWH_hydraulic*produced_energy_hydraulic )
# plt.xlabel("Year")
# plt.ylabel("C02 of nuclear energy production")
# plt.show()
