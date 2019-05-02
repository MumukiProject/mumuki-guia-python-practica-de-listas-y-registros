_Ahora que sabemos la función que necesitamos (`ganancia_total`), razonemos cómo hacerla..._

Vamos de a poquito :hand:: si la lista no tuviera elementos, ¿cuánto debería ser la sumatoria? ¡0!

```python
def ganancia_total_0(balances_de_un_periodo):
  sumatoria = 0
  return sumatoria
```

¿Y si tuviera exactamente 1 elemento? Sería... 0.... ¿más ese elemento? ¡Exacto! :sunglasses:

```python
def ganancia_total_1(balances_de_un_periodo):
  sumatoria = 0
  sumatoria = sumatoria + balances_de_un_periodo[0]["ganancia"]
  return sumatoria
```

¿Y si tuviera 2 elementos? :thought_balloon:

```python
def ganancia_total_2(balances_de_un_periodo):
  sumatoria = 0
  sumatoria = sumatoria + balances_de_un_periodo[0]["ganancia"]
  sumatoria = sumatoria + balances_de_un_periodo[1]["ganancia"]
  return sumatoria
```

¿Y si tuviera 3 elementos? :thought_balloon:

```python
def ganancia_total_3(balances_de_un_periodo):
  sumatoria = 0;
  sumatoria = sumatoria + balances_de_un_periodo[0]["ganancia"]
  sumatoria = sumatoria + balances_de_un_periodo[1]["ganancia"]
  sumatoria = sumatoria + balances_de_un_periodo[2]["ganancia"]
  return sumatoria
```

> ¿Empezás a ver un patrón? Tratá de escribir `ganancia_total_4` que funcione para 4 elementos.
