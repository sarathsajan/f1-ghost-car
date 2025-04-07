# F1 Ghost Car Visualisation
---

Generate a video with a ghost car effect (as seen in video games) on the POV video of car-A and utilizing telemetry data of car-A and car-B.

expected outcome : https://www.youtube.com/watch?v=lXuAf8ly6hs

## Project Intent


This project aims to:
1. Fetch telemetry data for two cars (car-A and car-B) from Formula 1 sessions.
2. Process the telemetry data to identify key metrics such as normalised track coordinates in 3D coordiantes space of both cars.
3. Attach the car-A POV video (child) on the car-A normalised track coordinates (parent).
4. Attach the car-B 3D model (child) on the car-B normalised track coordinates (parent).
5. Overlay the 3D model of car-B as a "ghost car" on the POV video of car-A.
6. Generate a final video showcasing the ghost car effect, allowing for visual comparison of performance.

## Current Status

### Achievements So Far

1. **Telemetry Data Fetching**:  
   - Implemented the `fetch_data.py` script to fetch telemetry data for a specific driver and session using the `fastf1` library.
   - Identified the fastest lap for the driver and exported the lap data to a CSV file.

2. **Data Export**:  
   - Successfully exported telemetry data to CSV files with dynamically generated filenames based on the driver's abbreviation, session type, and fastest lap time (e.g., `VER_2025_japan_Q_01_26_983000_telemetry.csv`).

3. **Visualization**:  
   - Generated scatter plots of telemetry data for visual analysis (e.g., `ANT_2025_japan_R_01_30_965000_scatterplot.png`).

4. **Configuration Management**:  
   - Added a `config.json` file to specify the driver abbreviation, session type, year, and other parameters for telemetry data fetching.

5. **Dependencies Management**:  
   - Created a `requirements.txt` file listing the required Python dependencies (`pandas`, `fastf1`, etc.).

6. **Output Files**:  
   - Produced various output files, including telemetry CSVs, scatter plots, and placeholder video files (e.g., `ANT_2025_japan_R_01_30_965000.mp4`).

### Project Structure

- `fetch_data.py`: Script for fetching telemetry data, identifying the fastest lap, and exporting lap data to a CSV file.
- `config.json`: Configuration file specifying the driver abbreviation, session, and year for the telemetry data.
- `requirements.txt`: Lists the Python dependencies for the project (`pandas` and `fastf1`).
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `ANT_2025_japan_R_01_30_965000_coordinates.csv`: Example output file containing normalized track coordinates.
- `ANT_2025_japan_R_01_30_965000_scatterplot.png`: Example scatter plot visualization of telemetry data.
- `ANT_2025_japan_R_01_30_965000.mp4`: Placeholder video file for the ghost car visualization.
