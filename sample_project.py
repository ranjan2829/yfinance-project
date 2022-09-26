import yfinance as yf
import streamlit as st
import pandas as pd

# Here you can use markdown language to make your app prettier
st.write("""
# Financial App
""")





from datetime import date

# Returns the current local date
today = date.today()



d = st.date_input(
    "Select the Historical data",
    date(2019, 7, 6))
st.write('your selected date is :', d)





























def main():
    st.title('Search Medium Story')
    stock = st.text_input('Enter search words:')
    
    # Get stock data
    get_stock_data = yf.Ticker(stock)

    # Set the time line of your data
    ticket_df = get_stock_data.history(period='1d', start=f'{d}', end=f'{today}')

    # Show your data in line chart
    st.line_chart(ticket_df.Close)
    st.line_chart(ticket_df.Volume)


   
    
 
if __name__ == '__main__':
    main()












