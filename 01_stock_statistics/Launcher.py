from stat import annualized_return, daily_returns, close_tte, first_close_price_float, last_close_price_float, performance
from risk import annualized_volatility, sharpe_ratio, max_drawdown,win_rate, best_day, worst_day, positive_days, negative_days

print(f"Premier prix : {first_close_price_float:.2f} €")
print(f"Dernier prix : {last_close_price_float:.2f} €")
print(f"Performance : {performance:.2f}%")

print(f"Rendement annualisé : {annualized_return * 100:.2f}%")
print(f"Volatilité annualisée : {annualized_volatility * 100:.2f}%")
print(f"Sharpe ratio : {sharpe_ratio:.2f}")
print(f"Maximum drawdown : {max_drawdown * 100:.2f}%")

print(f"Jours positifs : {positive_days}")
print(f"Jours négatifs : {negative_days}")
print(f"Win rate : {win_rate * 100:.2f}%")

print(f"Meilleur jour : {best_day * 100:.2f}%")
print(f"Pire jour : {worst_day * 100:.2f}%")