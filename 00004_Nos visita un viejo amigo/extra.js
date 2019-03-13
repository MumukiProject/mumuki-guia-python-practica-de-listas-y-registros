function gananciaTotal(unPeriodo) {
  let sumatoria = 0;
  for (let gananciaDelMes of unPeriodo) {
    sumatoria = sumatoria + gananciaDelMes.ganancia;
  }
  return sumatoria;
}