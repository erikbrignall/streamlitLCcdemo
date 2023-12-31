# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 09:08:31 2022

@author: erikb
"""

import streamlit as st
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType

st.set_page_config(page_title='GA4 Analyser')
st.image('logo-temp2.PNG', width=200)
st.write('Please input a query for the bot')

openai_api_key = st.secrets["OpenAIapikey"]

# Page title

st.title('GA4 Analysis bot')

filename = 'origin_customers.csv'
df = pd.read_csv(filename) 
filename = 'products_sold.csv'
df1 = pd.read_csv(filename)
filename = 'Queries.csv'
df2 = pd.read_csv(filename)
dfs = [df,df1,df2]

## Generate LLM response
def generate_response(input_query):
  llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0, openai_api_key=openai_api_key)
  #df = load_csv(csv_file)
  # Create Pandas DataFrame Agent
  agent = create_pandas_dataframe_agent(llm, dfs, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)
  # Perform Query using the Agent
  response = agent.run(input_query)
  return st.success(response)

# Input widgets
#uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])
#question_list = [
  #'How many rows are there?',
  #'What is the range of values for MolWt with logS greater than 0?',
  #'How many rows have MolLogP value greater than 0.',
  #'Other']
#query_text = st.selectbox('Select an example query:', question_list, disabled=not uploaded_file)
# openai_api_key = st.text_input('OpenAI API Key', type='password', disabled=not (uploaded_file and query_text))
query_text = st.text_input('Enter Query')

# App logic
if query_text is 'Other':
  query_text = st.text_input('Enter your query:', placeholder = 'Enter query here ...', disabled=not uploaded_file)
if not openai_api_key.startswith('sk-'):
  st.warning('Please enter your OpenAI API key!', icon='⚠')
if openai_api_key.startswith('sk-') and query_text != "":
  st.header('Output')
  generate_response(query_text)
