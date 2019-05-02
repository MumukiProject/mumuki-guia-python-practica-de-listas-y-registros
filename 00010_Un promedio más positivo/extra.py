/*...solution[8]...*/

/*...solution[9]...*/

def promedio(listaDeNumeros) {
	return sumatoria(listaDeNumeros) / longitud(listaDeNumeros);
}

def sumatoria(listaDeNumeros) {
  sumatoria = 0;
  for (numero of listaDeNumeros) {
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