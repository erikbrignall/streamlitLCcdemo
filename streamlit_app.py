# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 09:08:31 2022

@author: erikb
"""

import streamlit as st
import pandas as pd
import pandas as pd 
#import matplotlib.pyplot as plt 
#import seaborn as sns 
from langchain.agents import create_pandas_dataframe_agent 
from langchain.llms import OpenAI 
from langchain.chat_models import ChatOpenAI

filename = 'origin_customers.csv'
df = pd.read_csv(filename) 
filename = 'products_sold.csv'
df1 = pd.read_csv(filename) 
dfs = [df,df1]

st.image('logo-temp2.PNG', width=200)
st.title('🦜🔗 GA4 Analysis Bot')

openai_api_key = st.secrets["OpenAIapikey"]

def generate_response(input_text):
  #llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  agent = create_pandas_dataframe_agent(OpenAI(temperature=0, model_name='gpt-3.5-turbo',openai_api_key=openai_api_key), dfs, verbose=True)
  #st.info(llm(input_text))
  st.info(agent(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
