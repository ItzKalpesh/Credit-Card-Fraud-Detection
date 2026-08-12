import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Credit Card Fraud Detection - Visualization")
st.write("Student level ML project visualization")

df = pd.read_csv("creditcard_2023.csv")

st.subheader("Dataset Preview")
st.write(df.head())

# Bar graph to show fraud vs non-fraud transactions
st.subheader("Fraud vs Non-Fraud Transactions")
fig1, ax1 = plt.subplots()
sns.countplot(x='Class', data=df, ax=ax1)
ax1.set_xlabel("Class (0 = Normal, 1 = Fraud)")
ax1.set_ylabel("Count")
st.pyplot(fig1)

# Histogram to show distribution of transaction amount
st.subheader("Transaction Amount Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(df['Amount'], bins=50, ax=ax2)
ax2.set_xlabel("Transaction Amount")
st.pyplot(fig2)

# Box plot to compare amount for fraud and non-fraud
st.subheader("Amount vs Transaction Type")
fig3, ax3 = plt.subplots()
sns.boxplot(x='Class', y='Amount', data=df, ax=ax3)
ax3.set_xlabel("Class")
ax3.set_ylabel("Amount")
st.pyplot(fig3)

# Heatmap to show correlation between features
st.subheader("Correlation Heatmap")
corr = df.corr()
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, cmap='coolwarm', ax=ax4)
st.pyplot(fig4)

st.write("Visualization done using Streamlit, Seaborn and Matplotlib")
