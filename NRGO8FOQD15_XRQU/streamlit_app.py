import streamlit as st
from snowflake.snowpark.context import get_active_session
session = get_active_session()

current_user = session.sql("SELECT CURRENT_USER()").collect()
current_role = session.sql("SELECT CURRENT_ROLE()").collect()

st.write(current_user)
st.write(current_role)

st.write(f"Streamlit version: {st.__version__}")
 