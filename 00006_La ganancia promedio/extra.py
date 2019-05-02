function longitud(lista) {
  return lista.length
}

function gananciaTotal(balancesDeUnPeriodo) {
  sumatoria = 0;
  for (balance of balancesDeUnPeriodo) {
    sumatoria = sumatoria + balance.ganancia;
  }
  return sumatoria;
}