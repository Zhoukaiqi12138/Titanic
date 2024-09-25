# import packages
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
sns.set()

# show the title
st.title('Titanic App by Kaiqi Zhou')

# read csv and show the dataframe
df=pd.read_csv('train.csv')


# Create a figure for the first subplot: Box plot of ticket prices by class
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='Pclass', y='Fare')
plt.title('Ticket Price by Class')
plt.xlabel('Class')
plt.ylabel('Ticket Price')

# Display the figure in Streamlit
st.pyplot(plt)

