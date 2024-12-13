# 3D Earth Earthquake Visualization

An interactive 3D visualization of global earthquake data, built with Python and Three.js. This application provides a stunning visual representation of seismic activity across the globe, allowing users to explore and understand earthquake patterns through time.

## Features

- Interactive 3D Earth visualization
- Real-time earthquake data rendering
- Year-based filtering of earthquake events
- Magnitude-based filtering
- Responsive design with smooth controls
- Color-coded earthquake indicators based on magnitude
- Dynamic statistics display

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jfblanchard/earthquake-visualization-3d.git
cd earthquake-visualization-3d
```

2. Install the required Python packages:
```bash
pip install streamlit pandas numpy pydeck
```

3. Place your earthquake data CSV file in the project directory (should contain Date, Latitude, Longitude, and Magnitude columns)

## Usage

1. Run the Streamlit application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the provided URL (default: http://localhost:5000)

3. Use the sidebar controls to:
   - Select specific years
   - Filter earthquakes by magnitude range
   - View statistics about the displayed data

## Dependencies

- Python 3.x
- Streamlit
- Pandas
- NumPy
- PyDeck
- Three.js (loaded via CDN)

## Data Format

The application expects a CSV file named `earthquake_database.csv` with the following columns:
- Date: Date of the earthquake
- Latitude: Latitude coordinates
- Longitude: Longitude coordinates
- Magnitude: Earthquake magnitude

## License

This project is licensed under the MIT License - see the LICENSE file for details.
