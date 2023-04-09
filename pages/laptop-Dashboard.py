import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

#IMAGE_PATH = os.path.join(dir_of_interest, "images", "iris.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "df.csv")

st.title("Dashboard - Laptop Data")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "lap.jpg")
img = image.imread(IMAGE_PATH)
st.image(img)


# img = image.imread(IMAGE_PATH)
# st.image(img)

df = pd.read_csv(DATA_PATH)
df.drop(labels='Unnamed: 0',axis=1,inplace=True)
st.dataframe(df)



col1, col2 ,col3 ,col4 ,col5= st.columns(5)

fig_1 = px.scatter(df, x='Ram_1', y='Price')
col1.plotly_chart(fig_1, use_container_width=True)

#avg_price_by_brand = df.groupby('Brand')['Price'].mean().reset_index()
fig_2 = px.box(df, x='Touch_Screen', y='Price')
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.box(df, x='Operating_System', y='Price')
col3.plotly_chart(fig_3, use_container_width=True)

fig_4 = px.bar(df, x='Processor', y='Price')
col4.plotly_chart(fig_4, use_container_width=True)

fig_5 = px.strip(df, x='SSD', y='Price')
col5.plotly_chart(fig_5, use_container_width=True)

st.subheader("Factors Effecting Price of Laptop")
st.write('''1.RAM and storage: More RAM and storage will generally increase the price of a laptop.\n
2.Processor: The processor is the "brain" of the laptop, and a more powerful processor will generally result in a more expensive laptop.\n
3.Operating system: Laptops with certain operating systems, such as macOS, tend to be more expensive than those with other operating systems like Windows.\n
4.Laptops with touchscreen tend to be slightly more expensive than those without touchscreen, as the median price for touchscreen laptops is higher than that for non-touchscreen laptops.
''')