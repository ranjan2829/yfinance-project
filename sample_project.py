import yfinance as yf
import streamlit as st
import pandas as pd

# Here you can use markdown language to make your app prettier
st.write("""
# Financial App
""")








def main():
    st.title('Search Medium Story')
    stock = st.text_input('Enter search words:')
    
    # Get stock data
    get_stock_data = yf.Ticker(stock)

    # Set the time line of your data
    ticket_df = get_stock_data.history(period='1d', start='2021-1-02', end='2021-12-12')

    # Show your data in line chart
    st.line_chart(ticket_df.Close)
    st.line_chart(ticket_df.Volume)
if __name__ == '__main__':
    main()












