def ganancia_total(balances_de_periodo):
  sumatoria = 0
  for balance in balances_de_periodo:
    sumatoria = sumatoria + balance["ganancia"]
  return sumatoria