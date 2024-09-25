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

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
sns.boxplot(data=df[df['Pclass'] == 1], x='Pclass', y='Fare', ax=axes[0])
axes[0].set_title('Ticket Price for 1st Class')
axes[0].set_xlabel('Class')
axes[0].set_ylabel('Ticket Price')

# Box plot for 2nd class
sns.boxplot(data=df[df['Pclass'] == 2], x='Pclass', y='Fare', ax=axes[1])
axes[1].set_title('Ticket Price for 2nd Class')
axes[1].set_xlabel('Class')
axes[1].set_ylabel('Ticket Price')

# Box plot for 3rd class
sns.boxplot(data=df[df['Pclass'] == 3], x='Pclass', y='Fare', ax=axes[2])
axes[2].set_title('Ticket Price for 3rd Class')
axes[2].set_xlabel('Class')
axes[2].set_ylabel('Ticket Price')

# Adjust layout
plt.tight_layout()

# Display the figure in Streamlit
st.pyplot(fig)
