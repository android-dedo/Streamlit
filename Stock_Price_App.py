#!/usr/bin/env python
# coding: utf-8

import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""

# Stock Price App
Shown are stock closing price of Google and Apple

###### BY : **Andrew Adel Labib**

""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d' , start='2010-5-31' , end='2020-5-31')

st.write("""
### **Google Closing Price**
""")

st.line_chart(tickerDf.Close)

st.write("""
### **Google Volume Price**
""")

st.line_chart(tickerDf.Volume)

tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d' , start='2010-5-31' , end='2020-5-31')

st.write(""""
### **Apple Closing Price**
""")

st.line_chart(tickerDf.Close)

st.write(""""
### **Apple Volume Price**
""")

st.line_chart(tickerDf.Volume)
