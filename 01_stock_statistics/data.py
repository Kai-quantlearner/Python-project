import numpy as np
import yfinance as yf

tte_data = yf.download('TTE.PA', period='1y')

close_tte = tte_data[('Close', 'TTE.PA')]

daily_returns = close_tte.pct_change().dropna()

high_tte = tte_data[('High', 'TTE.PA')]
low_tte = tte_data[('Low', 'TTE.PA')]
volume_tte = tte_data[('Volume', 'TTE.PA')]