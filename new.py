import streamlit as st

# Create buttons in columns
st.markdown("<h2>Horizontal Buttons using Columns</h2>", unsafe_allow_html=True)
st.markdown("<h3>Buttons in a horizontal layout using columns:</h3>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7= st.columns(7)  # Create 10 columns

# Place buttons in the columns
with col1:
    st.button("Button 1")

with col2:
    st.button("Button 2")

with col3:
    st.button("Button 3")

with col4:
    st.button("Button 4")

with col5:
    st.button("Button 5")

with col6:
    st.button("Button 6")

with col7:
    st.button("Button 7")

with col8:
    st.button("Button 8")

with col9:
    st.button("Button 9")

with col10:
    st.button("Button 10")


