import pandas as pd
import numpy as np

def load_and_process_data(file):
    """Load and process the earthquake data from CSV."""
    df = pd.read_csv(file)
    
    # Ensure required columns exist
    required_columns = ['Date', 'Latitude', 'Longitude', 'Magnitude']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("CSV must contain Date, Latitude, Longitude, and Magnitude columns")
    
    # Handle different date formats and extract year
    # First ensure the Date column is string type
    df['Date'] = df['Date'].astype(str)
    
    try:
        # Convert to datetime with coerce to handle invalid dates
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        # Drop any rows where date conversion failed
        df = df.dropna(subset=['Date'])
        # Extract year after conversion
        df['year'] = df['Date'].dt.year
    except Exception as e:
        raise ValueError(f"Error processing dates: {str(e)}")
    
    # Rename columns to lowercase for consistency
    df = df.rename(columns={
        'Latitude': 'latitude',
        'Longitude': 'longitude',
        'Magnitude': 'magnitude'
    })
    
    # Calculate logarithmic height scale for visualization
    df['height'] = np.log1p(df['magnitude']) * 30000
    
    # Calculate color based on magnitude
    df['color'] = df['magnitude'].apply(calculate_color)
    
    return df

def filter_data(df, year, magnitude_range):
    """Filter the DataFrame based on year and magnitude ranges."""
    return df[
        (df['year'] == year) &
        (df['magnitude'].between(magnitude_range[0], magnitude_range[1]))
    ]

def calculate_color(magnitude):
    """Calculate color based on earthquake magnitude."""
    if magnitude < 4:
        return [65, 182, 196]    # Light blue
    elif magnitude < 5:
        return [250, 177, 160]   # Light orange
    elif magnitude < 6:
        return [243, 156, 18]    # Orange
    elif magnitude < 7:
        return [230, 126, 34]    # Dark orange
    else:
        return [231, 76, 60]     # Red
