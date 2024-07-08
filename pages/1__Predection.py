import streamlit as st
import pickle
import time
from streamlit_lottie import st_lottie
import json

st.set_page_config(
    page_title="Prediction",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)

def load_lottie_file(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)
# Replace 'path_to_your_lottie_file.json' with the actual file path
lottie_animation = load_lottie_file('predection_animation.json')

# Display the Lottie animation in Streamlit
st_lottie(lottie_animation, height=300, key="prediction")


model = pickle.load(open('model.pkl', 'rb'))

store_types = {
    "Apparel": 1,
    "Accessories": 2,
    "Shoes": 3,
    "Electronics": 4,
    "Home Appliances": 5,
    "Furniture": 6,
    "Home Decor": 7,
    "Sporting Goods": 8,
    "Toys": 9,
    "Books": 10,
    "Stationery": 11,
    "Beauty Products": 12,
    "Jewelry": 13,
    "Watches": 14,
    "Handbags": 15,
    "Luggage": 16,
    "Pet Supplies": 17,
    "Garden Supplies": 18,
    "Automotive": 19,
    "Hardware": 20,
    "Kitchenware": 21,
    "Bedding": 22,
    "Bath": 23,
    "Lighting": 24,
    "Mattresses": 25,
    "Baby Products": 26,
    "Health Supplies": 27,
    "Pharmacy": 28,
    "Optical": 29,
    "Music and Movies": 30,
    "Gifts and Novelties": 31,
    "Party Supplies": 32,
    "Craft Supplies": 33,
    "Art Supplies": 34,
    "Office Supplies": 35,
    "Computers": 36,
    "Mobile Phones": 37,
    "Photography": 38,
    "Appliances Repair": 39,
    "Cosmetics": 40,
    "Perfumes": 41,
    "Snacks and Beverages": 42,
    "Groceries": 43,
    "Deli": 44,
    "Bakery": 45
}

# Most Important Features

col1 , col2 = st.columns(2)

with col1:
    store = st.selectbox('Store Type : ', list(store_types.keys()),help="Select Store Type")
    store = store_types[store]

    cpi = st.number_input('CPI : ', min_value=125, max_value=230,help="Consumer Price Index")

    Unemployment = st.number_input('Unemployment Rate: ', min_value=3, max_value=15,help="Unemployment Rate for the Region")

with col2:
    date = st.date_input("Select Date : ",help="Date of Sales")
    month = date.month

    fuel_price = st.number_input('Fuel Price : ', min_value=2, max_value=5,help="Cost of fuel in the Region")

    temperature = st.number_input('Temperature (Celsius): ', min_value=-10, max_value=100,help="Temperature in the Region")



final_prediction = model.predict([[store, month, cpi, Unemployment, fuel_price, temperature]])

st.divider()

if st.button('Predict', help="Click here to predict the Sales"):
    time.sleep(3)
    st.success(f'Predicted Sales : {final_prediction[0].round(2)} USD')

