import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objects as go
from utils import *

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Price Prediction")

stocks = ("AAPL", "MSFT", "GOOG", "GME")
selected_stock = st.sidebar.selectbox("Select a stock", stocks)

n_years = st.sidebar.slider("Number of Years", 1, 5, 1)
period = n_years * 365

data_load_state = st.text('Loading data...')
data = load_data(selected_stock, START, TODAY)
data_load_state.text('Loading data...done!!!')

st.subheader("Raw data")
st.write(data.head())

plot_raw_data(data)

# Forecasting
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={'Date': 'ds', 'Close': 'y'})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)
st.subheader("Forecast")
st.write(forecast.head())

st.write("Forecast data")
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecase components")
fig2 = m.plot_components(forecast)
st.write(fig2)