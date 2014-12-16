heatsource_version_Boku
=======================

### Heat Source

This is a fork of the Heat Source computer model used by Oregon DEQ to simulate stream thermodynamics and hydraulics.



### 13/12/2014 v 001
Hydrological velocity as input file: configuration in the HeatSource_Control.csv
* HYDROLOGICAL VELOCITY FILE(m/s)
* HYDROLOGICAL VELOCITY FILE USED (TRUE/FALSE)

changed: each node has a "hydro_vel" "hydro_used" attribute
* hydro_vel: Hydrological velocity of the current node
* hydro_used: Characterizes if hydrological is imported from file
if hydro_used is set different methods from PyHeatsource.py are used
