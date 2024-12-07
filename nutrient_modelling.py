def calculate_nutrient_recommendations(soil_data, weather_summary):
    recommendations = []

    # Soil pH
    soil_pH = soil_data["phh2o"].iloc[0]
    print("DEBUG: Evaluating Soil pH:", soil_pH)
    if soil_pH is not None:
        if soil_pH < 6.5:
            recommendations.append("Apply lime to increase soil pH.")
        elif soil_pH >= 7.5:
            recommendations.append("Apply sulfur to lower soil pH.")
        else:
            recommendations.append("Soil pH is within the optimal range.")
    else:
        recommendations.append("Soil pH data is missing or invalid.")

    # CEC
    cec = soil_data["cec"].iloc[0]
    print("CEC:", cec)
    if cec is not None:
        if cec < 10:
            recommendations.append("Enhance soil with organic matter to improve nutrient retention.")
    else:
        recommendations.append("CEC data is missing. Unable to provide recommendations.")

    # Bulk Density
    bd = soil_data["bdod"].iloc[0]
    print("Bulk Density:", bd)
    if bd is not None:
        if bd > 1.6:  # Example threshold for compacted soil
            recommendations.append("Reduce soil compaction using deep tillage or cover crops.")
    else:
        recommendations.append("Bulk density data is missing. Unable to provide recommendations.")

    # Clay Content
    clay_content = soil_data["clay"].iloc[0]
    print("Clay Content:", clay_content)
    if clay_content is not None:
        if clay_content > 40:
            recommendations.append("Improve drainage with soil amendments or tile drainage.")
        elif clay_content < 10:
            recommendations.append("Increase water retention by adding organic matter.")
        else:
            recommendations.append("Clay content is within the optimal range.")
    else:
        recommendations.append("Clay content data is missing. Unable to provide recommendations.")

    # Soil Organic Carbon (SOC)
    soc = soil_data["soc"].iloc[0]
    print("Soil Organic Carbon (SOC):", soc)
    if soc is not None:
        if soc < 10:
            recommendations.append("Incorporate organic amendments like compost or manure to improve SOC.")
        elif soc > 50:
            recommendations.append("Maintain high SOC levels through conservation tillage or crop rotations.")
        else:
            recommendations.append("SOC levels are within the optimal range.")
    else:
        recommendations.append("SOC data is missing. Unable to provide recommendations.")

    # Rainfall
    try:
        rainfall = weather_summary.loc[weather_summary["Parameter"] == "Rain (mm)", "Value"].iloc[0]
        print("Rainfall:", rainfall)
        if rainfall < 10:
            recommendations.append(
                "Rainfall is low; consider maintaining current fertiliser levels to avoid undernutrition, but monitor soil moisture.")
        elif rainfall > 50:
            recommendations.append("Rainfall is excessive; delay fertiliser application to prevent nutrient runoff.")
        else:
            recommendations.append("Rainfall is moderate; conditions are suitable for fertiliser application.")
    except IndexError:
        recommendations.append("Rainfall data is unavailable; unable to provide recommendations.")

    # Temperature
    try:
        temperature = weather_summary.loc[weather_summary["Parameter"] == "Temperature (°C)", "Value"].iloc[0]
        print("Temperature:", temperature)
        if temperature < 10:
            recommendations.append("Delay fertiliser application due to low temperature.")
        elif temperature > 35:
            recommendations.append("Delay fertiliser application due to excessive heat.")
        else:
            recommendations.append("Temperature is suitable for fertiliser application.")
    except IndexError:
        recommendations.append("Temperature data is missing. Unable to provide recommendations.")
    except Exception:
        recommendations.append("An error occurred while processing temperature data.")

    print("DEBUG: Final Recommendations:", recommendations)
    return recommendations