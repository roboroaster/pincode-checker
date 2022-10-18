import streamlit as st
import pandas as pd 
st.sidebar.title("Region to Pincode")
df = pd.read_csv("all_india_PO_list_without_APS_offices_ver2_lat_long.csv")
st.header("pincode detail checker")
st.text("enter your pincode to get the details: ")
# pincode = st.text_input("enter the pincode here")
distrticts = df['Districtname'].unique()
pincode = st.selectbox(label="enter the district name",options=distrticts)
# pincode = st.text_input("enter the district name here:")

ok_button = st.button("Submit")
if ok_button:
    # st.dataframe(df[df['pincode'] == int(pincode)])
    st.dataframe(df[df['Districtname'] == pincode])
    st.map(df[df['pincode'] == int(pincode)])