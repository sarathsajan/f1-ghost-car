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
# This function will return a Session object, but it will not load any session specific data like lap timing, telemetry, … yet.
# For this, you will need to call load() on the returned object.
session.load(telemetry=True)

# Fetch the Laps object for the specified driver
driver_all_laps = session.laps.pick_drivers(DRIVER_ABBRV)
driver_fastest_lap = driver_all_laps.pick_fastest()

print(driver_fastest_lap['LapTime'])

driver_all_laps.to_csv(f'{DRIVER_ABBRV}_{str(driver_fastest_lap['LapTime']).replace(':','_')}_laps.csv', index=False)


