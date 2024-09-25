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


# Create a figure for the first class (1st class)
plt.figure(figsize=(10, 5))
sns.boxplot(data=df[df['Pclass'] == 1], x='Pclass', y='Fare')
plt.title('Ticket Price for 1st Class')
plt.xlabel('Class')
plt.ylabel('Ticket Price')
st.pyplot(plt)  # Display the first class plot

# Create a figure for the second class (2nd class)
plt.figure(figsize=(10, 5))
sns.boxplot(data=df[df['Pclass'] == 2], x='Pclass', y='Fare')
plt.title('Ticket Price for 2nd Class')
plt.xlabel('Class')
plt.ylabel('Ticket Price')
st.pyplot(plt)  # Display the second class plot

# Create a figure for the third class (3rd class)
plt.figure(figsize=(10, 5))
sns.boxplot(data=df[df['Pclass'] == 3], x='Pclass', y='Fare')
plt.title('Ticket Price for 3rd Class')
plt.xlabel('Class')
plt.ylabel('Ticket Price')
st.pyplot(plt)  # Display the third class plot
