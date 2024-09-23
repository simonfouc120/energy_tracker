#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   @Date : September 2024
   @Author : Simon Foucambert - simon.fcbrt@gmail.fr
"""

from tracker_library import*

years_nuclear, produced_energy_nuclear, years_hydraulic, produced_energy_hydraulic, years_thermical, produced_energy_thermical = load_array("various_energy_produced")

plot(years_nuclear, produced_energy_nuclear, years_hydraulic, produced_energy_hydraulic, years_thermical, produced_energy_thermical)

calcul_equ_co2(produced_energy_nuclear)


