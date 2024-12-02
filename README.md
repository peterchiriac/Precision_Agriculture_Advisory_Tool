  ##                    Precision Agriculture Advisory Tool
  ![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
  ![Streamlit](https://img.shields.io/badge/Streamlit-Framework-orange)
  ![License](https://img.shields.io/badge/License-MIT-green)
  #### A modern tool for optimised crop nutrition and sustainable farming

  
---
Table Of Contents

1. [Introduction](#1-introduction)
2. [Overview](#2-overview)
3. [Challenges Addressed](#3-challenges-addressed)
4. [End-to-End Workflow](#4-end-to-end-workflow)
5. [Features](#5-features)
6. [Running the Application](#7-running-the-application)
7. [Installation](#6-installation)
8. [Instructions](#8-instructions)
9. [Deployment](#9-deployment)
10. [Technologies Used](#10-technologies-used)
11. [Limitations and Future Work](#11-limitations-and-future-work)
12. [Contributing](#12-contributing)
13. [License](#13-license)
14. [Contact](#14-contact)

---

## 1. Introduction

The Precision Agriculture Advisory Tool is a web-based application designed to assist in making data-driven decisions about crop nutrition and soil health. This tool aims to bridge the gap between modern technology and traditional farming practices, empowering farmers with actionable insights to optimise productivity while reducing environmental impact.
   
---
## 2. Overview

Farmers face significant challenges in optimising fertiliser application due to the absence of integrated tools that provide real-time, actionable data. This gap often results in inefficient nutrient use, leading to:

•	Diminished yields  
•	Increased costs  
•	Environmental strain  
• Poor nutritional quality in harvested crops  

Crops subjected to excessive or insufficient fertiliser applications frequently fail to develop an optimal nutrient profile, compromising both their quality and nutritional value. The central question this project seeks to address is:
*How can farmers leverage data to optimise nutrient application effectively?*

   ---

## 3. Challenges Addressed

The tool directly tackles key challenges faced by modern agriculture:

#### Economic Challenges:

•	Economic Loss: Overuse of fertilisers leads to unnecessary expenses without proportional benefits.  
•	Reduced Yields: Insufficient nutrients result in stunted growth, low yields, and unprofitable farming.  
•	Long-Term Soil Degradation: Mismanagement of nutrients depletes soil health, increasing future costs for rehabilitation and reducing land productivity.  
•	Financial Risk from Crop Failure: Poor nutrient application or timing can result in crop failures, causing significant income loss and potential debt.  

#### Technical Challenges

•	Precision Requirements: Nutrient needs vary significantly based on soil type, crop type, and location, requiring tailored application strategies.  
•	Timing Sensitivity: Proper timing is essential to maximise nutrient absorption and minimise waste, but many farmers lack access to precise timing recommendations.  
•	Environmental Sensitivity: Nutrients can be washed away by heavy rains or remain unused during drought conditions, further complicating application decisions.  

#### Environmental Challenges:

•	Water Pollution: Nutrient leaching into groundwater contaminates water supplies.  
•	Eutrophication: Excessive nutrient runoff into water bodies promotes algal blooms, depleting oxygen and causing fish die-offs.  
•	Sustainability Risks: Inefficient nutrient use increases environmental strain, reducing the long-term viability of farmland.  

---

## 4. End-to-End Workflow

The development process for the Precision Agriculture Advisory Tool was structured around the following workflow:

 *4.1 Problem Definition*

•	Key Question: How can farmers optimise nutrient application using data?  
•	Stakeholders: Farmers, agricultural advisors, and sustainability advocates.  

 *4.2 Data Collection*

•	Real-Time Data: Integrated APIs for live weather and soil conditions (OpenWeatherMap and SoilGrids).  
•	User Inputs: Enabled user input for crop type, location, and nutrient preferences.  

  *4.3 Data Processing*

•	Cleaned and preprocessed raw data from APIs and datasets.  
•	Engineered features by combining soil and weather data for nutrient advice.  
•	Stored processed data in efficient structures for easy access.  

 *4.4 Modelling and Analytics*

•	Developed algorithms for tailored nutrient recommendations.  
•	Built predictive models to forecast the impact of fertiliser timing on crop yield.  
•	Validated recommendations using research-based standards.  

 *4.5 Visualisation and Delivery*

•	Designed an advisory tool with an intuitive interface for tailored recommendations.  


  *4.6 Deployment*

•	Deployed the tool as a web app using Streamlit Sharing.  
•	Made the tool accessible with clear instructions for usage.  

 *4.7 Future enhancements*

•	Outlined future enhancements for data visualisation and feature expansion.  

---

## 5. Features:

Soil Analysis: Evaluates five key soil properties:
•	Soil pH (phh2o)  
•	Cation Exchange Capacity (cec)  
•	Bulk Density (bdod)  
•	Clay Content (clay)  
•	Soil Organic Carbon (soc)  
•	Weather Analysis: Incorporates real-time weather data, including:  
•	Temperature  
•	Rainfall  
•	Nutrient Recommendations  
•	Tailored advice based on soil and weather data.  
•	Suggestions to address deficiencies or improve soil conditions.  

---

## 6. Running the application

streamlit run agri.py

After running, open the displayed URL (typically http://localhost:8501) in your browser.
 

---

## 7. Installation

7.1 Clone the repository
git clone [https://github.com/peterchiriac/Precision_Agriculture_Advisory_Tool.git](https://github.com/peterchiriac/Precision_Agriculture_Advisory_Tool.git)
cd Precision_Agriculture_Advisory_Tool
Ensure you have Python 3.7 or higher installed on your system

7.2 Install dependencies
pip install -r requirements.txt

7.3 Add Environment Variables
Create a .env file in the project directory with your API keys:
OPENWEATHER_API_KEY=your_openweather_api_key

---

## 8. Instructions

8.1 Enter the latitude and longitude of your field in the input sidebar. Ensure these coordinates correspond to active agricultural areas. For your convenience, here are some suggested locations:

*England*  
•	Latitude: 52.2053, Longitude: 0.1218 (Cambridge, an agricultural hub)  
•	Latitude: 51.5074, Longitude: -0.1278 (Near Greater London’s outskirts, where agriculture thrives)  
•	Latitude: 53.4808, Longitude: -2.2426 (Manchester surroundings, with productive farmland)  
*Romania*    
•	Latitude: 46.5678, Longitude: 27.6659 (Bacău County, known for its farmland)   
*Indiana, US*    
•	Latitude: 39.7684, Longitude: -86.1581 (Indiana, part of the U.S. Corn Belt)  

Note: The locations provided are examples. You can input the latitude and longitude for any agricultural field within the supported regions.

8.2.	Click “Submit” to fetch soil and weather data.  
8.3.	View the processed data in tables displayed on the interface.  
8.4.	Review actionable crop nutrient recommendations tailored to your inputs.  

---

## 9. Deployment

The app is deployed using Streamlit Sharing and can be accessed here:
https://precisionagricultureadvisorytool-yfewcvczjjwyv9wb3ftea6.streamlit.app/

---

## 10. Technologies Used


| Technology         | Purpose                              |
|--------------------|--------------------------------------|
| Python             | Core programming language           |
| Streamlit          | Web app framework                   |
| Pandas             | Data manipulation and analysis      |
| Requests           | API calls to fetch soil/weather data|
| SoilGrids API      | Soil property data                  |
| OpenWeather API    | Weather data                        |

---

## 11. Limitations And Future Work

•	The tool relies on third-party APIs; data accuracy and availability are dependent on the APIs.  
•	Location-based data resolution may vary depending on the latitude and longitude provided.  
•	Currently, the tool does not integrate real-time location names or maps.  

  ##### API Coverage Note:

  Please be aware that the SoilGrids API is limited to areas that are already used for agricultural purposes. You can't input any location (i.e. a street or your backyard) as the API does not cover those areas.

Future Enhancements

•	Add interactive data visualizations using Tableau or Matplotlib.  
•	Integrate a location API for displaying field names.  
•	Expand soil and weather parameters for more comprehensive recommendations.  

---

## 12. Contributing

At this time, contributions are not accepted as this is a portfolio project. Future collaboration may be welcomed!

---

## 13. License 

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 14. Contact

For any inquiries, suggestions, or feedback, feel free to reach out to me at **peter.chiriac@outlook.com**.

---

I hope you find this tool valuable for enhancing agricultural practices. Feel free to explore the live app and provide feedback!

