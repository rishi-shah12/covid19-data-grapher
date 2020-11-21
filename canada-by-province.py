import numpy as np
import pandas as pd
import matplotlib
import json
import requests
import plotly.express as px

#API base link
api_url_base = 'https://api.opencovid.ca/'

#Get JSON for active cases per province
response_cases = requests.get(api_url_base + 'summary?stat=cases')
data_cases = response_cases.json()
df_cases = pd.json_normalize(data_cases['summary'])

#Get JSON for total deaths per province
response_deaths = requests.get(api_url_base + 'summary?stat=deaths')
data_deaths = response_deaths.json()
df_deaths = pd.json_normalize(data_deaths['summary'])

#Get daily new cases in Canada
response_daily_cases = requests.get(api_url_base + 'summary?after=01-03-2020&loc=canada')
data_daily_cases = response_daily_cases.json()
df_daily_cases = pd.json_normalize(data_daily_cases['summary'])

#Make a PI Chart for active cases
fig_cases = px.pie(df_cases, values='active_cases', names='province', title='Current Covid19 Cases in Canada By Province')
fig_cases.show()

#Make a PI Chart for total deaths per province
fig_deaths = px.pie(df_cases, values='cumulative_deaths', names='province', title='Current Covid19 Deaths in Canada By Province')
fig_deaths.show()

#Make a line graph for cases vs. date
fig_daily_cases = px.line(df_daily_cases, x="date", y="cases", title='New Daily Covid19 Cases in Canada')
fig_daily_cases.show()



