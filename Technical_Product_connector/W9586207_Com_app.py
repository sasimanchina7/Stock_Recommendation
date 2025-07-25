import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import streamlit as st
import time 

# For time stamps
from datetime import datetime

import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

# For time stamps
from datetime import datetime


# The computer software and service tech stocks we'll use for this analysis from yfinance as tickers(which are codes represented by the companies)
tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN','GOOGL','LNKD','PYPL','TWTR','EBAY','BIDU','SAP','CRM','ADBE','VMW','INTU','BABA','META']

# Set up End and Start times for data grab
tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN','GOOGL','LNKD','PYPL','TWTR','EBAY','BIDU','SAP','CRM','ADBE','VMW','INTU','BABA','META']

end = '2024-07-05'
start = '2023-07-05'


for stock in tech_list:
    globals()[stock] = yf.download(stock, start, end)
    

company_list = [AAPL] # type: ignore


st.title('Stock Purchase Recommendation')


user_input = st.text_input('Enter stock ticker','AAPL')
df = pd.concat(company_list, axis=0)

#describing the data

st.subheader ('Date from 2023-2024')
st.write(df.describe())

    
#visualisation
st.subheader('Close Price History vs Date')
fig = plt.figure(figsize =(12,6))
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Close Price History vs Date with 100MA')
MA100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize =(12,6))
plt.plot(MA100,'p')
plt.plot(df.Close)
st.pyplot(fig)


st.subheader('Close Price History vs Date with 100MA AND 200MA')
MA100 = df.Close.rolling(100).mean()
MA200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize =(12,6))
plt.plot(MA100,'r')
plt.plot(MA200,'g')
plt.plot(df.Close,'b')
st.pyplot(fig)
