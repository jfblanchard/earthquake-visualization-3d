import streamlit as st
import pandas as pd
from utils import load_and_process_data, filter_data
from streamlit.components.v1 import html
from pathlib import Path
import base64
import json


def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


st.set_page_config(page_title="Earthquake Visualization", layout="wide")


def main():
    try:
        # Load the earthquake data directly from the file
        df = load_and_process_data("earthquake_database.csv")

        # Sidebar controls
        st.sidebar.header("Filters")

        # Single year selector
        min_year, max_year = int(df['year'].min()), int(df['year'].max())
        selected_year = st.sidebar.slider("Select Year",
                                          min_value=min_year,
                                          max_value=max_year,
                                          value=min_year)

        # Display title with selected year
        st.markdown("### Earthquake Visualization - {}".format(selected_year))

        # Magnitude range slider
        min_mag, max_mag = float(df['magnitude'].min()), float(
            df['magnitude'].max())
        magnitude_range = st.sidebar.slider("Select Magnitude Range",
                                            min_value=min_mag,
                                            max_value=max_mag,
                                            value=(min_mag, max_mag),
                                            step=0.1)

        # Filter data based on selections
        filtered_df = filter_data(df, selected_year, magnitude_range)

        # Convert filtered data to list of dicts for JSON serialization
        earthquake_data = filtered_df[['latitude', 'longitude',
                                       'magnitude']].to_dict('records')

        # Read the template and encode the texture
        template_path = Path('templates/earth_viz.html')
        template = template_path.read_text()

        # Get base64 encoded texture
        texture_base64 = get_base64_encoded_image('earth_atmos_2048.jpg')

        # Replace placeholders
        html_content = template.replace('{{ earthquake_data|tojson }}',
                                        json.dumps(earthquake_data))
        html_content = html_content.replace(
            '{{ earth_texture_base64 }}',
            f'data:image/jpeg;base64,{texture_base64}')

        # Display the visualization
        html(html_content, height=800)

        # Display statistics
        st.sidebar.markdown("### Statistics")
        st.sidebar.write(f"Total earthquakes shown: {len(filtered_df)}")
        st.sidebar.write(
            f"Average magnitude: {filtered_df['magnitude'].mean():.2f}")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info(
            "Please ensure earthquake_database.csv is present in the project directory"
        )


if __name__ == "__main__":
    main()
