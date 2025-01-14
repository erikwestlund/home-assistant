def log_to_csv(data):
    # Path to the CSV file
    csv_file = '/config/www/heat_dynamics_data_log.csv'

    # Prepare the data in CSV format (comma-separated values)
    data_to_log = f"{data['timestamp']},{data['room']},{data['temp']},{data['temp_change_5m']}," \
                  f"{data['temp_change_15m']},{data['temp_change_60m']},{data['outdoor_temp_current']}," \
                  f"{data['outdoor_temp_5m_ago']},{data['outdoor_temp_15m_ago']},{data['outdoor_temp_60m_ago']}," \
                  f"{data['temp_5m_window']},{data['office_average_temp']},{data['family_room_average_temp']}," \
                  f"{data['living_room_average_temp']},{data['dining_room_temp']},{data['erik_office_temp']}," \
                  f"{data['master_bedroom_average_temp']},{data['kids_bedrooms_average_temp']}," \
                  f"{data['hank_bedroom_temp']},{data['tilly_bedroom_temp']},{data['office_average_temperature_5m_ago']}," \
                  f"{data['family_room_average_temperature_5m_ago']},{data['living_room_average_temperature_5m_ago']}," \
                  f"{data['dining_room_temperature_5m_ago']},{data['erik_office_temperature_5m_ago']}," \
                  f"{data['master_bedroom_average_temperature_5m_ago']},{data['kids_rooms_average_temperature_5m_ago']}," \
                  f"{data['hank_room_temperature_5m_ago']},{data['tilly_room_temperature_5m_ago']}," \
                  f"{data['office_radiator_power_status']},{data['family_room_radiator_power_status']}," \
                  f"{data['main_zone_radiator_power_status']},{data['office_mini_split_power_status']}," \
                  f"{data['family_room_mini_split_power_status']},{data['living_room_mini_split_power_status']}," \
                  f"{data['dining_room_mini_split_power_status']},{data['erik_office_mini_split_power_status']}," \
                  f"{data['master_bedroom_mini_split_power_status']},{data['ducted_mini_split_power_status']}," \
                  f"{data['office_space_mini_split_heater_power_status']},{data['office_radiator_setpoint']}," \
                  f"{data['family_room_radiator_setpoint']},{data['main_zone_radiator_setpoint']}," \
                  f"{data['office_mini_split_setpoint']},{data['family_room_mini_split_setpoint']}," \
                  f"{data['living_room_mini_split_setpoint']},{data['dining_room_mini_split_setpoint']}," \
                  f"{data['erik_office_mini_split_setpoint']},{data['master_bedroom_mini_split_setpoint']}," \
                  f"{data['ducted_setpoint']},{data['office_radiator_setpoint_5m_ago']},{data['family_room_radiator_setpoint_5m_ago']}," \
                  f"{data['main_zone_radiator_setpoint_5m_ago']},{data['office_mini_split_setpoint_5m_ago']}," \
                  f"{data['family_room_mini_split_setpoint_5m_ago']},{data['living_room_mini_split_setpoint_5m_ago']}," \
                  f"{data['dining_room_mini_split_setpoint_5m_ago']},{data['erik_office_mini_split_setpoint_5m_ago']}," \
                  f"{data['master_bedroom_mini_split_setpoint_5m_ago']},{data['ducted_setpoint_5m_ago']}\n"

    # Open the file in append mode and write the data
    try:
        with open(csv_file, mode='a') as file:
            file.write(data_to_log)
    except Exception as e:
        logger.error(f"Error writing to CSV file: {e}")