import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objects as go


@st.cache_data
def load_data(ticker, start, today):
    data = yf.download(ticker, start=start, end=today)
    data.reset_index(inplace=True)
    return data

def plot_raw_data(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock close"))
    fig.layout.update(title_text="Stock Price Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig, use_container_width=True)