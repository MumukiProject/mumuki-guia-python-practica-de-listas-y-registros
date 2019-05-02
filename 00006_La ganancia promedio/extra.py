def longitud(lista) {
  return lista.length
}

def ganancia_total(balances_de_un_periodo) {
  sumatoria = 0;
  for (balance of balances_de_un_periodo) {
    sumatoria = sumatoria + balance.ganancia;
  }
  return sumatoria;
}