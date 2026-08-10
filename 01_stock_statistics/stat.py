import numpy as np
from data import close_tte, daily_returns

first_close_price_float = close_tte.iloc[0]
last_close_price_float = close_tte.iloc[-1]
highest_price = close_tte.max()
lowest_price = close_tte.min()
variation = np.subtract(last_close_price_float, first_close_price_float)
performance = np.multiply(np.divide(variation, first_close_price_float), 100)

mean_daily_return = daily_returns.mean()
daily_volatility = np.std(daily_returns, ddof=1)
annualized_return = np.subtract(
    np.power(
        np.prod(
            np.add(daily_returns, 1)
        ),
        np.divide(252, len(daily_returns))
    ),
    1
)