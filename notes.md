# Notes

Various notes to ease creating configuration/automations.

## List of Thermostats

```
# LG ThingQ Mini Splits
climate.tinas_office_heat_pump
climate.dining_room_heat_pump
climate.family_room_heat_pump
climate.family_room_mini_split_hvac_unit
climate.living_room_heat_pump
climate.master_bedroom_heat_pump

# LG ThingQ Ducted System
climate.ducted_heat_pump

# Flair Puck-controlled Heat Pump
climate.eriks_office_room

# Ecobee Radiator Thermostats
climate.living_room_main_heating
climate.family_room_heating
climate.office
```

## List of General Settings

```
input_boolean.hvac_away_mode
input_number.heatpump_mode_threshold_offset
input_number.heatpump_overheated_threshold_offset
input_number.heatpump_cooling_default_setpoint
input_number.heatpumps_away_setpoint
input_number.radiators_away_setpoint

```

## Binary Sensors:

```aiignore

binary_sensor.daytime_status
binary_sensor.ducted_rooms_occupied
binary_sensor.office_occupancy_detected
binary_sensor.office_occupied
binary_sensor.family_room_occupancy_detected
binary_sensor.family_room_occupied
binary_sensor.living_room_occupancy_detected
binary_sensor.living_room_occupied
binary_sensor.dining_room_occupancy_detected
binary_sensor.dining_room_occupied
binary_sensor.master_bedroom_occupancy_detected
binary_sensor.master_bedroom_occupied
binary_sensor.tilly_s_room_occupancy_detected
binary_sensor.tilly_s_room_occupied
binary_sensor.hank_s_room_occupancy_detected
binary_sensor.hank_s_room_occupied
```