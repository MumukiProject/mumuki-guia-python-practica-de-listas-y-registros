/*...solution[8]...*/

/*...solution[9]...*/

def promedio(lista_de_numeros) {
	return sumatoria(lista_de_numeros) / longitud(lista_de_numeros);
}

def sumatoria(lista_de_numeros) {
  sumatoria = 0;
  for (numero of lista_de_numeros) {
    sumatoria = sumatoria + numero;
  }
  return sumatoria;
}

def agregar(lista, elemento) {
  return lista.push(elemento);
}

def longitud(lista) {
  return lista.length;
}