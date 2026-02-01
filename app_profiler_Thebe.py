import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
# Title of the app
st.title("Researcher Profile")

# Collect basic information

field = "Microbiology"
institution = "Agricultural Research Council"

# Display basic profile information
st.header("Tumelo Thebe")

st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://i1.rgstatic.net/ii/profile.image/272816599728147-1442055954841_Q128/Tumelo-Thebe.jpg",
    caption="Tumelo Thebe"
)
st.header("Professional Summary")

st.write("Highly motivated professional with a robust academic background, holding a B.Sc. in Biology and Chemistry, a B.Sc. Honours in Microbiology, and training in Project Management and Quality Assurance. My diverse expertise spans biology, analytical and organic chemistry, microbiology, biotechnology, and quality management. With hands-on experience as an intern research microbiologist at the National Research Foundation (NRF), roles in quality control and physical testing at Lafarge-Holcim, and M.Sc. student at the Agricultural Research Council (ARC), I bring a proven track record in research, quality control, and student mentorship. My ability to conduct independent research, coupled with a passion for continuous learning and development, positions me to contribute effectively and uphold high standards in dynamic environments.")
# Add a section for publications
st.header("Research Outputs")
publications = pd.read_csv("C:/Users/ThebeT/Desktop/Python Course/Training/Day 3/Publications.csv")
st.dataframe(publications)

st.header("Research Output Insights")
if "Year" in publications.columns:
    year_counts = publications["Year"].value_counts().sort_index()
    # Create a Plotly figure
fig = px.bar(year_counts, title="Figure 1: Number of publications per year")

# Display the plot in the Streamlit app
st.plotly_chart(fig)

st.header("More Information")

# Generate dummy data
affiliations_data = pd.DataFrame({
    "Institution": ["Agricultural Research Council", "North-West University", "Lefika Solutions", "Tharabololo Primary Cooporative"],
    "Position": ["Junior Researcher", "Post-graduate Student", "Director", "Board Chairperson"],
    "Commencement Date": ["2024-10-01", "2025-02-28", "2016-03-01", "2023-03-01"]
})


weather_data = pd.DataFrame({
    "City": ["Mafikeng", "Pretoria", "Buenos Aires", "Tijuana", "Paris"],
    "Temperature (°C)": [25, 24, 23, 25, 15],
    "Humidity (%)": [66, 74, 56, 78, 54]
})

# Tabbed view for STEM data
st.subheader("STEM Data Viewer")
data_option = st.selectbox(
    "Choose Information to explore", 
    ["Click Here to Select", "Affiliations", "Weather Data"]
)

if data_option == "Affiliations":
    st.write("### Affiliations Info")
    st.dataframe(affiliations_data)
   

elif data_option == "Weather Data":
    st.write("### Weather Data")
    st.dataframe(weather_data)
    # Add widgets to filter by temperature and humidity
    temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    filtered_weather = weather_data[
        weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
        weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
    ]
    st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
    st.dataframe(filtered_weather)

# Add a contact section
st.header("Contact Information")
email = "ThebeT@arc.agric.za"
st.write(f"You can reach me at {email}.")