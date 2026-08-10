import numpy as np
from data import close_tte, daily_returns
from market_stats import annualized_return

daily_volatility = np.std(daily_returns, ddof=1)

annualized_volatility = np.multiply(daily_volatility, np.sqrt(252))

sharpe_ratio = np.divide(
    np.subtract(annualized_return, 0),
    annualized_volatility
)

max_drawdown = np.min(np.subtract(np.divide(close_tte, close_tte.cummax()), 1))

positive_days = np.sum(daily_returns > 0)
negative_days = np.sum(daily_returns < 0)

win_rate = np.divide(positive_days, np.add(positive_days, negative_days))

best_day = np.max(daily_returns)
worst_day = np.min(daily_returns)
