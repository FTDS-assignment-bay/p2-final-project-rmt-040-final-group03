import streamlit as st
import pandas as pd
import datetime
import pickle

# Load model
with open('model_lr.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

def run():
    st.title("Estimated Ad Performance and Transaction Metrics Form")
    with st.form(key = "marketing_form"):
        st.subheader("Customer Transaction and Ad Performance Form")
        st.write("Please fill in the following transaction and advertising details.")
        st.markdown('---')

        st.markdown("#### 📋 Basic Information")
        transaction_date = st.date_input("Transaction Date", value = datetime.date.today())
        category = st.selectbox("Category", ["Electronics", "Toys", "Home Appliances", "Clothing", "Books"])
        region = st.selectbox("Region", ["Asia", "Europe", "North America"])
        st.markdown('---')

        st.markdown("#### 💵 Sales Metrics")
        units_sold = st.number_input("Units Sold", min_value = 0, step = 1)
        discount_applied = st.slider("Discount Applied (%)", 0.0, 100.0, step = 0.1)
        revenue = st.number_input("Revenue", min_value = 0.0, step = 50.0, help = "Total income from sales in currency")
        st.markdown('---')

        st.markdown("#### 👩🏻‍💻 Advertising Metrics")
        st.write("Fill in the values based on your goals for the campaign, such as the desired number of clicks, impressions, conversion rate, and cost-per-click (CPC).")
        col1, col2 = st.columns(2)
        with col1:
            clicks = st.number_input("Clicks", min_value = 0, step = 1)
        with col2:
            impressions = st.number_input("Impressions", min_value = 0, step = 1)
        conversion_rate = st.number_input("Conversion Rate (%)", min_value = 0.0, max_value = 100.0, step = 0.1)
        col3, col4 = st.columns(2)
        with col3:
            ad_ctr = st.number_input("Ad CTR (%)", min_value =  0.0, max_value = 100.0, step = 0.1)
        with col4:
            ad_cpc = st.number_input("Ad CPC", min_value =  0.0, step = 0.01)
        st.markdown('---')

        submitted = st.form_submit_button("Submit!")

    data = {
        "units_sold": units_sold,
        "discount_applied": discount_applied,
        "revenue": revenue,
        "clicks": clicks,
        "impressions": impressions,
        "conversion_rate": conversion_rate,
        "category": category,
        "region": region,
        "ad_ctr": ad_ctr,
        "ad_cpc": ad_cpc,
        "transaction_date_update": transaction_date
    }

    data = pd.DataFrame([data])
    st.dataframe(data)

    if submitted:
        st.success("Data submitted successfully!")
        predict = loaded_model.predict(data)
        st.subheader("🔍 Predicted result")
        st.metric(label = "Estimated Budget Required", value = round(predict[0], 5))

if __name__ == '__main__':
    run()