import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pydeck as pdk
#AIzaSyDkQiL4C6R47BVNl0F6ZhOIlE4jKyF-2M0
# Set page title and layout
st.set_page_config(page_title="Alabama Counties", layout="wide")

# Data for 20 Alabama counties
data_race_high_income = {
    'County': [
        'Shelby County', 'Madison County', 'Limestone County', 'Baldwin County', 'Tuscaloosa County',
        'Jefferson County', 'Montgomery County', 'Elmore County', 'Lee County', 'Mobile County',

    ],
    'LAT': [
        33.2098, 34.7304, 34.7806, 30.7277, 33.2098,
        33.5207, 32.3668, 32.5644, 32.6020, 30.6954,

    ],
    'LON': [
        -86.6611, -86.5861, -86.9824, -87.7226, -87.5692,
        -86.8025, -86.3000, -86.0125, -85.4865, -88.0399,

    ]
}

data_race_low_income = {
    'County': [
        'Wilcox County', 'Perry County', 'Sumter County', 'Greene County', 'Bullock County',
        'Lowndes County', 'Dallas County', 'Macon County', 'Conecuh County', 'Hale County'
    ],
    'LAT': [

        31.9876, 32.6301, 32.6550, 32.8555, 32.1003,
        32.1565, 32.4073, 32.4043, 31.4340, 32.7585
    ],
    'LON': [

        -87.3080, -87.2970, -88.2005, -87.9568, -85.7124,
        -86.6074, -87.0241, -85.6920, -87.0968, -87.6324
    ]
}

# Convert data to DataFrame
df_counties_high = pd.DataFrame(data_race_high_income)
df_counties_low = pd.DataFrame(data_race_low_income)

# Create a map with PyDeck
st.title("Map of 20 Alabama Counties")
counties_layer = pdk.Layer(
    'ScatterplotLayer',
    data=df_counties_high,
    get_position='[LON, LAT]',
    get_fill_color='[142, 202, 230]',
    get_radius=10000,
    extruded=True,
    pickable=True
)

counties_layer2 = pdk.Layer(
    'ScatterplotLayer',
    data=df_counties_low,
    get_position='[LON, LAT]',
    get_fill_color='[251, 133, 0]',
    elevation_scale=50,
    get_radius=10000,
    pickable=True
)

view_state = pdk.ViewState(
    latitude=32.8067,
    longitude=-86.7911,
    zoom=6,
    pitch=0
)

counties_map = pdk.Deck(
    layers=[counties_layer, counties_layer2],
    initial_view_state=view_state,
    tooltip={
        'html': '<b>County:</b> {County}<br/><b>Income Level:</b> High' if '{County}' in df_counties_high[
            'County'].values else '<b>Income Level:</b> Low',
        'style': {
            'color': 'white'
        }
    }
)

st.pydeck_chart(counties_map)
