# streamlit_app.py 

import streamlit as st

# Establish Snowflake connection
conn = st.connection("snowflake")

# Query from the correct database and table
df = conn.query("SELECT * FROM PETS.PUBLIC.MYTABLE", ttl="10m")  # Replace with actual table name

# Display results
st.write("Pets Data:")
for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")  # Ensure column names match your actual table
