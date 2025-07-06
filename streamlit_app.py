import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="House Price Predictor", layout="wide")

# Load model and supporting files
@st.cache_resource
def load_model():
    try:
        model = joblib.load("house_price_model.pkl")
        scaler = joblib.load("house_price_scaler.pkl")
        feature_info = joblib.load("feature_info.pkl")
        return model, scaler, feature_info
    except:
        return None, None, None

model, scaler, feature_info = load_model()

# Title
st.title(" House Price Prediction App")
st.write("This app predicts house prices using a Linear Regression model trained on California housing data.")

# Sidebar Inputs
st.sidebar.header("Input House Features")


inputs = {
        'MedInc': st.sidebar.slider("Median Income (in $10k)", 0.5, 15.0, 5.0, 0.1),
        'HouseAge': st.sidebar.slider("House Age (years)", 1, 50, 20),
        'AveRooms': st.sidebar.slider("Average Rooms", 3.0, 12.0, 6.0, 0.1),
        'AveBedrms': st.sidebar.slider("Average Bedrooms", 0.5, 3.0, 1.1, 0.1),
        'Population': st.sidebar.slider("Population", 500, 10000, 3000, 100),
        'AveOccup': st.sidebar.slider("Average Occupancy", 1.0, 8.0, 3.0, 0.1),
        'Latitude': st.sidebar.slider("Latitude", 32.0, 42.0, 34.0, 0.1),
        'Longitude': st.sidebar.slider("Longitude", -125.0, -114.0, -118.0, 0.1),
    }

# Derived features
inputs['rooms_per_person'] = inputs['AveRooms'] / inputs['AveOccup']
inputs['bedrooms_per_room'] = inputs['AveBedrms'] / inputs['AveRooms']
inputs['population_density'] = inputs['Population'] / (inputs['AveOccup'] * 100)

# Prediction
if st.sidebar.button(" Predict House Price"):
    if model and scaler:
        input_df = pd.DataFrame([inputs])
        input_scaled = scaler.transform(input_df[feature_info["feature_names"]])
        prediction = model.predict(input_scaled)[0]

        st.subheader(" Predicted House Price")
        st.success(f"Estimated Price: **${prediction * 100:.0f}k**")

        # Summary
        st.subheader(" Input Summary")
        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Median Income**: ${inputs['MedInc'] * 10:.0f}k")
            st.write(f"**House Age**: {inputs['HouseAge']} years")
            st.write(f"**Avg. Rooms**: {inputs['AveRooms']}")
            st.write(f"**Avg. Bedrooms**: {inputs['AveBedrms']}")
            st.write(f"**Population**: {inputs['Population']}")
            st.write(f"**Avg. Occupancy**: {inputs['AveOccup']}")

        with col2:
            st.write(f"**Latitude**: {inputs['Latitude']}")
            st.write(f"**Longitude**: {inputs['Longitude']}")
            st.write(f"**Rooms per Person**: {inputs['rooms_per_person']:.2f}")
            st.write(f"**Bedrooms per Room**: {inputs['bedrooms_per_room']:.2f}")
            st.write(f"**Population Density**: {inputs['population_density']:.2f}")

        # Graph: Comparison with CA average
        st.subheader(" Price Comparison")

        comparison_data = pd.DataFrame({
            "Category": ["Your House", "CA Average", "CA Median"],
            "Price (in $1000s)": [prediction * 100, 350, 280],
            "Type": ["Prediction", "Reference", "Reference"]
            })

        fig = px.bar(
                comparison_data,
                x="Category",
                y="Price (in $1000s)",
                color="Type",
                color_discrete_map={"Prediction": "#1f77b4", "Reference": "#ff7f0e"},
                title="Predicted vs Average House Prices"
            )
        st.plotly_chart(fig, use_container_width=True)

            # Feature Importance
        st.subheader("🔍 What Affects House Prices?")

        importance_data = pd.DataFrame({
                "Feature": ["Median Income", "Latitude/Longitude", "House Age", "Rooms", "Population Density"],
                "Impact": ["Very High", "High", "Medium", "Medium", "Low"],
                "Why it matters": [
                    "Higher income = more expensive houses",
                    "Location influences price (coastal is costlier)",
                    "Newer houses often cost more",
                    "More rooms → larger and costlier",
                    "Dense areas may increase demand"
                ]
            })

        st.dataframe(importance_data, use_container_width=True)

# About the model
st.markdown("---")
st.subheader("ℹ️ About the Model")

st.markdown("""
- **Model Type**: Linear Regression  
- **Dataset**: California Housing (20,000+ entries)  
- **Features Used**: 11 (including engineered ones like rooms per person)  
- **R² Score**: ~0.60 → Model explains ~60% of price variation  
- **Limitations**:
  - Based only on California data
  - Prices are in units of $100,000 (multiply prediction by 100)
  - Assumes a linear relationship between features and price
""")
