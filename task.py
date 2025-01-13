import pandas as pd
import numpy as np

file_path = "D:/ML Internship/cleaned_data.csv"  
data = pd.read_csv(file_path)

data = data.drop_duplicates()

columns_to_drop = [
    'distance', 'o_s1_b1_voltage', 'commanded_exhaust_gas_recirculation',
    'commanded_throttle_actuator', 'fuel_rail_pressure', 'fuel_tank_level_input',
    'fuel_air_commanded_equivalence_ratio', 'hybrid_battery_pack_remaining',
    'intake_manifold_absolute_pressure', 'egr_error'
]

existing_columns_to_drop = [col for col in columns_to_drop if col in data.columns]
data_cleaned = data.drop(columns=existing_columns_to_drop)

data_cleaned.fillna(0, inplace=True)
data_cleaned['time_stamp'] = pd.to_datetime(data_cleaned['time_stamp'])
data_cleaned = data_cleaned.sort_values(by='time_stamp')

data_cleaned = data_cleaned[(data_cleaned['latitude'].between(-90, 90)) & 
                            (data_cleaned['longitude'].between(-180, 180))]

data_cleaned['time_difference'] = data_cleaned['time_stamp'].diff().dt.total_seconds().fillna(0) / 3600

data_cleaned['distance_traveled'] = data_cleaned['vehicle_speed'] * data_cleaned['time_difference']
data_cleaned['distance_traveled'] = data_cleaned['distance_traveled'].fillna(0)  # Fill NaNs with 0
data_cleaned['cumulative_distance'] = data_cleaned['distance_traveled'].cumsum()

data_cleaned['driving_time_hours'] = data_cleaned['time_difference'].cumsum()

avg_speed = data_cleaned['vehicle_speed'].mean()
max_speed = data_cleaned['vehicle_speed'].max()
total_distance = data_cleaned['cumulative_distance'].iloc[-1]

data_cleaned['fuel_consumption'] = (data_cleaned['distance_traveled'] / 100) * 8
total_fuel_consumption = data_cleaned['fuel_consumption'].sum()


mileage = total_distance / total_fuel_consumption if total_fuel_consumption > 0 else 0


avg_coolant_temp = data_cleaned['engine_coolant_temperature'].mean()
overheat_temp = data_cleaned['engine_coolant_temperature'].max()
max_temp_index = data_cleaned['engine_coolant_temperature'].idxmax()
time_to_max_temp = (
    data_cleaned['time_stamp'].iloc[max_temp_index] - data_cleaned['time_stamp'].iloc[0]
).total_seconds() / 60  # Convert to minutes


high_rpm_threshold = 4000  # Example threshold for high RPM
high_rpm_periods = data_cleaned[data_cleaned['engine_rpm'] > high_rpm_threshold]
high_rpm_count = len(high_rpm_periods)


if {'intake_air_temperature', 'ambient_air_temperature'}.issubset(data_cleaned.columns):
    data_cleaned['temperature_diff'] = (data_cleaned['intake_air_temperature'] - 
                                        data_cleaned['ambient_air_temperature'])
    avg_temp_diff = data_cleaned['temperature_diff'].mean()
else:
    avg_temp_diff = "Temperature columns not available"

results = {
    "Average Speed (km/h)": avg_speed,
    "Max Speed (km/h)": max_speed,
    "Driving Time (hours)": data_cleaned['driving_time_hours'].iloc[-1],
    "Total Distance Traveled (km)": total_distance,
    "Total Fuel Consumption (liters)": total_fuel_consumption,
    "Mileage (km/liter)": mileage,
    "Average Coolant Temperature (°C)": avg_coolant_temp,
    "Overheat Temperature (°C)": overheat_temp,
    "Time to Max Temperature (minutes)": time_to_max_temp,
    "High RPM Periods Count": high_rpm_count,
    "Average Temperature Difference (Intake vs Ambient)": avg_temp_diff
}


print("Analysis Results:")
for key, value in results.items():
    print(f"{key}: {value}")

output_path = "D:/ML Internship/cleaned_data.csv" 
data_cleaned.to_csv(output_path, index=False)