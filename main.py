import numpy as np
import pandas as pd
import matplotlib
import json
import requests
import plotly.express as px

api_url_base = 'https://api.opencovid.ca/'


api_url_base = 'https://api.opencovid.ca/summary?stat=cases'
response = requests.get(api_url_base)
data = response.json()
df = pd.json_normalize(data['summary'])
print(df)


fig = px.pie(df, values='active_cases', names='province', title='Current Covid19 Cases in Canada By Province')
fig.show()

