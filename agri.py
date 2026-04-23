import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv
import os
from nutrient_modelling import calculate_nutrient_recommendations

load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

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

st.sidebar.header("Input Parameters")
latitude = st.sidebar.number_input("Latitude", value=51.7752, step=0.01)
longitude = st.sidebar.number_input("Longitude", value=0.3361, step=0.01)

if st.sidebar.button("Submit"):
    soil_df = None
    weather_summary = None

    with st.spinner("Fetching data..."):
        try:
            # Soil API call
            soil_api_url = "https://rest.isric.org/soilgrids/v2.0/properties/query"
            soil_params = {
                "lat": latitude,
                "lon": longitude,
                "property": ["phh2o", "cec", "bdod", "clay", "soc"],
                "depth": ["0-5cm", "5-15cm", "15-30cm"],
                "value": ["mean"]
            }

            soil_response = requests.get(soil_api_url, params=soil_params, timeout=20)
            soil_response.raise_for_status()
            soil_raw_data = soil_response.json()

            # Weather API call
            weather_api_url = "https://api.openweathermap.org/data/2.5/weather"
            weather_params = {
                "lat": latitude,
                "lon": longitude,
                "appid": OPENWEATHER_API_KEY,
                "units": "metric",
            }

            weather_response = requests.get(weather_api_url, params=weather_params, timeout=15)
            weather_response.raise_for_status()
            weather_data = weather_response.json()

            # Weather summary
            weather_summary = pd.DataFrame({
                "Parameter": [
                    "Temperature (°C)",
                    "Feels Like (°C)",
                    "Humidity (%)",
                    "Wind Speed (m/s)",
                    "Rain (mm)"
                ],
                "Value": [
                    weather_data["main"]["temp"],
                    weather_data["main"]["feels_like"],
                    weather_data["main"]["humidity"],
                    weather_data["wind"]["speed"],
                    weather_data.get("rain", {}).get("1h", 0),
                ],
            })

            st.subheader("Weather Data")
            st.dataframe(weather_summary)

            # Parse soil data
            properties = ["phh2o", "cec", "bdod", "clay", "soc"]
            layers = ["0-5cm", "5-15cm", "15-30cm"]
            soil_data = {"Layer": layers}

            all_layers_data = soil_raw_data.get("properties", {}).get("layers", [])

            for prop in properties:
                values = []

                property_data = next(
                    (item for item in all_layers_data if item.get("name") == prop),
                    None
                )

                for layer in layers:
                    mean_value = None

                    if property_data:
                        layer_data = next(
                            (depth for depth in property_data.get("depths", []) if depth.get("label") == layer),
                            None
                        )

                        if layer_data:
                            mean_value = layer_data.get("values", {}).get("mean")

                    if mean_value is not None:
                        if prop == "phh2o":
                            mean_value /= 10
                        elif prop == "cec":
                            mean_value /= 10
                        elif prop == "bdod":
                            mean_value /= 100
                        elif prop == "clay":
                            mean_value /= 10
                        elif prop == "soc":
                            mean_value /= 100

                    values.append(mean_value)

                soil_data[prop] = values

            soil_df = pd.DataFrame(soil_data)

            st.subheader("Parsed Soil Data")
            st.dataframe(soil_df)

        except requests.exceptions.Timeout:
            st.error("The soil or weather service took too long to respond. Please try again.")
        except requests.exceptions.RequestException as e:
            st.error(f"API request failed: {e}")
        except Exception as e:
            st.error(f"An error occurred while fetching or parsing data: {e}")

    # Only generate recommendations if data was successfully built
    if soil_df is not None and weather_summary is not None and not soil_df.empty and not weather_summary.empty:
        required_soil_cols = {"phh2o", "cec", "bdod", "clay", "soc"}

        if required_soil_cols.issubset(soil_df.columns):
            try:
                nutrient_recommendations = calculate_nutrient_recommendations(soil_df, weather_summary)

                if nutrient_recommendations:
                    st.subheader("Enhanced Nutrient Recommendations")
                    for recommendation in nutrient_recommendations:
                        st.markdown(f"- {recommendation}")
                else:
                    st.warning("No recommendations could be generated. Check your input data.")
            except Exception as e:
                st.error(f"An error occurred while generating recommendations: {e}")
        else:
            st.warning("Soil data is incomplete, so recommendations could not be generated.")
    else:
        st.info("Recommendations were skipped because the input data could not be retrieved.")