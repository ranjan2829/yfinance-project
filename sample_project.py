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
    
    # For data manipulation
    import numpy as np
    import pandas as pd

    # To fetch financial data
    import yfinance as yf

    # For visualisation
    import matplotlib.pyplot as plt
    plt.style.use('seaborn-darkgrid')


    # Set the ticker as 'EURUSD'
    forex_data = yf.download('EURUSD', start='2019-01-02', end='2021-12-31')

    # Set the index to a datetime object
    forex_data.index = pd.to_datetime(forex_data.index)

    # Display the last five rows
    forex_data.tail()




    # Plot the close price
    plt.figure(figsize=(15, 7))
    forex_data['Adj Close'].plot()

    # Set the title and axis label
    plt.title('EUR/USD Data', fontsize=16)
    plt.xlabel('Year-Month', fontsize=15)
    plt.ylabel('Price', fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.legend(['Close'], prop={'size': 15})

    # Show the plot
    plt.show()




    # Set the ticker as 'EURUSD'
    forex_data_minute = yf.download('EURUSD', period='5d', interval='1m')

    # Set the index to a datetime object
    forex_data_minute.index = pd.to_datetime(forex_data_minute.index)

    # Display the last five rows
    forex_data_minute.tail()



    # Transform index type from datetime to string
    forex_data_minute['dates'] = forex_data_minute.index.strftime(
        '%Y-%m-%d %H:%M:%S')

    # Plot the series
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.plot(forex_data_minute['dates'], forex_data_minute['Adj Close'])

    # Set title and axis label
    plt.title('EUR/USD Data', fontsize=16)
    plt.xlabel('Time', fontsize=15)
    plt.ylabel('Price', fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.legend(['Close'], prop={'size': 15})

    # Set maximum number of tick locators
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()




    # Plot the close price
    ax = plt.figure(figsize=(15, 7))

    # Plot both forex pairs
    ax = forex_data['EURUSD']['Close'].plot(label='EUR/USD')
    ax2 = forex_data['GBPUSD']['Close'].plot(secondary_y=True, color='g',  ax=ax, label='GBP/USD')

    # Set the title and axis labels
    plt.title('EUR/USD and GBP/USD Data', fontsize=16)
    ax.set_xlabel('Year-Month', fontsize=15)
    ax.set_ylabel('Close Prices', fontsize=15)
    ax2.set_ylabel('Close Prices', fontsize=15)
    ax.tick_params(axis='both', labelsize=15)
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1+h2, l1+l2, loc=2, prop={'size': 15})

    # Save the figure
    plt.savefig('Figures/EURUSD_and_GBPUSD_Daily_Data.png', bbox_inches = 'tight')
    # Show the plot
    plt.show()
if __name__ == '__main__':
    main()












