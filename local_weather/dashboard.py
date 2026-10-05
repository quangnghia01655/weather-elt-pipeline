import streamlit as st
import duckdb

# 1. setup Streamlit page configuration
st.set_page_config(page_title="Weather Data Pipeline", page_icon="🌤️", layout="wide")

st.title(" Automated Weather Data Pipeline")
st.markdown("_Data extracted from OpenWeatherMap API & Transformed via dbt & DuckDB_")

# 2. create a function to load data from DuckDB and cache it for performance
@st.cache_data 
def load_data():
    conn = duckdb.connect('weather_warehouse.duckdb')
    return conn.execute("SELECT * FROM stg_daily_weather").df()

df = load_data()

# 3. create a sidebar for user input to filter data
st.sidebar.header("Filter Options")
selected_city = st.sidebar.multiselect(
    "Select cities:",
    options=df['city'].unique(),
    default=df['city'].unique()
)

# filter the DataFrame based on user selection
df_filtered = df[df['city'].isin(selected_city)]

# 4. display key metrics in a 3-column layout
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Highest Temperature", f"{df_filtered['temp_celsius'].max()} °C")
with col2:
    st.metric("Average Humidity", f"{int(df_filtered['humidity_pct'].mean())} %")
with col3:
    st.metric("Total Records", f"{len(df_filtered)} records")

st.divider()

# 5. layout for bar chart and data table side by side
col_chart, col_table = st.columns([3, 2]) # set the width ratio for chart and table

with col_chart:
    st.subheader("Temperature Distribution by City")
    st.bar_chart(data=df_filtered, x='city', y='temp_celsius')

with col_table:
    st.subheader("Additional Weather Data")
    # render the filtered DataFrame as a table without the index
    st.dataframe(
        df_filtered[['city', 'temp_celsius', 'humidity_pct', 'condition_desc']], 
        hide_index=True
    )