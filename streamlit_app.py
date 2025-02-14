############## Constistuent.Online #################
####### Code-free analysis for curious folk. ######

### An application for ...

## streamlit run "C:\Users\Jack\Documents\Python_projects\streamlit_apps\google_dorker\streamlit_app.py"

### --------------------------------------- IMPORTS 

import datetime
import json
import math
import numpy as np
import pandas as pd
from pathlib import Path
import plotly.graph_objects as go
import re
import requests
import streamlit as st

pd.set_option('display.max_columns', None)

### 
headers = {
    "content-type": "application/json"
}

css = 'body, html, p, h1, .st-emotion-cache-1104ytp h1, [class*="css"] {font-family: "Inter", sans-serif;}'
st.markdown( f'<style>{css}</style>' , unsafe_allow_html= True)

### ---------------------------------------- FUNCTIONS 


### _________________________________________ RUN

st.markdown("**Open Investigation Tools** | [constituent.online](%s)" % 'http://www.constituent.online')
    
st.title('Google Dorker')
st.write('Lift your internet search game.')


### 

bools = ['AND', 'OR', None]

### Free text search
col1, col2 = st.columns([1,3])
with col1:
    st.write('')
    st.write('')
    st.write('Search for:')
with col2:
    row_4 = st.text_input('', 'Private', key = f'search_text_4',)
    
    if ' ' in row_4:    
        make_text_exact = st.checkbox('Search for exact phrase')
        if make_text_exact:
            row_4 = f'"{row_4}"'
        
    row_4 = row_4.replace(' ', '+')
    row_4 = row_4 + '+'
        

def make_row_bool(n, nx, example_text):
    
    col1, col2 = st.columns([1,3])
    with col1:
        search_type = st.selectbox('Choose:', (bools), index = nx, key = f'search_type_{n}', label_visibility = 'hidden')
        if search_type == None:
            search_type = ''
        else:
            search_type = search_type
        search_type = search_type + '+'
        
    with col2:
        search_text = st.text_input('', example_text, key = f'search_text_{n}',)
        
        if ' ' in search_text:
            make_text_exact = st.checkbox('Search for exact phrase?', key = f'checkbox_{n}')
            if make_text_exact:
                search_text = f'"{search_text}"'
            
        search_text = search_text.replace(' ', '+')
        
        
        
    row = ''
    if search_type == None or search_text == None or search_text == '':
        row = ''
    else:
        row = f'{search_type}{search_text}+'
                
    return row

row_5 = make_row_bool(5, 1, 'Confidential')
row_6 = make_row_bool(6, 0, 'Vietnam')


### Technical search

search_types = ['site', 'inurl', 'filetype', 'intitle', 'intext',  None]
search_text = ['.gov', '"TOP SECRET"', 'pdf']

st.write('')
st.write('')
st.write('With these requirements:')

def make_row(n, example_text):
    
    col1, col2 = st.columns([1,3])
    with col1:
        search_type = st.selectbox('Choose:', (search_types), index = n,  key = f'search_type_{n}', label_visibility = 'hidden')
      
    with col2:
        search_text = st.text_input('', example_text, key = f'search_text_{n}',)
        search_text = search_text.replace(' ', '+')
        
    row = ''
    if search_type == None or search_text == None or search_text == '':
        row = ''
    else:
        search_type = search_type + ':'
        row = f'{search_type}{search_text}+'
        
    return row
        
row_0 = make_row(1, search_text[0])
row_1 = make_row(3, search_text[1])
row_2 = make_row(2, search_text[2])
row_3 = ''


### Dates 
date_q = ''
st.write('')
st.write('')
set_date_range = st.checkbox('Set a date range?')
if set_date_range:
    col1, col2 = st.columns([2,2])
    with col1:
        start_date = st.date_input("Start search at", datetime.date(2000, 1, 1))
    with col2:
        end_date = st.date_input("Start search at", None)
    date_q = f'&tbs=cdr:1,cd_min:{start_date.month}/{start_date.day}/{start_date.year},cd_max:{end_date.month}/{end_date.day}/{end_date.year}'



### How many results to return?
col1, col2 = st.columns([1,3])
with col1:
    st.write('')
    st.write('')
    st.write('Return up to 100 results per page')
with col2:
    results_per_page = st.slider('', 0, 100, 100)  


    
### Compile
base_url = 'https://www.google.com/search?q='
query = row_0 + row_1 + row_2 + row_3 + row_4 + row_5 + row_6 + f'&num={results_per_page}' + date_q
url = base_url + query



st.write('')
st.write('')
st.write('Click on this and see what Google returns  &#x2935;')
st.markdown(f'<p class="result"><a href={url}>{url}</a></p>', unsafe_allow_html=True)
st.markdown("""<style>.result {font-size:16px !important; font-family: Consolas; background-color: #efefef; padding: 10px; margin: 0;}</style>""", unsafe_allow_html=True)
