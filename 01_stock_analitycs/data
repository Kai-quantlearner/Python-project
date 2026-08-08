import numpy as np
import yfinance as yf

tte_data = yf.download('TTE.PA', period='1y')
close_tte = tte_data[('Close', 'TTE.PA')]
last_close_price_float = close_tte.iloc[-1]
first_close_price_float = close_tte.iloc[0]
last_close_price = tte_data['Close'].iloc[-1]
first_close_price = tte_data['Close'].iloc[0]
highest_price = tte_data['High'].max()
highest_price_float = highest_price.iloc[0]
lowest_price = tte_data['Low'].min()
lowest_price_float = lowest_price.iloc[0]
volume = tte_data['Volume'].mean()
volume_float = volume.iloc[0]
daily_returns = close_tte.pct_change().dropna()
mean_daily_return = daily_returns.mean()
daily_volatility = np.std(daily_returns, ddof=1)
annualized_volatility = np.multiply(daily_volatility, np.sqrt(252))
annualized_return = np.subtract(
    np.power(
        np.prod(
            np.add(daily_returns, 1)
        ),
        np.divide(252, len(daily_returns))
    ),
    1
)
sharpe_ratio = np.divide(
    np.subtract(annualized_return, 0),
    annualized_volatility
)
max_drawdown = np.min(np.subtract(np.divide(close_tte, close_tte.cummax()), 1))
positive_days = np.sum(daily_returns > 0)
negative_days = np.sum(daily_returns < 0)
Win_rate = np.divide(positive_days, np.add(positive_days, negative_days))
head = tte_data.head()
tail = tte_data.tail()
describe = tte_data.describe()
info = tte_data.info()
variation = np.subtract(last_close_price_float, first_close_price_float)
performance = np.multiply(np.divide(np.subtract(last_close_price_float, first_close_price_float), first_close_price_float), 100)
best_day = np.max(daily_returns)
worst_day = np.min(daily_returns)


print("Statistiques de l'action TotalEnergies (TTE.PA) sur la dernière année :",
       f"Premier prix : {first_close_price_float:.2f} €",
        f"Dernier prix : {last_close_price_float:.2f} €",
        f"Performance : {performance:.2f}%",
         f"Prix le plus élevé : {highest_price_float:.2f} €",
          f"Prix le plus bas : {lowest_price_float:.2f} €",
           f"Volume moyen : {volume_float:.0f}",
            f"Variation : {variation:.2f} €",
             f"Rendements quotidiens :\n{daily_returns}")
print(f"Rendement quotidien moyen : {mean_daily_return*100:.4f}%")
print(f"Volatilité quotidienne : {daily_volatility*100:.4f}%")
print(f"Volatilité annualisée : {annualized_volatility*100:.4f}%")
print(f"Rendement annualisé : {annualized_return*100:.4f}%")
print(f"Ratio de Sharpe : {sharpe_ratio:.4f}")
print(f"Drawdown maximal : {max_drawdown*100:.4f}%")
print(f"Nombre de jours positifs : {positive_days}")
print(f"Nombre de jours négatifs : {negative_days}")
print(f"Ratio de gain/perte : {Win_rate:.4f}")
print(f"Meilleur jour : {best_day*100:.4f}%")
print(f"Pire jour : {worst_day*100:.4f}%")