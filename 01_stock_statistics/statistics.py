from data import  close_tte, daily_returns
import numpy as np

last_close_price_float = close_tte.iloc[-1]
first_close_price_float = close_tte.iloc[0]
last_close_price = tte_data['Close'].iloc[-1]
first_close_price = tte_data['Close'].iloc[0]
highest_price_float = highest_price.iloc[0]
lowest_price_float = lowest_price.iloc[0]
volume_float = volume.iloc[0]
mean_daily_return = daily_returns.mean()

annualized_return = np.subtract(
    np.power(
        np.prod(
            np.add(daily_returns, 1)
        ),
        np.divide(252, len(daily_returns))
    ),
    1
)
variation = np.subtract(last_close_price_float, first_close_price_float)
performance = np.multiply(np.divide(np.subtract(last_close_price_float, first_close_price_float), first_close_price_float), 100)