def gananciaTotal(balancesDePeriodo) {
  sumatoria = 0;
  for (balance of balancesDePeriodo) {
    sumatoria = sumatoria + balance.ganancia;
  }
  return sumatoria;
}
