# 📊 BudgetIn – Smart Advertising Budget Recommendation App

## 📌 Project Overview
In today’s highly competitive digital era, the e-commerce industry is experiencing rapid growth, leading to the emergence of many new businesses. However, many early-stage e-commerce ventures struggle to manage and allocate their advertising budgets effectively. This challenge often stems from a lack of experience in digital marketing strategies and the high costs of advertising across multiple digital platforms. Poor budget allocation not only results in wasted expenses, but also negatively affects business growth, brand awareness, and conversion rates.

**BudgetIn** is a machine learning-based web application that helps early-stage e-commerce businesses optimize their advertising budget. It predicts the necessary ad spend based on business-related parameters, helping users allocate their budgets more effectively and avoid wasted spending.

This project was developed as part of the final group assignment at Hacktiv8 Data Science Bootcamp.

---

## 📁 Repository Outline
| Name | Type | Description |
|------|------|-------------|
| `deployment/` | Folder | Contains the deployment code and files for launching the app on Hugging Face Spaces using Streamlit. |
| `cleaned_data.csv` | File | Final cleaned dataset containing 5,000 rows and 12 columns. |
| `data_analyst.ipynb` | Notebook | Contains exploratory data analysis and visualizations to uncover patterns and trends. |
| `data_engineer.py` | Script | ETL pipeline script for data extraction, transformation, and loading using Airflow and PostgreSQL. |
| `notebook_inference.ipynb` | Notebook | Inference notebook for testing the trained model with new input data. |
| `notebook_modeling.ipynb` | Notebook | Contains the modeling process including feature engineering, training, tuning, and evaluation. |
| `raw_data.csv` | File | Original dataset with 5,000 records and 15 columns, prior to cleaning. |
| `url.txt` | File | Contains URLs to the final Tableau dashboard and Hugging Face app deployment. |

---

## 📊 Data
- **Original Dataset**: 5,000 entries with 15 columns.
- **Cleaned Dataset**: Still 5,000 entries (no duplicates), reduced to **12 columns** after removing irrelevant or redundant fields.
- Dataset includes key information such as ad impressions, clicks, CPC, revenue, product category, region, and more.

---

## 🔁 Method

1. **Data Extraction**  
   - Data is retrieved from a PostgreSQL table via a Python-based ETL script scheduled using Apache Airflow.

2. **Data Cleaning & Transformation**  
   - Unnecessary columns are dropped, and data types are standardized.
   - Feature engineering includes the creation of `transaction_date_update` (Month-Year format)

3. **Modeling**  
   - Linear Regression and Random Forest models are trained to predict advertising ROI.
   - Model performance is evaluated using **Mean Absolute Error (MAE)** and **R² Score**.

4. **Deployment**  
   - The final model is deployed using Streamlit and hosted on **Hugging Face Spaces**, allowing users to test real-time predictions interactively.

5. **Dashboarding**  
   - Tableau is used to create a supporting dashboard with charts and insights based on the cleaned dataset.

---

## ✅ Output
- An interactive **web app on Hugging Face Spaces** to recommend advertising budgets.
- A **Tableau dashboard** visualizing historical patterns in ad performance, conversions across categories and regions.
- All files and outputs are organized and documented in this repository for clarity and reproducibility.

---

## 👥 Team Members
- **M. Wahyu Ghifari** - Data Analysr
- **Nadhira Gunawan** – Data Engineer  
- **Revi Naufal Hisyam** – Data Scientist
- **Yelina Kusuma** – Data Scientist  

---

## 📚 Acknowledgements
- Dataset: [Comprehensive Synthetic E-commerce Dataset – Kaggle](https://www.kaggle.com/datasets/imranalishahh/comprehensive-synthetic-e-commerce-dataset)
- Hacktiv8 Data Science Bootcamp
