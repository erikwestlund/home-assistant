import csv
from datetime import datetime

# Function to write data to a CSV file
def write_to_csv(data):
    # Path to the CSV file
    file_path = '/config/www/heat_dynamics_data_5m.csv'

    # Prepare the data to be written
    data_to_write = {
        'timestamp': data['timestamp'],
        'room': data['room'],
        'temp': data['temp'],
        'temp_change_5m': data['temp_change_5m'],
        'temp_change_15m': data['temp_change_15m'],
        'temp_change_60m': data['temp_change_60m'],
        'outdoor_temp_current': data['outdoor_temp_current'],
        'outdoor_temp_5m_ago': data['outdoor_temp_5m_ago'],
        'outdoor_temp_15m_ago': data['outdoor_temp_15m_ago'],
        'outdoor_temp_60m_ago': data['outdoor_temp_60m_ago'],
        'temp_5m_window': data['temp_5m_window'],
        'office_average_temp': data['office_average_temp'],
        'family_room_average_temp': data['family_room_average_temp'],
        'living_room_average_temp': data['living_room_average_temp'],
        'dining_room_temp': data['dining_room_temp'],
        'erik_office_temp': data['erik_office_temp'],
        'master_bedroom_average_temp': data['master_bedroom_average_temp'],
        'kids_bedrooms_average_temp': data['kids_bedrooms_average_temp'],
        'hank_bedroom_temp': data['hank_bedroom_temp'],
        'tilly_bedroom_temp': data['tilly_bedroom_temp'],
        'office_average_temperature_5m_ago': data['office_average_temperature_5m_ago'],
        'family_room_average_temperature_5m_ago': data['family_room_average_temperature_5m_ago'],
        'living_room_average_temperature_5m_ago': data['living_room_average_temperature_5m_ago'],
        'dining_room_temperature_5m_ago': data['dining_room_temperature_5m_ago'],
        'erik_office_temperature_5m_ago': data['erik_office_temperature_5m_ago'],
        'master_bedroom_average_temperature_5m_ago': data['master_bedroom_average_temperature_5m_ago'],
        'kids_rooms_average_temperature_5m_ago': data['kids_rooms_average_temperature_5m_ago'],
        'hank_room_temperature_5m_ago': data['hank_room_temperature_5m_ago'],
        'tilly_room_temperature_5m_ago': data['tilly_room_temperature_5m_ago'],
        'office_radiator_power_status': data['office_radiator_power_status'],
        'family_room_radiator_power_status': data['family_room_radiator_power_status'],
        'main_zone_radiator_power_status': data['main_zone_radiator_power_status'],
        'office_mini_split_power_status': data['office_mini_split_power_status'],
        'family_room_mini_split_power_status': data['family_room_mini_split_power_status'],
        'living_room_mini_split_power_status': data['living_room_mini_split_power_status'],
        'dining_room_mini_split_power_status': data['dining_room_mini_split_power_status'],
        'erik_office_mini_split_power_status': data['erik_office_mini_split_power_status'],
        'master_bedroom_mini_split_power_status': data['master_bedroom_mini_split_power_status'],
        'ducted_mini_split_power_status': data['ducted_mini_split_power_status'],
        'office_space_mini_split_heater_power_status': data['office_space_mini_split_heater_power_status'],
        'office_radiator_setpoint': data['office_radiator_setpoint'],
        'family_room_radiator_setpoint': data['family_room_radiator_setpoint'],
        'main_zone_radiator_setpoint': data['main_zone_radiator_setpoint'],
        'office_mini_split_setpoint': data['office_mini_split_setpoint'],
        'family_room_mini_split_setpoint': data['family_room_mini_split_setpoint'],
        'living_room_mini_split_setpoint': data['living_room_mini_split_setpoint'],
        'dining_room_mini_split_setpoint': data['dining_room_mini_split_setpoint'],
        'erik_office_mini_split_setpoint': data['erik_office_mini_split_setpoint'],
        'master_bedroom_mini_split_setpoint': data['master_bedroom_mini_split_setpoint'],
        'ducted_setpoint': data['ducted_setpoint'],
        'office_radiator_setpoint_5m_ago': data['office_radiator_setpoint_5m_ago'],
        'family_room_radiator_setpoint_5m_ago': data['family_room_radiator_setpoint_5m_ago'],
        'main_zone_radiator_setpoint_5m_ago': data['main_zone_radiator_setpoint_5m_ago'],
        'office_mini_split_setpoint_5m_ago': data['office_mini_split_setpoint_5m_ago'],
        'family_room_mini_split_setpoint_5m_ago': data['family_room_mini_split_setpoint_5m_ago'],
        'living_room_mini_split_setpoint_5m_ago': data['living_room_mini_split_setpoint_5m_ago'],
        'dining_room_mini_split_setpoint_5m_ago': data['dining_room_mini_split_setpoint_5m_ago'],
        'erik_office_mini_split_setpoint_5m_ago': data['erik_office_mini_split_setpoint_5m_ago'],
        'master_bedroom_mini_split_setpoint_5m_ago': data['master_bedroom_mini_split_setpoint_5m_ago'],
        'ducted_setpoint_5m_ago': data['ducted_setpoint_5m_ago']
    }

    # Check if the CSV file exists
    try:
        # Write to CSV (Append if file exists, otherwise create new)
        with open(file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data_to_write.keys())

            # Write header if file is empty (first run)
            if file.tell() == 0:
                writer.writeheader()

            # Write data
            writer.writerow(data_to_write)
    except Exception as e:
        logger.error(f"Error writing to CSV: {e}")

# Call the function with the data from the automation
write_to_csv(data)