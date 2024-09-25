# import packages
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
sns.set()

# show the title
st.title('Titanic App by Kaiqi Zhou')

# read csv and show the dataframe
df=pd.read_csv('train.csv')


# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
# Import necessary packages

# Create a figure with three subplots, size should be (15, 5)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))


fig.suptitle('Ticket Price Distribution by Class')

# Plot box plots for each ticket class
sns.boxplot(data=df, x='Pclass', y='Fare', ax=axes[0])
axes[0].set_title('Ticket Price by Class')
axes[0].set_xlabel('Ticket Class')
axes[0].set_ylabel('Fare')

# Plot box plots for ticket price with respect to gender
sns.boxplot(data=df, x='Sex', y='Fare', ax=axes[1])
axes[1].set_title('Ticket Price by Gender')
axes[1].set_xlabel('Gender')
axes[1].set_ylabel('Fare')

# Plot box plots for ticket price with respect to survival status
sns.boxplot(data=df, x='Survived', y='Fare', ax=axes[2])
axes[2].set_title('Ticket Price by Survival Status')
axes[2].set_xlabel('Survived (0 = No, 1 = Yes)')
axes[2].set_ylabel('Fare')

# Display the plot in Streamlit
st.pyplot(fig)

