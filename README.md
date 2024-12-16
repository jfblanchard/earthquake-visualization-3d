# 3D Earth Earthquake Visualization

Interactive 3D visualization of global earthquake data using Python, Three.js, and Streamlit. This application creates an immersive visual experience for exploring seismic activity patterns across the globe.

## 🌟 Features

- **Interactive 3D Earth**: Fully rotatable and zoomable globe visualization
- **Real-time Data Rendering**: Smooth visualization of earthquake events
- **Time-based Filtering**: Filter earthquakes by year
- **Magnitude Filtering**: Focus on specific earthquake magnitudes
- **Dynamic Statistics**: Real-time statistics updates
- **Visual Indicators**: Color-coded earthquakes based on magnitude
- **Responsive Design**: Adapts to different screen sizes

## Quick Start

1. **Clone the Repository**
   ```bash
   git clone [your-repository-url]
   cd earthquake-visualization-3d
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Data**
   - Place your earthquake data CSV file in the project directory
   - Required columns: Date, Latitude, Longitude, Magnitude

4. **Run the Application**
   ```bash
   streamlit run main.py
   ```

5. **Access the Visualization**
   - Open your browser
   - Navigate to http://localhost:5000

## Usage Guide

### Sidebar Controls
- **Year Selection**: Choose specific years to visualize
- **Magnitude Range**: Filter earthquakes by magnitude
- **Statistics Panel**: View real-time data statistics

### Visualization Controls
- **Rotate**: Click and drag
- **Zoom**: Scroll wheel
- **Reset View**: Double click

## Data Format

The `earthquake_database.csv` file should contain:
```csv
Date,Latitude,Longitude,Magnitude
2020-01-01,35.7,-117.5,4.2
```

## 🛠 Technical Stack

- **Frontend**: Three.js for 3D rendering
- **Backend**: Python with Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: PyDeck, Three.js


## 📄 License

This project is licensed under the MIT License 
