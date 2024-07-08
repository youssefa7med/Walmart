
# Walmart Sales Prediction Using Machine Learning
---
#[streamlit](https://walmart-predection.streamlit.app/)
---
## Overview

This project aims to predict Walmart sales using machine learning. By analyzing various features such as store type, Consumer Price Index (CPI), unemployment rate, fuel price, and temperature, we can estimate the sales for a given period. This predictive model can help Walmart optimize inventory, staffing, and marketing strategies.

## Features

- **Date Selection:** Users can select a date to predict sales for that specific month.
- **Store Type:** Choose from 45 different store types to see how they impact sales.
- **Consumer Price Index (CPI):** Enter the CPI value to understand its effect on sales.
- **Unemployment Rate:** Input the regional unemployment rate.
- **Fuel Price:** Include the cost of fuel in the region.
- **Temperature:** Account for regional temperature variations.

## Usage

To use this project, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/walmart-sales-prediction.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd walmart-sales-prediction
    ```

3. **Install the Required Packages:**

    Make sure you have Python installed. Then, install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit Application:**

    ```bash
    streamlit run app.py
    ```

5. **Use the Application:**

    - Open your web browser and navigate to `http://localhost:8501`.
    - Select the store type, CPI, unemployment rate, fuel price, and temperature.
    - Click on the **Predict** button to get the sales prediction.

## Model

The machine learning model used in this project is trained on historical sales data. It leverages the following features:

- Store Type
- Month
- Consumer Price Index (CPI)
- Unemployment Rate
- Fuel Price
- Temperature

## Performance

The model achieves an accuracy of **93%** on the test dataset, making it a reliable tool for sales prediction.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or inquiries, please contact [Youssef Ahmed](mailto:yaa2003ya@gmail.com).

---
