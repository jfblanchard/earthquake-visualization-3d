import pydeck as pdk
import numpy as np

def create_earthquake_layer(df):
    """Create the PyDeck layer for earthquake visualization."""
    # Create a denser star field
    stars = [{"position": [i, j, -1]} for i, j in zip(
        np.random.uniform(-180, 180, 2000),  # Increased number of stars
        np.random.uniform(-90, 90, 2000)
    )]
    
    # Create grid lines for the Earth
    grid_lines = []
    # Latitude lines
    for lat in range(-80, 81, 20):
        points = [[lng, lat] for lng in range(-180, 181, 5)]
        grid_lines.append(points)
    # Longitude lines
    for lng in range(-180, 181, 20):
        points = [[lng, lat] for lat in range(-80, 81, 5)]
        grid_lines.append(points)
    
    return [
        # Stars background
        pdk.Layer(
            "ScatterplotLayer",
            data=stars,
            get_position="position",
            get_radius=500,  # Smaller stars
            get_fill_color=[255, 255, 255, 80],  # Brighter stars
            pickable=False,
        ),
        # Earth sphere - ocean
        pdk.Layer(
            "PolygonLayer",
            data=[{"coordinates": [0, 0]}],
            stroked=False,
            filled=True,
            extruded=True,
            wireframe=False,
            get_polygon=lambda x: [[[lng, lat] for lng in range(-180, 181, 5)] for lat in range(-90, 91, 5)],
            get_fill_color=[0, 20, 40, 200],  # Darker blue for oceans
            pickable=False,
        ),
        # Earth grid lines
        pdk.Layer(
            "PathLayer",
            data=[{"path": line} for line in grid_lines],
            get_path="path",
            get_width=1,
            get_color=[30, 100, 200, 120],  # Light blue grid lines
            pickable=False,
            width_scale=1,
        ),
        # Earthquake columns
        pdk.Layer(
            "ColumnLayer",
            data=df,
            get_position=["longitude", "latitude"],
            get_elevation="height",
            elevation_scale=1,
            radius=25000,
            get_fill_color="color",
            pickable=True,
            auto_highlight=True,
            coverage=1,
        )
    ]

def create_view_state():
    """Create the initial view state for the visualization."""
    return pdk.ViewState(
        latitude=0,
        longitude=0,
        zoom=1.5,
        min_zoom=1,
        max_zoom=16,
        pitch=50,
        bearing=0,
        height=700,
        auto_rotation_speed=0.5  # Rotation speed in degrees/second
    )

def calculate_camera_position(center_lat, center_lon, zoom_level):
    """Calculate camera position based on center coordinates and zoom level."""
    R = 6371000  # Earth's radius in meters
    camera_distance = R * np.exp(-zoom_level * np.log(2))
    return {
        "longitude": center_lon,
        "latitude": center_lat,
        "zoom": zoom_level,
        "pitch": 45,
        "bearing": 0,
        "altitude": camera_distance
    }
