##
## September 2024
## Simon Foucambert - simon.fcbrt@gmail.fr
##

from tracker_library import*

years_nuclear, produced_energy_nuclear, years_hydraulic, produced_energy_hydraulic, years_thermical, produced_energy_thermical = load_array("various_energy_produced")

print("Equivalent CO2 en nombre d'aller retour Paris - Tokyo pour une production maximale annuelle via le nucléaire : ",  np.int64((np.max(produced_energy_nuclear)*GCO2_PER_GWH_NUCLEAR)/(KGCO2_AR_TOKYO_PARIS*1e3)))
print("Equivalent CO2 en nombre d'aller retour Paris - Tokyo pour une même production annuelle mais via le thermique : ", np.int64((np.max(produced_energy_nuclear)*GCO2_PER_GWH_THERMICAL)/(KGCO2_AR_TOKYO_PARIS*1e3)))

plot(years_nuclear, produced_energy_nuclear, years_hydraulic, produced_energy_hydraulic, years_thermical, produced_energy_thermical)

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



