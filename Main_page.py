import streamlit as st
import pandas as pd 

st.markdown("# Pincode and Region Helper")
st.text(" This website helps you with finding the region of the pincode you selected with all the details provided like the head office, district name, etc and vice versa.")

st.text("Navigate to the pages using the sidebar...")
st.map()

# def main_page():
#     st.markdown("# Pincode finder")
#     st.sidebar.markdown("# Main Page")

# def page1():
#     st.markdown("# Pincode to Region finder")
#     st.sidebar.markdown("# Pincode to Region finder")

# def page2():
#     st.markdown("# Region to Pincode finder")
#     st.sidebar.markdown("# Region to Pincode finder")


# pages_name_to_funcs = {
#     "Main Page":main_page,
#     "Page 1" : page1,
#     "Page 2": page2
# }

# selected_page = st.sidebar.selectbox("Select a page", pages_name_to_funcs.keys())
# pages_name_to_funcs[selected_page]()
