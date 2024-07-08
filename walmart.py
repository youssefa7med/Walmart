import streamlit as st
from streamlit_lottie import st_lottie
import json

# Set page configuration with the prediction icon
st.set_page_config(
    page_title="Walmart Sales Prediction",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS to use full width and height
st.markdown(
    """
    <style>
    .css-18e3th9 {
        padding-top: 1rem;
        padding-right: 1rem;
        padding-bottom: 1rem;
        padding-left: 1rem;
    }
    .css-1d391kg {
        padding-top: 1rem;
        padding-right: 1rem;
        padding-bottom: 1rem;
        padding-left: 1rem;
    }
    h2 {
        color: #4CAF50;
        text-align: center;
        font-family: 'Arial', sans-serif;
        margin-top: 1.5rem;
    }
    h3 {
        color: #2E8B57;
        font-family: 'Arial', sans-serif;
        margin-top: 1.0rem;
        margin-bottom: 1.0rem;
    }
    p {
        font-family: 'Arial', sans-serif;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def load_lottie_file(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

# Replace 'path_to_your_lottie_file.json' with the actual file path
lottie_animation = load_lottie_file('walmart_animation.json')

# Display the Lottie animation in Streamlit
st_lottie(lottie_animation, height=300, key="shopping_cart")

# Add your markdown content here
st.markdown("<h2>Walmart Sales Prediction Using Machine Learning</h2>", unsafe_allow_html=True)

st.divider()

st.markdown("""
<h3>Introduction</h3>
<p>This project aims to predict sales for Walmart stores using historical sales data. The goal is to develop a machine learning model that can accurately forecast future sales, helping Walmart optimize their inventory and staffing.</p>

<h3>Dataset</h3>
<p>The dataset used for this project is sourced from Kaggle and contains historical sales data from Walmart. It includes the following key features:</p>
<ul>
    <li><b>Store</b>: The store number.</li>
    <li><b>Date</b>: The week of sales.</li>
    <li><b>Weekly_Sales</b>: Sales for the given store and date.</li>
    <li><b>Holiday_Flag</b>: Whether the week is a special holiday week (1) or not (0).</li>
    <li><b>Temperature</b>: Temperature in the region.</li>
    <li><b>Fuel_Price</b>: Cost of fuel in the region.</li>
    <li><b>CPI</b>: Consumer Price Index.</li>
    <li><b>Unemployment</b>: Unemployment rate.</li>
</ul>
<p>You can find the dataset <a href='https://www.kaggle.com/datasets/yasserh/walmart-dataset'>here</a>.</p>

<h3>Data Exploration</h3>
<p>Before building the prediction model, it's important to explore and understand the dataset. This involves:</p>
<ul>
    <li>Checking for missing values.</li>
    <li>Visualizing sales trends over time.</li>
    <li>Analyzing the impact of holidays on sales.</li>
    <li>Investigating correlations between sales and other features.</li>
</ul>

<h3>Model Development</h3>
<p>For this project, we use several machine learning algorithms to predict weekly sales. The steps involved are:</p>
<ol>
    <li><b>Data Preprocessing</b>: Cleaning the data, handling missing values, and feature engineering.</li>
    <li><b>Model Selection</b>: Trying out different algorithms such as Linear Regression, Decision Tree, Support Vector Regression(SVR) , K-Nearest Neighbors (KNN), and Decision Tree Regressor.</li>
    <li><b>Training and Evaluation</b>: Training the models on the dataset and evaluating their performance using metrics like R2 Score and Root Mean Squared Error (RMSE).</li>
</ol>

<h3>Streamlit Application</h3>
<p>The project includes a Streamlit application that allows users to interact with the prediction model. The app provides:</p>
<ul>
    <li>A user-friendly interface to input new data.</li>
    <li>Visualization of the prediction results.</li>
    <li>Insights and analysis based on the input data.</li>
</ul>

<h3>How to Run the App</h3>
<p>To run the Streamlit application, follow these steps:</p>
<ol>
    <li>Clone the repository:</li>
    <pre><code>git clone &lt;repository-url&gt;</code></pre>
    <li>Navigate to the project directory:</li>
    <pre><code>cd walmart-sales-prediction</code></pre>
    <li>Install the required dependencies:</li>
    <pre><code>pip install -r requirements.txt</code></pre>
    <li>Run the Streamlit app:</li>
    <pre><code>streamlit run app.py</code></pre>
</ol>

<h3>Conclusion</h3>
<p>This project demonstrates the application of machine learning techniques to predict retail sales. By leveraging historical sales data and various features, we can build models that help in making informed business decisions. The Streamlit application provides an intuitive way to interact with the model and gain insights from the predictions.</p>

<h3>Future Work</h3>
<ul>
    <li><b>Model Improvement</b>: Experimenting with more advanced algorithms and hyperparameter tuning.</li>
    <li><b>Feature Expansion</b>: Including additional features such as promotional events and competitor pricing.</li>
    <li><b>Real-time Predictions</b>: Integrating the model with live data sources for real-time sales forecasting.</li>
</ul>

<h3>Acknowledgements</h3>
<p>Special thanks to <a href='https://www.kaggle.com/'>Kaggle</a> for providing the dataset used in this project.</p>

<h2>Final Score</h2>
<p>I achieved a score of 93% in this project.</p>
""", unsafe_allow_html=True)
