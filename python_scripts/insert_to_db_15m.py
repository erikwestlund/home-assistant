import sqlite3
from datetime import datetime

# Function to connect to the SQLite database and insert data
def insert_to_db(data):
    # Database file
    db_file = '/config/heat_dynamics.db'

    # Connect to SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Prepare SQL Insert query
    query = """
    INSERT INTO heat_data (
        timestamp, room, temp, temp_change_15m, temp_change_115m, temp_change_60m,
        outdoor_temp_current, outdoor_temp_15m_ago, outdoor_temp_115m_ago, outdoor_temp_60m_ago,
        temp_15m_window, office_average_temp, family_room_average_temp, living_room_average_temp,
        dining_room_temp, erik_office_temp, master_bedroom_average_temp, kids_bedrooms_average_temp,
        hank_bedroom_temp, tilly_bedroom_temp, office_average_temperature_15m_ago, 
        family_room_average_temperature_15m_ago, living_room_average_temperature_15m_ago, 
        dining_room_temperature_15m_ago, erik_office_temperature_15m_ago, 
        master_bedroom_average_temperature_15m_ago, kids_rooms_average_temperature_15m_ago,
        hank_room_temperature_15m_ago, tilly_room_temperature_15m_ago, office_radiator_power_status,
        family_room_radiator_power_status, main_zone_radiator_power_status, office_mini_split_power_status,
        family_room_mini_split_power_status, living_room_mini_split_power_status, dining_room_mini_split_power_status,
        erik_office_mini_split_power_status, master_bedroom_mini_split_power_status, ducted_mini_split_power_status,
        office_space_mini_split_heater_power_status, office_radiator_setpoint, family_room_radiator_setpoint,
        main_zone_radiator_setpoint, office_mini_split_setpoint, family_room_mini_split_setpoint,
        living_room_mini_split_setpoint, dining_room_mini_split_setpoint, erik_office_mini_split_setpoint,
        master_bedroom_mini_split_setpoint, ducted_setpoint, office_radiator_setpoint_15m_ago,
        family_room_radiator_setpoint_15m_ago, main_zone_radiator_setpoint_15m_ago, office_mini_split_setpoint_15m_ago,
        family_room_mini_split_setpoint_15m_ago, living_room_mini_split_setpoint_15m_ago,
        dining_room_mini_split_setpoint_15m_ago, erik_office_mini_split_setpoint_15m_ago,
        master_bedroom_mini_split_setpoint_15m_ago, ducted_setpoint_15m_ago)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    # Gather data from the automation
    cursor.execute(query, (
        data['timestamp'],
        data['room'],
        data['temp'],
        data['temp_change_15m'],
        data['temp_change_115m'],
        data['temp_change_60m'],
        data['outdoor_temp_current'],
        data['outdoor_temp_15m_ago'],
        data['outdoor_temp_115m_ago'],
        data['outdoor_temp_60m_ago'],
        data['temp_15m_window'],
        data['office_average_temp'],
        data['family_room_average_temp'],
        data['living_room_average_temp'],
        data['dining_room_temp'],
        data['erik_office_temp'],
        data['master_bedroom_average_temp'],
        data['kids_bedrooms_average_temp'],
        data['hank_bedroom_temp'],
        data['tilly_bedroom_temp'],
        data['office_average_temperature_15m_ago'],
        data['family_room_average_temperature_15m_ago'],
        data['living_room_average_temperature_15m_ago'],
        data['dining_room_temperature_15m_ago'],
        data['erik_office_temperature_15m_ago'],
        data['master_bedroom_average_temperature_15m_ago'],
        data['kids_rooms_average_temperature_15m_ago'],
        data['hank_room_temperature_15m_ago'],
        data['tilly_room_temperature_15m_ago'],
        data['office_radiator_power_status'],
        data['family_room_radiator_power_status'],
        data['main_zone_radiator_power_status'],
        data['office_mini_split_power_status'],
        data['family_room_mini_split_power_status'],
        data['living_room_mini_split_power_status'],
        data['dining_room_mini_split_power_status'],
        data['erik_office_mini_split_power_status'],
        data['master_bedroom_mini_split_power_status'],
        data['ducted_mini_split_power_status'],
        data['office_space_mini_split_heater_power_status'],
        data['office_radiator_setpoint'],
        data['family_room_radiator_setpoint'],
        data['main_zone_radiator_setpoint'],
        data['office_mini_split_setpoint'],
        data['family_room_mini_split_setpoint'],
        data['living_room_mini_split_setpoint'],
        data['dining_room_mini_split_setpoint'],
        data['erik_office_mini_split_setpoint'],
        data['master_bedroom_mini_split_setpoint'],
        data['ducted_setpoint'],
        data['office_radiator_setpoint_15m_ago'],
        data['family_room_radiator_setpoint_15m_ago'],
        data['main_zone_radiator_setpoint_15m_ago'],
        data['office_mini_split_setpoint_15m_ago'],
        data['family_room_mini_split_setpoint_15m_ago'],
        data['living_room_mini_split_setpoint_15m_ago'],
        data['dining_room_mini_split_setpoint_15m_ago'],
        data['erik_office_mini_split_setpoint_15m_ago'],
        data['master_bedroom_mini_split_setpoint_15m_ago'],
        data['ducted_setpoint_15m_ago']
    ))

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()

# Call the function with the data from the automation
insert_to_db(data)