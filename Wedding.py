import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="WEDDING INVITATION: MR & MRS THEBE", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Wedding Information", "Gift Registry", "Wedding Programme", "RSVP"],
)

# Sections based on menu selection
if menu == "Wedding Information":
    st.title("Wedding Celebration")
    st.sidebar.header("Wedding Information")
# Title of the app


# Collect basic information
couple = "Dr. Tumelo Thebe & Dr. Mosa Seeco"
venue = "Cooke's Lake- Mafikeng"
date = "28th March 2026"

# Display basic profile information
st.header("Wedding Invitation")
st.write(f"**The Couple:** {couple}")
st.write(f"**Where:** {venue}")
st.write(f"**When:** {date}")

st.image(
    "https://scontent.fpry2-1.fna.fbcdn.net/v/t39.30808-6/468138446_10236239057739258_7387694576841345511_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=a5f93a&_nc_ohc=WPwI9STRoggQ7kNvwHY2Jx1&_nc_oc=AdlpbFiltIdkUzOp3RKUm_NYB1c4vfY8ROcwZ9mqrSkqv3vLJ5h1Cl96l1LARiUc-Jg&_nc_zt=23&_nc_ht=scontent.fpry2-1.fna&_nc_gid=QYm7fMMxLmHQiOeyu9VeNQ&oh=00_Afp7qcKwX1ofDuErA1cRzf7ZM6Ox8MtXqUjvQ9yxvYv0aw&oe=6980203A",
    caption="Mr & Mrs Thebe"
)
if menu == "Wedding Programme":
    st.title("Wedding Programme")
    st.sidebar.header("View or download the wedding programme here")
    
# Add a section for publications
st.header("Programme")
programme = pd.read_csv("programme.csv")


# Add a section for visualizing publication trends
st.header("Programme Timeline")
st.write(programme)

if menu == "Gift Registry":
    st.title("Gift Registry")
    st.sidebar.header("Gift Registry")
# Add STEM Data Section
st.header("Explore Gift Registry")

# Generate dummy data
gift_cards = pd.DataFrame({
    "Retailers": ["@Home", "Sheet Street", "Le Creuset", "Jet Home", "Mr Price Home"],
    "Value (R)": [500.0, 500.0, 2000.0, 500.0, 1000.0],
    "Expiry Date": pd.date_range(start="2026-04-01", periods=5),
})

gift_suggestions_tumelo = pd.DataFrame({
    "Gifts": ["Tyres", "Rims", "Vintage Sound", "Musical Instrument", "Boerboel"],
    "Rating (out of 10)": [4.0, 6.0, 8.5, 8.0, 7.5],
    "Expiry Date": pd.date_range(start="2026-04-01", periods=5),
})

gift_suggestions_pabi = pd.DataFrame({
    "Gifts": ["Furniture", "Books", "Galaxy Z Flip", "BMW 330is", "Pretty Things"],
    "Rating (out of 10)": [5, 8, 9, 9, 10],
    "Prices (R)": [50000, 7000, 30000, 800000, 5000000],
    "Expiry Date": pd.date_range(start="2026-04-01", periods=5),
})

# Tabbed view for wedding data
st.subheader("Wedding Data Viewer")
data_option = st.selectbox(
    "Choose info to explore", 
    ["Guest List", "Seating Arrangement", "Menu"]
)

if data_option == "Guest List":
    st.write("### Guest List")
    guest_list = pd.read_csv("Guestlist.csv")
    st.dataframe(guest_list)
    st.write(guest_list)

elif data_option == "Seating Arrangement":
    st.write("### Who sits where?")
    seating_arrangement = pd.read_csv("Seatingchart.csv")
    st.dataframe(seating_arrangement)
    st.write(seating_arrangement)

elif data_option == "Menu":
    st.write("### What's on the menu")
    st.image("https://marketplace.canva.com/EAFhSAvW2HU/1/0/1131w/canva-white-%26-black-gold-minimal-classy-wedding-menu-C5AC4pLPXow.jpg")
    caption = "The Menu"

if menu == "RSVP":
    st.header("Will you celebrate with us?")
    st.write("Please confirm your attendance")
    data_option = st.selectbox("SELECT AN OPTION", 
    st.button["YES, I'll attend", "No, I won't be attending", "I'm not certain"])
elif data_option == "YES, I'll attend":
    st.write("GREAT! We look forward to celebrating with you")
elif data_option == "No, I won't be attending":
    st.write("Your presence would be the best gift, we'll settle for other gifts")
elif data_option == "I'm not certain":
    st.write("Let us know when you decide")
    name_1 = "Mmoni"
    cell_1 = "0745454554"
    name_2 = "Tsholo"
    cell_2 = "0754562514"
    st.write(f"You can also RSVP by contacting {name_1} on {cell_1} and {name_2} on {cell_2}.")