
		
		
		
import yfinance as yf
import streamlit as st
import pandas as pd

# Here you can use markdown language to make your app prettier
st.write("""
# Financial App
""")



from bs4 import BeautifulSoup as BS
import requests as req

from datetime import date

# Returns the current local date
today = date.today()



d = st.date_input(
    "Select the Historical data",
    date(2019, 7, 6))
st.write('your selected date is :', d)




# IMPORT ALL THE REQUIRED LIBRARIES
from bs4 import BeautifulSoup as BS
import requests as req

url = "https://www.businesstoday.in/latest/economy"

webpage = req.get(url)
trav = BS(webpage.content, "html.parser")
M = 1
for link in trav.find_all('a'):
	
	# PASTE THE CLASS TYPE THAT WE GET
	# FROM THE ABOVE CODE IN THIS AND
	# SET THE LIMIT GRATER THAN 35
	if(str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
	and len(link.string) > 35):

		st.write(str(M)+".", link.string)
		M += 1
























def main():
    st.title('Search Medium Story')
    stock = st.text_input('Enter search words:')
    
    # Get stock data
    get_stock_data = yf.Ticker(stock)

    # Set the time line of your data
    ticket_df = get_stock_data.history(period='1d', start=f'{d}', end=f'{today}')

    # Show your data in line chart
    st.bar_chart(ticket_df.Close)
    st.bar_chart(ticket_df.Volume)
# IMPORT ALL THE REQUIRED LIBRARIES






   
    
 
if __name__ == '__main__':
    main()

