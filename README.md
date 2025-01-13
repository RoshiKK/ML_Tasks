Average Speed (km/h):
The average of all speed values recorded.
Average Speed = ∑ vehicle_speed/number of records
​
Max Speed (km/h):
The highest speed value in the data.
Max Speed = max(vehicle_speed)

Driving Time (hours):
Total time the vehicle was moving, calculated from time differences between consecutive timestamps.
Driving Time = ∑(time difference between consecutive timestamps in hours)

Total Distance Traveled (km):
Distance for each time interval is calculated as speed × time ( S=vt ), then summed up.
Distance Traveled (for each interval) = vehicle_speed×time_difference (hours)
Total Distance= ∑ Distance Traveled (for all intervals)

Total Fuel Consumption (liters):
Distance traveled is divided by 100 and multiplied by 8 (fuel consumption rate of 8 liters per 100 km).
Fuel Consumption = (Distance Travelled / 100) * 8
Total Fuel Consumption = ∑ Fuel Consumption (for all intervals)

Mileage (km/liter):
Total distance traveled divided by total fuel consumption.
Mileage = Total Distance Travelled / Total Fuel consumption

Average Coolant Temperature (°C):
The average of all coolant temperature readings.
Average Coolant Temperature = ∑ engine_coolant_temperature / Number of Records

Overheat Temperature (°C):
The highest recorded coolant temperature.
Overheat Temperature = max(engine_coolant_temperature)

Time to Max Temperature (minutes):
Time from the first reading to when the maximum coolant temperature is reached.
Time to Max Temp = Timestamp (Max Temp)−Timestamp (Start)/60
​
High RPM Periods Count:
Number of times the engine RPM exceeded a threshold (e.g 4000 RPM).
High RPM Count=Number of records where engine_rpm > 4000

Average Temperature Difference (Intake vs Ambient):
Average difference between intake air temperature and ambient air temperature.
Temperature Difference (for each record) = intake_air_temperature − ambient_air_temperature
Average Temperature Difference = ∑ Temperature Difference / Number of Records

The data is cleaned, unnecessary columns are dropped, and missing values are filled.
