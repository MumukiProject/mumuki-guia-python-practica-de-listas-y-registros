function gananciaTotal(balancesDeUnPeriodo) {
  sumatoria = 0;
  for (balance of balancesDeUnPeriodo) {
    sumatoria = sumatoria + balance.ganancia;
  }
  return sumatoria;
}