import datetime
import calendar
import random

with open('sqlinserts.txt', 'w') as file:
    year = 2022
    while year <= 2023:
        for month in range(1, 13):
            num_days = calendar.monthrange(year, month)[1]

            template = "INSERT INTO weatherdata_weatherdata (temperature, humidity, air_pressure, wind_speed, wind_direction, timestamp) VALUES ({temperature:.2f}, {humidity:.2f}, {air_pressure:.2f}, {wind_speed:.2f}, '{wind_direction}', '{timestamp}');\n"

            for day in range(1, num_days + 1):
                hour, minute, second, milliseconds = random.randint(0, 23), random.randint(0, 59), random.randint(0, 59), random.randint(0, 999999)
                dt = datetime.datetime(year, month, day, hour, minute, second, milliseconds)
                timestamp = dt.strftime('%Y-%m-%d %H:%M:%S.%f')


                temperature = random.uniform(-20, 40)
                humidity = random.uniform(0, 99.8)
                air_pressure = random.uniform(870, 1086)
                wind_speed = random.uniform(0, 112.5)
                wind_direction = random.choice(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])

                sql = template.format(temperature=temperature, humidity=humidity, air_pressure=air_pressure,
                                      wind_speed=wind_speed, wind_direction=wind_direction, timestamp=timestamp)


                file.write(sql)

        year += 1
