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
    
    from bandl.nse_data import NseData
    nd = NseData()
    # returns 'NseData object'. can be use to get nse data.
    strikes = nd.get_oc_strike_prices("NIFTY")
    oc_data = nd.get_option_data("NIFTY",strikes=strikes)
    expiry_dates = nd.get_oc_exp_dates(symbol) #return available expiry dates
    nd.get_option_chain_excel(symbol,expiry_date,filepath) #dumps option chain to file_path
    # or get in pandas dateframe
    bn_df = nd.get_option_chain_df(symbol, expiry_date,dayfirst=False) #returns option chain in pandas data frame.
    data_frame = nd.get_data(symbol,series="EQ",start=None,end=None,periods=None,dayfirst=False) #returns historical data in pandas data frames
    part_oi_df = nd.get_part_oi_df(start=None,end=None,periods=None,dayfirst=False,workers=None)
    from bandl.nasdaq import Nasdaq
    testObj = Nasdaq() # returns 'Nasdaq class object'.
    dfs = testObj.get_data("AAPL",periods=15) # returns last 15 days data
    from bandl.yfinance import Yfinance
    testObj = Yfinance() # returns 'Yfinance class object'.
    #if US stock, then pass is_indian=False
    dfs = testObj.get_data("AAPL",is_indian=False) #by default, returns last years data
    #to get indian stock data
    dfs = testObj.get_data("SBIN",start="21-Jan-2020") #retruns data from 21Jan 2020 to till today
    from bandl.coinbase import Coinbase
    testObj = Coinbase() # returns 'Coinbase class object'.
    dfs = testObj.get_data("BTC-USD",start="21-Jan-2020",end="21-Jan-2021")#retruns data from 21Jan 2020 to 21-Jan-2021
    
 
if __name__ == '__main__':
    main()












