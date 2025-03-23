# F1 Ghost Car Visualisation

Generate a video with a ghost car effect (as seen in video games) on the POV video of car-A and utilizing telemetry data of car-A and car-B.

expected outcome : https://www.youtube.com/watch?v=lXuAf8ly6hs

## Project Intent


This project aims to:
1. Fetch telemetry data for two cars (car-A and car-B) from Formula 1 sessions.
2. Process the telemetry data to identify key metrics such as normalised track coordinates in 3D coordiantes space of both cars.
3. Parent the car-A POV video on the car-A track coordinates.
4. Parent the car-B 3D model on the car-B track coordinates.
3. Overlay the 3D model of car-B as a "ghost car" on the POV video of car-A.
4. Generate a final video showcasing the ghost car effect, allowing for visual comparison of performance.

## Current Status


### Project Structure

- `fetch_data.py`: Script for fetching telemetry data, identifying the fastest lap, and exporting lap data to a CSV file.
- `config.json`: Configuration file specifying the driver abbreviation, session, and year for the telemetry data.
- `requirements.txt`: Lists the Python dependencies for the project (`pandas` and `fastf1`).
- `.gitignore`: Specifies files and directories to be ignored by Git.

### Configuration

Update the `config.json` file to specify the driver, session, and year for the telemetry data:
```json
{
    "driver_abbrv": "ver",
    "gp": "spain",
    "session_type": "race",
    "year": 2021
}
```
