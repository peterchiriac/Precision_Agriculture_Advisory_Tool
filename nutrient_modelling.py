def calculate_nutrient_recommendations(soil_data, weather_summary):
    recommendations = []

    # Soil pH
    soil_pH = soil_data["phh2o"].iloc[0]
    print("DEBUG: Evaluating Soil pH:", soil_pH)  # Debug print

    if soil_pH is not None:
        if soil_pH < 6.5:
            recommendations.append("Apply lime to increase soil pH.")
            print("Recommendations so far:", recommendations)  # Debug print
        elif soil_pH >= 7.5:
            recommendations.append("Apply sulfur to lower soil pH.")
            print("Recommendations so far:", recommendations)  # Debug print
        else:
            recommendations.append("Soil pH is within the optimal range.")
        print("DEBUG: Current Recommendations:", recommendations)  # Debug print
    else:
        recommendations.append("Soil pH data is missing or invalid.")
        print("DEBUG: Current Recommendations (Missing pH):", recommendations)  # Debug print

    # CEC
    cec = soil_data["cec"].iloc[0]
    print("CEC:", cec)  # Debug print
    if cec is not None:
        if cec < 10:
            recommendations.append("Enhance soil with organic matter to improve nutrient retention.")
            print("DEBUG: Current Recommendations:", recommendations)  # Debug print
    else:
        recommendations.append("CEC data is missing. Unable to provide recommendations.")

    # Bulk Density
    bd = soil_data["bdod"].iloc[0]
    print("Bulk Density:", bd)  # Debug print
    if bd is not None:
        if bd > 1.6:  # Example threshold for compacted soil
            recommendations.append("Reduce soil compaction using deep tillage or cover crops.")
            print("DEBUG: Current Recommendations:", recommendations)  # Debug print
    else:
        recommendations.append("Bulk density data is missing. Unable to provide recommendations.")

    # Rainfall
    try:
        rainfall = weather_summary.loc[weather_summary["Parameter"] == "Rain (mm)", "Value"].iloc[0]
        print("Rainfall:", rainfall)  # Debug print
        if rainfall < 10:
            recommendations.append("Reduce fertiliser application to prevent nutrient leaching.")
        elif rainfall > 50:
            recommendations.append("Delay fertiliser application due to high rainfall")
        else:
            recommendations.append("Rainfall conditions are suitable for fertiliser application")
            print("DEBUG: Current Recommendations:", recommendations)  # Debug print
    except IndexError:
        recommendations.append("Rainfall data is missing. Unable to provide recommendations.")

    # Temperature
    try:
        temperature = weather_summary.loc[weather_summary["Parameter"] == "Temperature (°C)", "Value"].iloc[0]
        print("Temperature:", temperature)  # Debug print
        if temperature < 10:
            recommendations.append("Delay fertiliser application due to low temperature.")
        elif temperature > 35:
            recommendations.append("Delay fertiliser application due to excessive heat.")
        else:
            recommendations.append("Temperature is suitable for fertiliser application")
            print("DEBUG: Current Recommendations:", recommendations)  # Debug print
    except IndexError:
        recommendations.append("Temperature data is missing. Unable to provide recommendations.")
    except Exception:
        recommendations.append("An error occurred while processing temperature data.")

    # Final debug before return
    print("DEBUG: Final Recommendations:", recommendations)  # Debug print
    return recommendations