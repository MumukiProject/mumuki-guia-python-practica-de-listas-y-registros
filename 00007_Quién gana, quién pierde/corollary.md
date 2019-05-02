Como podés ver todos los promedios se basan en el mismo principio :eyes:. Sumar una cantidad determinada elementos y dividir el resultado por esa cantidad. Si quisiéramos realizar una función `promedio` genérica sería algo así:

```python
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
```
¡Pero nosotros no tenemos una lista de números sino de registros! :fearful: ¿Y entonces? :thought_balloon:
