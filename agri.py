import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv
import os
from nutrient_modelling import calculate_nutrient_recommendations

# Load environment variables
load_dotenv()

# Fetch the API key from .env
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Title and Introduction
st.title("Precision Agriculture Advisory Tool")
st.markdown("""
This tool provides tailored crop nutrient recommendations based on soil properties and weather.

The five key soil properties analyzed are:
- **Soil pH (phh2o)**
- **Cation Exchange Capacity (cec)**
- **Bulk Density (bdod)**
- **Clay Content (clay)**
- **Soil Organic Carbon (soc)**

The two weather conditions analyzed are:
- **Temperature**
- **Rainfall**
""")

# Sidebar for User Input
st.sidebar.header("Input Parameters")
latitude = st.sidebar.number_input("Latitude", value=51.7752, step=0.01)
longitude = st.sidebar.number_input("Longitude", value=0.3361, step=0.01)

# Submit Button
if st.sidebar.button("Submit"):
    with st.spinner("Fetching data..."):
        try:
            # Soil API call
            soil_api_url = "https://rest.isric.org/soilgrids/v2.0/properties/query"
            soil_params = {"lat": latitude, "lon": longitude}
            soil_response = requests.get(soil_api_url, params=soil_params)
            soil_response.raise_for_status()
            soil_raw_data = soil_response.json()
            print("DEBUG: Raw Soil API Response fetched successfully.")

            # Weather API call
            weather_api_url = "https://api.openweathermap.org/data/2.5/weather?"
            weather_params = {
                "lat": latitude,
                "lon": longitude,
                "appid": OPENWEATHER_API_KEY,
                "units": "metric",
            }
            weather_response = requests.get(weather_api_url, params=weather_params)
            weather_response.raise_for_status()
            weather_data = weather_response.json()
            print("DEBUG: Weather API Response fetched successfully.")

            # Process Weather Data into a Summary Table
            weather_summary = pd.DataFrame({
                "Parameter": [
                    "Temperature (°C)",
                    "Feels Like (°C)",
                    "Humidity (%)",
                    "Wind Speed (m/s)",
                    "Rain (mm)"
                ],
                "Value": [
                    weather_data['main']['temp'],
                    weather_data['main']['feels_like'],
                    weather_data['main']['humidity'],
                    weather_data['wind']['speed'],
                    weather_data.get("rain", {}).get("1h", 0),  # Default to 0 if no rain data
                ],
            })

            # Debug Weather Data
            print("DEBUG: Weather Summary Content:\n", weather_summary)
            print("DEBUG: Weather Summary Info:\n", weather_summary.info())
            print("DEBUG: Weather Summary Describe:\n", weather_summary.describe(include="all"))

            # Display Weather Data
            st.subheader("Weather Data")
            st.dataframe(weather_summary)

            # Extract relevant soil properties
            properties = ["phh2o", "cec", "bdod", "clay", "soc"]
            layers = ['0-5cm', '5-15cm', '15-30cm']
            soil_data = {"Layer": layers}

            for prop in properties:
                values = []
                for layer in layers:
                    try:
                        # Locate the property in the raw data
                        property_data = next(
                            layer_data for layer_data in soil_raw_data["properties"]["layers"]
                            if layer_data["name"] == prop
                        )

                        # Find the specific layer
                        layer_data = next(
                            depth for depth in property_data["depths"]
                            if depth["label"] == layer
                        )

                        # Get the mean value
                        mean_value = layer_data["values"]["mean"]
                        # Apply scaling based on property type
                        if prop == "phh2o":  # Scaling for pH
                            mean_value /= 10
                        elif prop == "cec":  # Scaling for CEC
                            mean_value /= 10
                        elif prop == "bdod":  # Scaling for Bulk Density
                            mean_value /= 100
                        elif prop == "clay":  # Scaling for Clay Content
                            mean_value /= 10
                        elif prop == "soc":  # Scaling for Soil Organic Carbon
                            mean_value /= 100
                        values.append(mean_value)
                    except (StopIteration, KeyError):
                        values.append(None)  # Handle missing data gracefully
                soil_data[prop] = values

            # Convert to DataFrame
            soil_df = pd.DataFrame(soil_data)

            # Debug Soil Data
            print("DEBUG: Soil DataFrame Content:\n", soil_df)
            print("DEBUG: Soil DataFrame Info:\n", soil_df.info())
            print("DEBUG: Soil DataFrame Describe:\n", soil_df.describe(include="all"))

            # Display Parsed Soil Data
            st.subheader("Parsed Soil Data")
            st.dataframe(soil_df)

        except Exception as e:
            st.error(f"An error occurred while fetching or parsing data: {e}")
            print(f"ERROR: Exception occurred while processing data: {e}")
            soil_df = pd.DataFrame()
            weather_summary = pd.DataFrame()

        try:
            # Call the recommendation function
            print("DEBUG: About to call `calculate_nutrient_recommendations`.")
            nutrient_recommendations = calculate_nutrient_recommendations(soil_df, weather_summary)
            print("DEBUG: Final Recommendations:", nutrient_recommendations)

            # Display recommendations
            if nutrient_recommendations:
                st.subheader("Enhanced Nutrient Recommendations")
                for recommendation in nutrient_recommendations:
                    st.markdown(f"- {recommendation}")
            else:
                st.warning("No recommendations could be generated. Check your input data.")
        except Exception as e:
            print(f"ERROR: Exception while generating recommendations: {e}")
            st.error(f"An error occurred while generating recommendations: {e}")