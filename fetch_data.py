import fastf1 as ff1
import pandas as pd
import json

# read the json config file
config = json.load(open('config.json'))
YEAR = config['year']
GP = config['gp']
SESSION_TYPE = config['session_type']
DRIVER_ABBRV = config['driver_abbrv']

# Fetch the session object
session = ff1.get_session(year=YEAR, gp=GP, identifier=SESSION_TYPE)
# This function will return a Session object, but it will not load any session specific data like lap timing, telemetry... yet.
# For this, you will need to call load() function on the returned object.
session.load(telemetry=True)

# Fetch the Laps object for the specified driver
single_driver_telemetry_all_laps = session.laps.pick_drivers(DRIVER_ABBRV)
single_driver_telemetry_fastest_lap = single_driver_telemetry_all_laps.pick_fastest()

print(single_driver_telemetry_fastest_lap['LapTime'])

single_driver_telemetry_all_laps.to_csv(f'{DRIVER_ABBRV}_{str(single_driver_telemetry_fastest_lap['LapTime']).replace(':','_')}_laps.csv', index=False)


