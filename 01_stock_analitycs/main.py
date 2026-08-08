from statistics import (
    first_close_price,
    last_close_price,
    performance,
    annualized_return
)

from risk import (
    annualized_volatility,
    sharpe_ratio,
    max_drawdown,
    positive_days,
    negative_days,
    win_rate,
    best_day,
    worst_day
)

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