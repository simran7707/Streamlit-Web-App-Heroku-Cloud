# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import seaborn as sns


st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")

#upload dataset
upload=st.file_uploader("Upload your Dataset(In CSV Format)")

if upload is not None:
    data=pd.read_csv(upload)
    
#show dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
        
#chk data type of each col

if upload is not None:
    if st.checkbox("Datatype of each column"):
        st.text("Datatypes")
        st.write(data.dtypes)
        
# Find Shape of dataset       
if upload is not None:
    data_shape=st.radio("What Dimension Do you want to check?",('Rows','Columns'))

    if data_shape=='Rows':
        st.text('Number of rows')
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text('Number of Columns')
        st.write(data.shape[1])
            
#find null values
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null values in dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("conngratulations!!,No Missing Values")         
            
        
# find duplicate values in dataset     
if upload is not None:
    test = data.duplicated().any()
    if test == True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup = st.selectbox(
            "Do you want to remove duplicate values?",
            ("Select one", "Yes", "No")
        )
        
        if dup == 'Yes':
            data = data.drop_duplicates()
            st.text("Duplicates Values are removed")
        if dup == "No":
            st.text("ok no problem")


#Get overall Stats
if upload is not None:
    if st.checkbox("Summary of the dataset"):
        st.write(data.describe(include='all'))
        
#about section
if st.button('About App'):
    st.text("Build with Streamlit")
    st.text('Thanks to streamlit')
    
 #By
if st.checkbox('By'):
    st.success('Simran')   

            
            
        
        