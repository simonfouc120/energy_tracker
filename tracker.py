#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   @Date : September 2024
   @Author : Simon Foucambert - simon.fcbrt@gmail.fr
"""

from tracker_library import*

if __name__ == "__main__":
   years_nuclear, produced_energy_nuclear, years_hydraulic, produced_energy_hydraulic, years_thermical, produced_energy_thermical = load_array("various_energy_produced")

   city_centrale, combustible, installed_power = load_array("centrale_nuclear")

   centrale_rank(city_centrale, combustible, installed_power) 

   proportion_combustible(combustible, installed_power)
   # plot_energy_production_and_co2(years_nuclear, produced_energy_nuclear, years_hydraulic, produced_energy_hydraulic, years_thermical, produced_energy_thermical)
   years_consumption, energy_consumption, gaz_consumption = load_array("energy_consumption")
   
   plot_energy_consumption(years_consumption, energy_consumption, gaz_consumption)
   # calcul_equ_co2(produced_energy_nuclear)

